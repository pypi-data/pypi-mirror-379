import time
import logging
from concurrent.futures import ThreadPoolExecutor

from .singleton_registry import SingletonRegistry
from .singleton import Singleton

logger = logging.getLogger("akris.scheduler")


class Scheduler(Singleton):
    def __init__(self):
        self.schedule_executor = None
        self.stopped = False
        self.tasks = []
        self.db = SingletonRegistry.get_instance().get("Database").get_instance()

    # accepts a task in the form of a function pointer
    def register_task(self, task, interval_knob):
        self.tasks.append({"task": task, "interval_knob": interval_knob, "last_run": 0})

    def run(self):
        while not self.stopped:
            for task in self.tasks:
                # get the interval from the database
                interval = self.db.get_knob(task["interval_knob"])
                # don't run tasks with an interval of 0
                if interval is None:
                    continue

                if task["last_run"] + interval < time.time():
                    task["task"]()
                    task["last_run"] = time.time()
            time.sleep(0.5)

    def start(self):
        self.schedule_executor = ThreadPoolExecutor(
            max_workers=1, thread_name_prefix="scheduler"
        )
        future = self.schedule_executor.submit(self.run)
        future.add_done_callback(self.handle_scheduler_done)

    def stop(self):
        self.stopped = True
        self.schedule_executor.shutdown(wait=False)

    def handle_scheduler_done(self, future):
        logger.info("run stopped")
        ex = future.exception()
        if ex is not None:
            logger.exception(f"exception in scheduler: {ex}")
