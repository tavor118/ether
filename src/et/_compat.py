from typing import Any, Callable, TypeVar

F = TypeVar("F", bound=Callable[..., Any])

try:
    from typing import dataclass_transform
except ImportError:  # Python < 3.11
    try:
        from typing_extensions import dataclass_transform
    except ImportError:

        def dataclass_transform(*args: Any, **kwargs: Any) -> Callable[[F], F]:
            def decorator(fn: F) -> F:
                return fn

            return decorator


__all__ = ["dataclass_transform"]
