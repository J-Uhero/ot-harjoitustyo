from time import time

class Clock:
    def __init__(self):
        self._start_time = 0.0
        self._end_time = 0.0
        self._stopped = True

    def start(self):
        if self._stopped:
            self._start_time = time()
            self._stopped = False
    
    def stop(self):
        self._end_time = time()
        self._stopped = True

    def give_exact_time(self):
        if self._stopped:
            return self._end_time - self._start_time
        return time() - self._start_time
    
    def give_time_in_seconds(self):
        time = self.give_exact_time()
        return "{:.0f}".format(time)

    def reset(self):
        self._start_time = 0.0
        self._end_time = 0.0
        self._stopped = True
