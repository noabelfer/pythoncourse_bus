# Implement a decorator @single_str_arg that validates that
# function received exactly one argument and that the argument
# type is string. If the validation fails, the decorator should
# raise an InvalidArgument exception.

class InvalidArgument(Exception):
    pass

def single_str_arg(func):
    def decorator(*args, **kwargs):
        if len(args) == 1 and len(kwargs) == 0:
            if type(args[0]) != str:
                raise InvalidArgument
            return func(*args, **kwargs)
        if len(args) != 1 or len(kwargs) != 0:
            raise InvalidArgument
        return func(*args, **kwargs)
    return decorator

@single_str_arg
def convert_to_upper(word):
    return word.upper()

a = convert_to_upper(78)
print(a)

