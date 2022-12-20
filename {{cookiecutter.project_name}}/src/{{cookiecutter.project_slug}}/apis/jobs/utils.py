import functools
from multiprocessing import Process


def spawn_process_for_func(func):

    @functools.wraps(func)
    def wrapped(*args, **kwargs):
        process = Process(target=func, args=args, kwargs=kwargs)
        process.start()
        process.join()
        process.close()

    return wrapped
