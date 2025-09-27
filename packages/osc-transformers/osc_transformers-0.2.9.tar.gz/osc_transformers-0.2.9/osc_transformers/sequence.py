from copy import copy
from enum import Enum, auto
from itertools import count
from typing import List

from .sampler import SamplingParams


class SequenceStatus(Enum):
    WAITING = auto()
    RUNNING = auto()
    FINISHED = auto()
    FAILED = auto()


class Sequence:
    counter = count()

    def __init__(
        self,
        token_ids: List[int],
        sampling_params=SamplingParams(),
        end_char: str = "[NONE]",
        stream_response: bool = False,
        block_size: int = 256,
        ignore_eos: bool = False,
    ):
        self.seq_id = next(Sequence.counter)
        self.status = SequenceStatus.WAITING
        self.token_ids = copy(token_ids)
        self.last_token = token_ids[-1]
        self.num_tokens = len(self.token_ids)
        self.num_prompt_tokens = len(token_ids)
        self.num_cached_tokens = 0
        self.block_table = []
        self.block_size = block_size
        self.temperature = sampling_params.temperature
        self.ignore_eos = ignore_eos
        self.end_char = end_char
        self.stream_response = stream_response
        self.sampling_params = sampling_params
        self.error_message = None

    @property
    def is_finished(self):
        return self.status == SequenceStatus.FINISHED

    @property
    def num_completion_tokens(self):
        return self.num_tokens - self.num_prompt_tokens

    @property
    def prompt_token_ids(self):
        return self.token_ids[: self.num_prompt_tokens]

    @property
    def completion_token_ids(self):
        return self.token_ids[self.num_prompt_tokens :]

    @property
    def num_cached_blocks(self):
        return self.num_cached_tokens // self.block_size

    @property
    def num_blocks(self):
        return (self.num_tokens + self.block_size - 1) // self.block_size

    @property
    def last_block_num_tokens(self):
        return self.num_tokens - (self.num_blocks - 1) * self.block_size

    def block(self, i: int) -> List[int]:
        """get token ids of the i-th block"""
        assert 0 <= i < self.num_blocks
        return self.token_ids[i * self.block_size : (i + 1) * self.block_size]

    def append_token(self, token_id: int) -> None:
        self.token_ids.append(token_id)
        self.last_token = token_id
        self.num_tokens += 1

    def reset(self) -> None:
        """reset sequence to initial state for reuse"""
        self.token_ids = self.token_ids[: self.num_prompt_tokens]
        self.last_token = self.token_ids[-1]
        self.num_tokens = self.num_prompt_tokens
        self.num_cached_tokens = 0
        self.block_table.clear()
        self.status = SequenceStatus.WAITING
        self.error_message = None

    def __getstate__(self):
        return (
            self.num_tokens,
            self.num_prompt_tokens,
            self.num_cached_tokens,
            self.block_table,
            self.token_ids if self.num_completion_tokens == 0 else self.last_token,
            self.error_message,
        )

    def __setstate__(self, state):
        (
            self.num_tokens,
            self.num_prompt_tokens,
            self.num_cached_tokens,
            self.block_table,
            self.error_message,
        ) = state[:-1]
        if self.num_completion_tokens == 0:
            self.token_ids = state[-1]
        else:
            self.last_token = state[-1]

    def __len__(self):
        return self.num_tokens

    def __getitem__(self, key):
        return self.token_ids[key]
