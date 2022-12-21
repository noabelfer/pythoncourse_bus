# Implement a decorator @valid_param_types that receives as
# parameter allowed argument types and validates whether the
# argument passed to a function answers this requirement.
# If the validation fails, the decorator should raise an InvalidArgument exception.

class InvalidArgument(Exception):
    pass

def valid_param(allowed_types:list):
    def inner(func):
        def decorated_func(*args,**kwargs):

            for a in args:
                if type(a) not in allowed_types:
                    raise InvalidArgument
            for v in kwargs:
                if type(v) not in allowed_types:
                    raise InvalidArgument
            return func(*args, **kwargs)

        return decorated_func
    return inner


@valid_param([int,float])
def get_sum(num1,num2):
    return num1+num2


a = get_sum(2,3)
print(a)