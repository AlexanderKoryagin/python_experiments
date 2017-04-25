#!/usr/bin/env python

from contextlib import contextmanager
from time import sleep, time


class TimerClass(object):

    def __enter__(self):
        print "\n-- Timer class --"
        self.start = time()
        print "Starting at {0}.".format(self.start)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end = time()
        total_time = self.end - self.start
        print "Ending at {0}.\nTotal time: {1}".format(self.end, total_time)


@contextmanager
def timer_func():
    print "\n-- Timer function --"
    start_t = time()
    print "Starting at {0}.".format(start_t)
    try:
        yield
    finally:
        end_t = time()
        total_time = end_t - start_t
        print "Ending at {0}.\nTotal time: {1}".format(end_t, total_time)

with TimerClass():
    sleep(2)
    # assert False

with timer_func():
    sleep(2)
    # assert False
