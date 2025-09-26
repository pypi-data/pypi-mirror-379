import asyncio
from asyncio import Queue, AbstractEventLoop

from ._task import Task


class TaskQueue:

    def __init__(self):
        super().__init__()

        self._loop: AbstractEventLoop | None = None
        self._q: Queue[Task] | None = None

        self.queue = Queue()

    async def start(self) -> None:
        """
        Initialize the queue inside the running loop.
        Must be awaited from the target loop/thread.
        """
        self._loop = asyncio.get_running_loop()
        self._q = asyncio.Queue()

    async def get(self) -> Task:
        """
        Get a task to the queue.
        :return: None
        """
        assert self._q is not None
        return await self.queue.get()

    async def put(self, task: Task) -> None:
        """
        Add a task to the queue.
        :param task: The task to add.
        :return: None
        """
        assert self._loop is not None and self._q is not None
        self._loop.call_soon_threadsafe(self._q.put_nowait, task)
