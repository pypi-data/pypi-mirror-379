# -*- coding: utf-8 -*-
#
# Author: GavinGong aka VisualDust
# Github: github.com/visualDust
# Date:   20250301

from typing import Any, Callable, Hashable, Optional


class CachedDict(dict):
    """
    A dict that lazily generates and stores values via a generator function.

    - If `unpack_tuple=True` and the key is a tuple, the key is unpacked into the
      generator: gen(*key). Otherwise, gen(key) is used.
    - `__getitem__` triggers generation (via __missing__).
    - `.get(key, default, generate=True)` can opt out of generation.
    """

    def __init__(self, gen: Callable[..., Any], unpack_tuple: bool = True):
        super().__init__()
        self._gen = gen
        self._unpack_tuple = unpack_tuple

    @property
    def gen(self) -> Callable[..., Any]:
        return self._gen

    def __missing__(self, key: Hashable) -> Any:
        val = (
            self._gen(*key)
            if (self._unpack_tuple and isinstance(key, tuple))
            else self._gen(key)
        )
        self[key] = val
        return val

    def get(
        self,
        key: Hashable,
        default: Optional[Any] = None,
        *,
        generate: bool = True
    ) -> Any:
        if generate:
            try:
                return self[key]  # triggers __missing__ if absent
            except Exception:
                return default
        return super().get(key, default)
