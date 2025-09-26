from asyncio import Queue

from ._task import Task


class TaskQueue:

    def __init__(self):
        super().__init__()

        self.queue = Queue()

    async def get(self) -> Task:
        """
        Get a task to the queue.
        :return: None
        """
        return await self.queue.get()

    async def put(self, task: Task) -> None:
        """
        Add a task to the queue.
        :param task: The task to add.
        :return: None
        """
        await self.queue.put(task)
