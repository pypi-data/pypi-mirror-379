from asyncio import Queue

from ._task import Task


class TaskQueue(Queue):

    def __init__(self):
        super().__init__()

        self.queue = Queue()

    async def get(self) -> Task:
        return await self.queue.get()

    async def put(self, task: Task):
        await self.queue.put(task)
