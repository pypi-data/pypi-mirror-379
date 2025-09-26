from typing import Callable, Any, Tuple, Dict, Awaitable


class Task:
    func: Callable[..., Awaitable[Any]]
    args: Tuple[Any]
    kwargs: Dict[str, Any]