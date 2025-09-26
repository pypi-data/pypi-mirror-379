from abc import abstractmethod
from typing import Callable, Iterable, ParamSpec, TypeVar, Concatenate
import functools


# TODO Track when the invalidatable should be deallocated
class Invalidatable:
    @abstractmethod
    def _invalidate(self):
        """To be called whenever an Invalidator being observed sends its signal."""
        ...


class Invalidator:
    @abstractmethod
    def _iter_invalidatables(self) -> Iterable[Invalidatable]: ...
    @abstractmethod
    def _add_invalidatable(self, invalidatable: Invalidatable):
        """Adds an :class :`Invalidatable` to this Invalidator."""
        ...


P = ParamSpec("P")
T = TypeVar("T")
_Invalidator = TypeVar("_Invalidator", bound=Invalidator)


def invalidates(
    method: Callable[Concatenate[_Invalidator, P], T],
) -> Callable[Concatenate[_Invalidator, P], T]:
    @functools.wraps(method)
    def invalidating_foo(self: _Invalidator, *args: P.args, **kwargs: P.kwargs) -> T:
        output = method(self, *args, **kwargs)
        for invalidatable in self._iter_invalidatables():  # type: ignore[reportPrivateUsage]
            invalidatable._invalidate()  # type: ignore[reportPrivateUsage]
        return output

    return invalidating_foo
