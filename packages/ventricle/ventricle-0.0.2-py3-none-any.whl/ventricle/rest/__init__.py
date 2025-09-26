from fastapi import FastAPI


def create_rest_app() -> FastAPI:
    """
    Create and configure a FastAPI REST application.
    :return: The configured FastAPI REST application.
    """
    app = FastAPI(title="Ventricle")
    return app