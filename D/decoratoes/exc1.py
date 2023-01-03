import time
#time.perf_counter()
import decorators

def performance_log (func):

    def decorator(*args, **kwargs):
        start_t = time.perf_counter()
        result = func(*args, **kwargs)
        end_t = time.perf_counter()
        print(f"running time is:{end_t - start_t}")
        return result
    return decorator


@performance_log
def long_running_func(num, iters):
    val = 1
    for i in range(iters):
        val *= num
    return val

long_running_func(14,18)