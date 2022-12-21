# Implement a decorator @numeric_in_range that receives
# as parameters allowed range for numeric arguments
#     (2 numbers - min and max) and validates that all
#     the numerical arguments passed to the decorated
#     function are in the range specified. If the validation
#     fails, your decorator should raise an InvalidArgument exception.

class InvalidArgument(Exception):
    pass

def numeric_in_range(min_num, max_num):
    def inner(func):
        def decorated_func(*args,**kwargs):

            for b in args:
                if b not in range(min_num, max_num):
                    raise InvalidArgument
            for c in kwargs:
                if c not in range(min_num, max_num):
                    raise InvalidArgument
            return func(*args,**kwargs)
        return decorated_func
    return inner


@numeric_in_range(2,5)
def get_sum(num1,num2):
    return num1+num2

a = get_sum(3,3)
print(a)