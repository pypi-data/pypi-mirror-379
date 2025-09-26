from typing import Callable, Any, Tuple, Dict, Awaitable

from pydantic import BaseModel


class Task(BaseModel):
    func: Callable[..., Awaitable[Any]]
    args: Tuple[Any]
    kwargs: Dict[str, Any]