import sys
import os
import time
import py_compile
import runpy
import logging
from multiprocessing import Process
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# Logging konfigurieren
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%H:%M:%S",
)
logger = logging.getLogger(__name__)


def run_target(file_to_watch):
    """Startet das angegebene Python-Skript als eigenes __main__."""
    runpy.run_path(file_to_watch, run_name="__main__")


class HRHandler(FileSystemEventHandler):
    def initialize(self, hot_reload_instance, file_to_watch):
        self.hot_reload_instance = hot_reload_instance
        self.file_to_watch = os.path.abspath(file_to_watch)

    def on_modified(self, event):
        if os.path.abspath(event.src_path) != self.file_to_watch:
            return
        if not event.src_path.endswith(".py"):
            return

        if self.hot_reload_instance.check_syntax(self.file_to_watch):
            logger.info(f"✅ Syntax OK, restarting {self.file_to_watch}...")
            self.hot_reload_instance.restart_modified()
        else:
            logger.error(f"❌ Syntax error in {self.file_to_watch}, not reloading.")


class HotReload:
    def __init__(self, file_to_watch):
        self.file_to_watch = os.path.abspath(file_to_watch)
        self.process = None
        self.observer = None

    def start_process(self):
        self.process = Process(target=run_target, args=(self.file_to_watch,))
        self.process.start()
        logger.info(f"Started process PID={self.process.pid} for {self.file_to_watch}")

    def start_watchdog(self):
        event_handler = HRHandler()
        event_handler.initialize(self, self.file_to_watch)

        folder = os.path.dirname(self.file_to_watch)
        self.observer = Observer()
        self.observer.schedule(event_handler, folder, recursive=False)
        self.observer.start()
        logger.info(f"Watching file: {self.file_to_watch}")

    def check_syntax(self, file_path):
        try:
            py_compile.compile(file_path, doraise=True)
            return True
        except py_compile.PyCompileError as e:
            logger.error(f"Syntax compilation error: {e}")
            return False

    def restart_modified(self):
        if self.process and self.process.is_alive():
            logger.info(f"Terminating process PID={self.process.pid}")
            self.process.terminate()
            self.process.join()
            time.sleep(0.2)
        self.start_process()

    def run(self):
        self.start_process()
        self.start_watchdog()


if __name__ == "__main__":
    if len(sys.argv) < 2:
        logger.error("Usage: hotreload <file.py>")
        sys.exit(1)

    file_to_watch = sys.argv[1]
    hr = HotReload(file_to_watch)
    hr.run()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        logger.info("Beende HotReload...")
        if hr.process:
            hr.process.terminate()
            hr.process.join()
        if hr.observer:
            hr.observer.stop()
            hr.observer.join()
        logger.info("HotReload beendet.")