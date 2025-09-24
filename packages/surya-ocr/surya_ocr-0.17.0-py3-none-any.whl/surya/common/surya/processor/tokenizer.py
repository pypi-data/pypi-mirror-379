import html
import re
from typing import List, Union, Dict, Optional, Tuple, Iterable
import numpy as np
import torch
from tokenizers import AddedToken
import json
import os
from transformers import PreTrainedTokenizer, Qwen2Tokenizer as Qwen2OriginalTokenizer


from surya.common.s3 import S3DownloaderMixin
from surya.common.surya.schema import TASK_NAMES, TaskNames
from surya.logging import get_logger
from surya.settings import settings

logger = get_logger()


def create_token_regex(tokens):
    escaped_tokens = [re.escape(token) for token in tokens]
    escaped_tokens.sort(key=len, reverse=True)
    pattern = r"^(" + "|".join(escaped_tokens) + r")"
    regex = re.compile(pattern)
    return regex


class InnerOCRTokenizer:
    def __init__(
        self,
        special_tokens: Dict[str, list] | None = None,
        qwen_tokenizer: Qwen2OriginalTokenizer | None = None,
        **kwargs,
    ):
        self.qwen_tokenizer = qwen_tokenizer
        self.qwen_token_offset = len(qwen_tokenizer)

        all_special_tokens = special_tokens.get("all", [])
        self.SPECIAL_TOKEN_MAPPING = {}

        idx = 0
        for tag in all_special_tokens:
            if tag in self.SPECIAL_TOKEN_MAPPING:
                continue
            self.SPECIAL_TOKEN_MAPPING[tag] = (
                idx + self.qwen_token_offset
            )  # Assign token ID
            idx += 1

        self.REVERSE_SPECIAL_TOKEN_MAPPING = {
            v: k for k, v in self.SPECIAL_TOKEN_MAPPING.items()
        }
        self.SPECIAL_TOKEN_OFFSET = idx
        self.FORMAT_TAG_PATTERN = create_token_regex(special_tokens["formatting"])
        self.MATH_TAG_PATTERN = create_token_regex(special_tokens["math_external"])
        self.LAYOUT_TAG_PATTERN = create_token_regex(special_tokens["layout"])
        self.TABLE_STRUCTURE_TAG_PATTERN = create_token_regex(
            special_tokens["table_structure"]
        )
        self.SYSTEM_TAG_PATTERN = create_token_regex(special_tokens.get("system", []))
        if not special_tokens.get("system", []):
            logger.warning("Warning: No system tokens found in special_tokens")

        self.MATH_TAG_START = "<math"
        self.MATH_END_TAG = "</math>"

        super().__init__(**kwargs)

    @property
    def vocab_size(self):
        return (
            65536 + self.SPECIAL_TOKEN_OFFSET
        )  # The highest codepoint is 65535, but we add 1 to account for the 0-indexing

    def _tokenize(self, text: str) -> List[int]:
        tokens = []
        in_math = False
        text = html.unescape(text)  # Unescape html entities like &lt; in equations
        while text:
            # Look for EOS, PAD, etc. tokens
            match = self.SYSTEM_TAG_PATTERN.search(text)
            if match:
                tag = match.group(1)
                tokens.append(
                    self.SPECIAL_TOKEN_MAPPING[tag]
                )  # These are already offset
                text = text[match.end() :]
                continue

            # Look for layout tokens
            match = self.LAYOUT_TAG_PATTERN.search(text)
            if match:
                tag = match.group(1)
                tokens.append(
                    self.SPECIAL_TOKEN_MAPPING[tag]
                )  # Layout tokens are already offset
                text = text[match.end() :]
                continue

            match = self.TABLE_STRUCTURE_TAG_PATTERN.search(text)
            if match:
                tag = match.group(1)
                tokens.append(self.SPECIAL_TOKEN_MAPPING[tag])
                text = text[match.end() :]
                continue

            # Check for math tags
            match = self.MATH_TAG_PATTERN.search(text)
            if match:
                # We found a tag
                tag = match.group(1)
                if tag.startswith(self.MATH_TAG_START):
                    in_math = True
                elif tag == self.MATH_END_TAG:
                    in_math = False
                tokens.append(
                    self.SPECIAL_TOKEN_MAPPING[tag]  # Special tokens are already offset
                )  # Use special token ID
                text = text[match.end() :]
                continue

            # Tokenize math content with qwen2 tokenizer
            if in_math:
                # If we're in a math block, check to see if we have a special math tag in the text
                math_end_position = text.find(self.MATH_END_TAG)
                math_str = text[:math_end_position]  # Gets the math content
                tokens += self.qwen_tokenizer(math_str)["input_ids"]
                text = text[math_end_position:]
                continue

            # Check for formatting tags
            match = self.FORMAT_TAG_PATTERN.search(text)
            if match:
                # We found a tag
                tag = match.group(1)
                tokens.append(
                    self.SPECIAL_TOKEN_MAPPING[tag]  # Special tokens are already offset
                )  # Use special token ID
                text = text[match.end() :]
                continue

            # General case, utf-16 tokenization
            utf_16_tokens = self.text_to_utf16_numbers(text[0])
            tokens += [
                t + self.SPECIAL_TOKEN_OFFSET + self.qwen_token_offset
                for t in utf_16_tokens
            ]
            text = text[1:]

        return tokens

    def text_to_utf16_numbers(self, text: str):
        """Converts text to UTF-16 encoded numbers."""
        utf16_bytes = text.encode(
            "utf-16le"
        )  # Little-endian to simplify byte order handling
        numbers = []

        for i in range(0, len(utf16_bytes), 2):
            # Combine two adjacent bytes into a single number
            number = utf16_bytes[i] + (utf16_bytes[i + 1] << 8)
            numbers.append(number)

        return numbers

    def utf16_numbers_to_text(self, numbers):
        """Converts UTF-16 numbers back to text."""
        byte_array = bytearray()
        for number in numbers:
            byte_array.append(number & 0xFF)  # Lower byte
            byte_array.append((number >> 8) & 0xFF)  # Upper byte

        try:
            text = byte_array.decode("utf-16le", errors="ignore")
        except Exception as e:
            logger.warning(f"Error decoding utf16: {e}")
            text = ""

        return text

    def __call__(
        self, texts: Union[str, List[str]], **kwargs
    ) -> Dict[str, List[List[int]]]:
        """Tokenizes text and returns input IDs."""
        tokenized = []

        if isinstance(texts, str):
            texts = [texts]

        for text in texts:
            tokens = self._tokenize(text)
            tokenized.append(tokens)

        return {"input_ids": tokenized}

    def decode(self, token_ids, **kwargs):
        """Decodes token IDs back to text."""
        if isinstance(token_ids, (np.ndarray, torch.Tensor)):
            token_ids = token_ids.tolist()

        decoded_text = ""
        token_buffer = []
        decode_qwen = [False]

        def decode_buffer():
            nonlocal decoded_text, token_buffer, decode_qwen
            if token_buffer:
                if decode_qwen[0]:
                    decoded_text += self.qwen_tokenizer.decode(token_buffer)
                else:
                    token_buffer = [
                        t - self.SPECIAL_TOKEN_OFFSET - self.qwen_token_offset
                        for t in token_buffer
                    ]
                    decoded_text += self.utf16_numbers_to_text(token_buffer)

            token_buffer = []
            decode_qwen[0] = False

        for t in token_ids:
            if t < self.qwen_token_offset:
                # This is for math tags
                if token_buffer and token_buffer[-1] >= self.qwen_token_offset:
                    decode_buffer()
                token_buffer.append(t)
                decode_qwen[0] = True
            elif t >= self.SPECIAL_TOKEN_OFFSET + self.qwen_token_offset:
                if token_buffer and token_buffer[-1] < self.qwen_token_offset:
                    decode_buffer()
                token_buffer.append(t)  # We shift this down later on
                decode_qwen[0] = False
            elif t in self.REVERSE_SPECIAL_TOKEN_MAPPING:
                decode_buffer()
                decoded_text += self.REVERSE_SPECIAL_TOKEN_MAPPING[t]
                decode_qwen[0] = False
            else:
                raise ValueError(
                    f'Unexpected token value while decoding, got "{t}" in token_ids {token_ids}'
                )

        # Detokenize remaining tokens
        decode_buffer()

        return decoded_text


class Qwen2Tokenizer(S3DownloaderMixin, Qwen2OriginalTokenizer):
    pass

class GreedyMathUTF16Tokenizer(S3DownloaderMixin, PreTrainedTokenizer):
    """
    HuggingFace slow tokenizer implementing:
      - UTF-16 code units as the base [0..65535]
      - Math tokens as greedy-longest-match ids after UTF-16
      - Literal special tokens after math tokens
    Absolute ID layout:
      [0 .. 65535]                      : UTF-16 units
      [65536 .. 65536+M-1]              : math tokens
      [65536+M .. 65536+M+S-1]          : special tokens
    """

    vocab_files_names = {
        "vocab_file": "vocab_math.json",  # {"\\frac": 0, "\\alpha": 1, ...} raw contiguous ids 0..M-1
        "specials_file": "specials.json",  # [flat list for legacy]
        "specials_dict_file": "specials_dict.json",  # category dict (preferred)
    }
    model_input_names = ["input_ids", "attention_mask"]
    is_fast = False

    # ---------- helpers ----------
    @staticmethod
    def _to_utf16_units(s: str) -> List[int]:
        b = s.encode("utf-16le")
        return [int.from_bytes(b[i : i + 2], "little") for i in range(0, len(b), 2)]

    @staticmethod
    def _from_utf16_units(units: List[int]) -> str:
        b = bytearray()
        for u in units:
            b += int(u).to_bytes(2, "little")
        return b.decode("utf-16le", errors="ignore")

    class _TrieNode:
        __slots__ = ("child", "id", "leaf")

        def __init__(self):
            self.child: Dict[str, "GreedyMathUTF16Tokenizer._TrieNode"] = {}
            self.id: Optional[int] = None
            self.leaf: bool = False

    @classmethod
    def _build_trie(
        cls, token_to_id: Dict[str, int]
    ) -> "GreedyMathUTF16Tokenizer._TrieNode":
        root = cls._TrieNode()
        for tok, tid in token_to_id.items():
            node = root
            for ch in tok:
                node = node.child.setdefault(ch, cls._TrieNode())
            node.leaf = True
            node.id = tid
        return root

    @classmethod
    def _encode_math_greedy(
        cls,
        s: str,
        trie: "GreedyMathUTF16Tokenizer._TrieNode",
        math_base: int,
        debug: bool = False,
    ) -> List[int]:
        i, n = 0, len(s)
        out: List[int] = []
        while i < n:
            node = trie
            j = i
            last_id = None
            last_j = i
            while j < n and (ch := s[j]) in node.child:
                node = node.child[ch]
                j += 1
                if node.leaf:
                    last_id, last_j = node.id, j
            if last_id is not None:
                if debug:
                    print(f"[MATH] matched {s[i:last_j]!r} -> {last_id}")
                out.append(math_base + last_id)
                i = last_j
            else:
                units = cls._to_utf16_units(s[i])
                if debug:
                    print(f"[MATH] fallback {s[i]!r} -> utf16 {units}")
                out.extend(units)
                i += 1
        return out

    # ---------- init ----------
    def __init__(
        self,
        vocab_file: Optional[str] = None,
        specials_file: Optional[str] = None,
        specials_dict_file: Optional[str] = None,
        *,
        # You can also pass programmatically instead of files:
        math_vocab: Optional[Dict[str, int]] = None,
        special_tokens: Optional[List[str]] = None,
        special_tokens_dict: Optional[Dict[str, List[str]]] = None,
        debug: bool = False,
        # Standard HF special token kwargs:
        bos_token: Optional[str] = None,
        eos_token: Optional[str] = None,
        pad_token: Optional[str] = None,
        unk_token: Optional[str] = None,
        **kwargs,
    ):
        # Load math vocab
        if vocab_file and os.path.isfile(vocab_file):
            with open(vocab_file, "r", encoding="utf-8") as f:
                mv = json.load(f)
        else:
            mv = math_vocab or {}

        # Make math ids contiguous if needed
        if mv:
            max_id = max(mv.values())
            if set(mv.values()) != set(range(max_id + 1)):
                items = sorted(mv.items(), key=lambda kv: kv[1])
                mv = {tok: i for i, (tok, _) in enumerate(items)}

        # Load special tokens (prefer category dict; fallback to flat list or defaults)
        sp_dict = None
        if specials_dict_file and os.path.isfile(specials_dict_file):
            with open(specials_dict_file, "r", encoding="utf-8") as f:
                sp_dict = json.load(f)
        elif special_tokens_dict is not None:
            sp_dict = dict(special_tokens_dict)

        if sp_dict is None:
            # Legacy path: flat list from file or provided/default list
            if specials_file and os.path.isfile(specials_file):
                with open(specials_file, "r", encoding="utf-8") as f:
                    sp_list_flat = json.load(f)
            else:
                sp_list_flat = special_tokens or SPECIAL_TOKENS
            sp_dict = {"all": list(sp_list_flat)}

        # Ensure "all" exists and is unique/preserved in order.
        if "all" not in sp_dict or not isinstance(sp_dict["all"], list):
            order = [
                "system",
                "formatting",
                "math_external",
                "script",
                "layout",
                "reasoning",
                "table_structure",
                "reserved",
            ]
            seen = set()
            all_tokens: List[str] = []
            for k in order:
                if k in sp_dict and isinstance(sp_dict[k], list):
                    for t in sp_dict[k]:
                        if t not in seen:
                            all_tokens.append(t)
                            seen.add(t)
            sp_dict["all"] = all_tokens

        # Keep a copy of categories (if present) for downstream processor logic.
        self.special_tokens = sp_dict
        sp_list = list(sp_dict.get("all", []))
        # Regex list should favor longest-first to avoid partial matches.
        specials_for_regex = sorted(sp_list, key=len, reverse=True)

        self.debug = debug
        self.UTF16_SPACE = 65536
        self.math_token_to_rawid = dict(mv)  # 0..M-1
        self.math_vocab_size = len(self.math_token_to_rawid)
        self.MATH_BASE = self.UTF16_SPACE
        self.SPECIAL_BASE = self.UTF16_SPACE + self.math_vocab_size

        # Maps
        self.math_absid_to_token = {
            self.MATH_BASE + rid: tok for tok, rid in self.math_token_to_rawid.items()
        }
        self.special_tokens_list = sp_list  # ID assignment order
        self.special_to_absid = {
            tok: self.SPECIAL_BASE + i for i, tok in enumerate(self.special_tokens_list)
        }
        self.absid_to_special = {v: k for k, v in self.special_to_absid.items()}

        # Public attributes for legacy/processor:
        # All specials mapping (token -> absolute id)
        self.SPECIAL_TOKEN_MAPPING: Dict[str, int] = dict(self.special_to_absid)
        # Subset used heavily by processor for quick access
        self.reverse_special_token_mapping = {
            v: k for k, v in self.SPECIAL_TOKEN_MAPPING.items()
        }
        self.LAYOUT_LABEL2ID = {
            k: v
            for k, v in self.SPECIAL_TOKEN_MAPPING.items()
            if k in self.special_tokens["layout"]
        }
        self.TABLE_STRUCTURE_LABEL2ID = {
            k: v
            for k, v in self.SPECIAL_TOKEN_MAPPING.items()
            if k in self.special_tokens["table_structure"]
        }
        if not self.special_tokens.get("system", []):
            print("Warning: No system tokens found in special_tokens")

        self.MATH_TAG_START = "<math"
        self.MATH_END_TAG = "</math>"

        sys_list = self.special_tokens.get("system", [])
        self.system_tokens: Dict[str, int] = {
            t: self.special_to_absid[t] for t in sys_list if t in self.special_to_absid
        }

        # Regex for literal specials
        self.specials_pattern = (
            re.compile(r"(" + "|".join(re.escape(k) for k in specials_for_regex) + r")")
            if specials_for_regex
            else None
        )

        # Trie for math greedy match
        self.trie = self._build_trie(self.math_token_to_rawid)

        # Tell HF about special tokens (metadata)
        kwargs.setdefault("bos_token", bos_token)
        kwargs.setdefault("eos_token", eos_token or "</S>")
        kwargs.setdefault("pad_token", pad_token or "<PAD>")
        kwargs.setdefault("unk_token", unk_token)

        super().__init__(
            vocab_file=vocab_file,
            specials_file=specials_file,
            specials_dict_file=specials_dict_file,
            **kwargs,
        )

    # ---------- required HF surface ----------
    @property
    def vocab_size(self) -> int:
        return self.UTF16_SPACE + self.math_vocab_size + len(self.special_tokens_list)

    def get_vocab(self) -> Dict[str, int]:
        # Compact vocab: just math+specials with ABSOLUTE ids.
        v = {tok: self.MATH_BASE + rid for tok, rid in self.math_token_to_rawid.items()}
        v.update(self.special_to_absid)
        return v

    def __len__(self) -> int:
        return self.vocab_size

    # Core encode/decode on ABSOLUTE ids
    def _encode_core(self, text: str) -> List[int]:
        text = html.unescape(text)
        ids: List[int] = []
        in_math = False
        chunks = self.specials_pattern.split(text) if self.specials_pattern else [text]
        for chunk in chunks:
            if chunk in self.special_to_absid:
                ids.append(self.special_to_absid[chunk])
                if chunk.startswith("<math"):
                    in_math = True
                elif chunk.startswith("</math>"):
                    in_math = False
                if self.debug:
                    print(f"[TAG] {chunk!r} -> {self.special_to_absid[chunk]}")
                continue

            if in_math:
                ids.extend(
                    self._encode_math_greedy(
                        chunk, self.trie, self.MATH_BASE, debug=self.debug
                    )
                )
            else:
                units = self._to_utf16_units(chunk)
                if self.debug and units:
                    print(
                        f"[TEXT] utf16 {chunk[:32]!r} -> {units[:8]}{'...' if len(units) > 8 else ''}"
                    )
                ids.extend(units)
        return ids

    def _decode_core(self, ids: Iterable[int]) -> str:
        out: List[str] = []
        buf: List[int] = []

        def flush():
            if buf:
                out.append(self._from_utf16_units(buf))
                buf.clear()

        for tid in ids:
            if tid >= self.MATH_BASE and tid < self.SPECIAL_BASE:
                flush()
                out.append(self.math_absid_to_token.get(tid, ""))
            elif tid >= self.SPECIAL_BASE:
                flush()
                out.append(self.absid_to_special.get(tid, ""))
            else:
                buf.append(int(tid))
        flush()
        return "".join(out)

    # ---- Tokenizer interface ----
    def _tokenize(self, text: str, **kwargs) -> List[str]:
        ids = self._encode_core(text)
        toks: List[str] = []
        for i in ids:
            if i < self.MATH_BASE:
                toks.append(f"<U+{i:04X}>")
            elif i < self.SPECIAL_BASE:
                toks.append(self.math_absid_to_token.get(i, "<UNK_MATH>"))
            else:
                toks.append(self.absid_to_special.get(i, "<UNK_SPECIAL>"))
        return toks

    def _convert_token_to_id(self, token: str) -> int:
        if token.startswith("<U+") and token.endswith(">"):
            try:
                return int(token[3:-1], 16)  # UTF-16 unit
            except Exception:
                return self.unk_token_id if self.unk_token_id is not None else 0
        # math or specials
        if token in self.math_token_to_rawid:
            return self.MATH_BASE + self.math_token_to_rawid[token]
        if token in self.special_to_absid:
            return self.special_to_absid[token]
        # rare path: single-char token -> its UTF-16 unit
        if len(token) == 1:
            u = self._to_utf16_units(token)
            if len(u) == 1:
                return u[0]
        return self.unk_token_id if self.unk_token_id is not None else 0

    def _convert_id_to_token(self, index: int) -> str:
        if index < self.MATH_BASE:
            return f"<U+{index:04X}>"
        if index < self.SPECIAL_BASE:
            return self.math_absid_to_token.get(index, "<UNK_MATH>")
        return self.absid_to_special.get(index, "<UNK_SPECIAL>")

    def convert_tokens_to_string(self, tokens: List[str]) -> str:
        ids = [self._convert_token_to_id(t) for t in tokens]
        return self._decode_core(ids)

    def decode(self, token_ids, skip_special_tokens: bool = False, **kwargs) -> str:
        # Accept int, list, tuple, numpy, torch
        if hasattr(token_ids, "tolist"):
            token_ids = token_ids.tolist()
        elif isinstance(token_ids, int):
            token_ids = [token_ids]
        else:
            token_ids = list(token_ids)
        token_ids = [int(i) for i in token_ids]  # normalize early

        if skip_special_tokens:
            token_ids = [i for i in token_ids if i < self.SPECIAL_BASE]
        return self._decode_core(token_ids)

    # HF plumbing
    def build_inputs_with_special_tokens(
        self, token_ids_0: List[int], token_ids_1: Optional[List[int]] = None
    ) -> List[int]:
        out = (
            list(token_ids_0)
            if token_ids_1 is None
            else list(token_ids_0) + list(token_ids_1)
        )
        # if self.eos_token_id is not None and (not out or out[-1] != self.eos_token_id):
        #     out.append(self.eos_token_id)
        return out

    def get_special_tokens_mask(
        self,
        token_ids_0: List[int],
        token_ids_1: Optional[List[int]] = None,
        already_has_special_tokens: bool = False,
    ) -> List[int]:
        def mask(seq: List[int]) -> List[int]:
            return [1 if i >= self.SPECIAL_BASE else 0 for i in seq]

        return (
            mask(token_ids_0)
            if token_ids_1 is None
            else mask(token_ids_0) + mask(token_ids_1)
        )

    def create_token_type_ids_from_sequences(
        self, token_ids_0: List[int], token_ids_1: Optional[List[int]] = None
    ) -> List[int]:
        return [0] * (
            len(token_ids_0)
            if token_ids_1 is None
            else len(token_ids_0) + len(token_ids_1)
        )

    # Save/load raw assets
    def save_vocabulary(
        self, save_directory: str, filename_prefix: Optional[str] = None
    ) -> Tuple[str, str]:
        os.makedirs(save_directory, exist_ok=True)
        pre = (filename_prefix + "-") if filename_prefix else ""
        vocab_path = os.path.join(
            save_directory, pre + self.vocab_files_names["vocab_file"]
        )
        specials_path = os.path.join(
            save_directory, pre + self.vocab_files_names["specials_file"]
        )
        specials_dict_path = os.path.join(
            save_directory, pre + self.vocab_files_names["specials_dict_file"]
        )
        with open(vocab_path, "w", encoding="utf-8") as f:
            json.dump(self.math_token_to_rawid, f, ensure_ascii=False, indent=2)
        # Save both the flat list ("all") and the category dict (preferred)
        with open(specials_path, "w", encoding="utf-8") as f:
            json.dump(self.special_tokens_list, f, ensure_ascii=False, indent=2)
        with open(specials_dict_path, "w", encoding="utf-8") as f:
            json.dump(self.special_tokens, f, ensure_ascii=False, indent=2)
        return (vocab_path, specials_path)


class SuryaOCRTokenizer(S3DownloaderMixin, PreTrainedTokenizer):
    def __init__(
        self,
        special_tokens: Dict[str, list] | None = None,
        model_checkpoint: str = settings.FOUNDATION_MODEL_CHECKPOINT,
        **kwargs,
    ):
        if special_tokens is None:
            special_tokens = dict()

        self.special_tokens = special_tokens

        self.ocr_tokenizer = GreedyMathUTF16Tokenizer.from_pretrained(
            model_checkpoint,
        )
        self.system_tokens = {
            v: self.ocr_tokenizer(v)["input_ids"][0]
            for v in special_tokens.get("system", [])
        }
        self.SPECIAL_TOKEN_MAPPING = self.ocr_tokenizer.SPECIAL_TOKEN_MAPPING

        super().__init__(**kwargs)

    def get_vocab(self) -> Dict[str, int]:
        return self.ocr_tokenizer.get_vocab()

    def _add_tokens(
        self,
        new_tokens: Union[List[str], List[AddedToken]],
        special_tokens: bool = False,
    ) -> int:
        return self.ocr_tokenizer._add_tokens(
            new_tokens, special_tokens=special_tokens
        )

    @property
    def vocab_size(self):
        return self.ocr_tokenizer.vocab_size

    def _tokenize(self, text: str, **kwargs):
        # task = kwargs.get("task", TaskNames.ocr_with_boxes)
        # assert task in TASK_NAMES, f"Invalid task: {task}"

        tokens = self.ocr_tokenizer(text)["input_ids"]

        return tokens

    def __call__(
        self,
        texts: Union[str, List[str]],
        tasks: Union[str, List[str]] = None,
        **kwargs,
    ) -> Dict[str, List[List[int]]]:
        """Tokenizes text and returns input IDs."""
        tokenized = []

        if isinstance(texts, str):
            texts = [texts]
            assert isinstance(tasks, str), "Tasks must be a string if texts is a string"
            tasks = [tasks]

        if isinstance(texts, list):
            assert isinstance(tasks, list), "Tasks must be a list if texts is a list"

        for text, task in zip(texts, tasks):
            tokens = self._tokenize(text, task=task)
            tokenized.append(tokens)

        return {"input_ids": tokenized}

    def decode(self, token_ids, **kwargs):
        if isinstance(token_ids, (np.ndarray, torch.Tensor)):
            token_ids = token_ids.tolist()

        decoded_text = self.ocr_tokenizer.decode(token_ids, skip_special_tokens=False)
        # replace all <SCRIPT-...> tokens with empty strings
        decoded_text = re.sub(r"<SCRIPT-.*?>", "", decoded_text)
        # replace </S> with empty string
        decoded_text = re.sub(r"</S>", "", decoded_text)
        return decoded_text
