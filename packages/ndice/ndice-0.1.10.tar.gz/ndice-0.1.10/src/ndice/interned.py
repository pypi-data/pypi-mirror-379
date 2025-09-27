from __future__ import annotations

import inspect

from collections import OrderedDict
from typing import Any, TypeVar


T = TypeVar('T')


def interned(class_: type[T]) -> type[T]:
    cache: dict[tuple, T] = {}
    original_new = class_.__new__

    def caching_new(cls: type[T], *args: Any, **kwargs: Any) -> T:
        arguments = _get_arguments(cls, *args, **kwargs)

        key = tuple(arguments.values())
        if key in cache:
            return cache[key]

        instance = original_new(cls)
        for name, value in arguments.items():
            object.__setattr__(instance, name, value)

        cache[key] = instance
        return instance

    setattr(class_, '__new__', caching_new)
    return class_


def _get_arguments(
    class_: type, *args: Any, **kwargs: Any
) -> OrderedDict[str, Any]:
    init_signature = inspect.signature(class_.__init__)  # type: ignore[misc]
    bound_arguments = init_signature.bind(None, *args, **kwargs)
    bound_arguments.apply_defaults()
    bound_arguments.arguments.pop('self')
    return bound_arguments.arguments
