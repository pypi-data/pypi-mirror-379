from apscheduler.schedulers.background import BackgroundScheduler

def create_schedular_app() -> BackgroundScheduler:
    schedular = BackgroundScheduler()

    return schedular