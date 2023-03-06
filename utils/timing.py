import time
# this changes made by developer1
def timeit(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time() - start
        print(f"[INFO] total time to execute :: {end}" )
        return result
    return wrapper
