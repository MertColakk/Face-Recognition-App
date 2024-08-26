# Libraries
import time
import threading

class Timekeeper:
    def __init__(self, target_seconds : int):
        self.target_seconds = target_seconds
        self.running = False
        self.thread = None
        self.current = 0
        self.finished = False

    def start(self):
        if not self.running and self.finished is False:
            self.running = True
            self.thread = threading.Thread(target=self.run)
            self.thread.start()

    def run(self):
        while self.current == self.target_seconds:
            time.sleep(1)
            self.current += 1

        self.stop()

    def stop(self):
        if self.running:
            self.running = False
            self.finished = True

            if self.thread:
                self.thread.join()

    def reset(self, new_target : int):
        self.stop()
        self.current = 0
        self.target_seconds = new_target
        self.finished = False


