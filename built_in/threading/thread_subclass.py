import threading
import time


class MyThread(threading.Thread):
    def __init__(self, name=None, args=(), kwargs=None, *, daemon=None):
        super().__init__(group=None, target=self.worker, name=name, args=args, kwargs=kwargs, daemon=daemon)
        self.start_time = time.perf_counter()

    # def run(self):
    #     try:
    #         if self._target:
    #             self._target(*self._args, **self._kwargs)
    #     finally:
    #         # Avoid a refcycle if the thread is running a function with
    #         # an argument that has a member that points to the thread.
    #         del self._target, self._args, self._kwargs

    def worker(self):
        for iteration in range(10):
            time.sleep(1)
            print(f"worker thread is working for {round(time.perf_counter() - self.start_time)} sec.")
        print(f"worker thread is done after {round(time.perf_counter() - self.start_time)} sec.")


mt = MyThread()
mt.start()

mt.join(3.4)

print("done")