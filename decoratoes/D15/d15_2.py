# Implement a decorator @numeric_params that validates that
# function received only numeric arguments (int, float).
# If the validation fails, the decorator should raise
# an InvalidArgument exception.

class InvalidArgument(Exception):
    pass

def numeric_params(func):
    def decorator(*args,**kwargs):
        for a in args:
            if type(a) != int and float:
                raise InvalidArgument
        for b in kwargs:
            if type(b) != int and float:
                raise InvalidArgument
        return func(*args, **kwargs)
    return decorator


@numeric_params
def next_num(num):
    return num+1

a = next_num(12)
print(a)