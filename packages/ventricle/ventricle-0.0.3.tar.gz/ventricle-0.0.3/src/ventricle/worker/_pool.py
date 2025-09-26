from ._worker import Worker
from ._task_queue import TaskQueue

class WorkerPool:

    def __init__(self, concurrency:int) -> None:
        """
        The main worker pool class.
        :param concurrency: The number of concurrency workers.
        """

        # initialize the worker queue
        _worker_queue = TaskQueue()


        # initialize the worker
        self._workers = [Worker(_worker_queue) for _ in range(concurrency)]

    def start(self):
        for worker in self._workers:
            worker.start()