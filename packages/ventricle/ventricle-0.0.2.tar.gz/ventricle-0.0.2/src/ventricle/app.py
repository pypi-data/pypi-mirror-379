from .rest import create_rest_app
from .scheduler import create_schedular_app
import uvicorn


class Ventricle:

    def __init__(self):
        self.rest = create_rest_app()
        self.scheduler = create_schedular_app()
        pass

    def start(self, rest:bool=True, schedular:bool=True):
        """
        Start the Ventricle app.
        :param rest: If the REST server should be started.
        :param schedular: If the scheduler should be started.
        :return: None
        """
        if schedular:
            self.scheduler.start()

        if rest:
            uvicorn.run(
                self.rest,
                host="0.0.0.0",
                port=8000
            )

