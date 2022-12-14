import datetime


# return values vs raising exceptions
# what do we return if there is a problem?
# birth_year is negative, age is negative?
class NegativeYearError(Exception):
    pass

def get_age(birth_year: int):
    if birth_year < 0:
        raise Exception("negative year")
    if birth_year > datetime.datetime.utcnow().year:
        raise Exception("Birth year in futeur")
    return datetime.datetime.utcnow().year - birth_year

try:
    b_year = int(input("insert your year: "))
    age = get_age(b_year)
    print(f"you are {age} years old")

    print("inside try after get_age")
except ValueError:
    print("you did not insert a number")
except Exception as e:
    print (e)
finally:
    print("inside finally")
print("bye")

# exceptions you've already seen


# num = int(input("Insert your birth year: "))
# age = datetime.datetime.utcnow().year - num
# print(f"You are {age} years old")


# try:
#     num = int(input("Insert your birth year: "))
#     age = datetime.datetime.utcnow().year - num
#     print(f"You are {age} years old")
# except:
#     print("You did not insert a number")


# while True:
#     try:
#         num = int(input("Insert your birth year: "))
#         age = datetime.datetime.utcnow().year - num
#         print(f"You are {age} years old")
#         break
#     except:
#         print("You did not insert a number")


# we can differentiate between error types!

# def divide_dictionary_values(dictionary, keys):
#     try:
#         key1 = keys[0]
#         key2 = keys[1]
#         print(dictionary[key1] / dictionary[key2])
#     except KeyError as error:
#         print(f"Provided key does not exist in the dictionary: {error}")
#     except ZeroDivisionError as zde:
#         print(f"You tried to divide by zero")
#     except TypeError as val_err:
#         print("TypeError")
#     except Exception as unknown_exc:
#         print(f"Unknown error of type {type(unknown_exc)}: {unknown_exc}")


# Create your own Exception
# Exceptions are Objects that inherit from Exception

# class MyException(Exception):
#     pass

# exception propagates until someone catches it

# finally

# adding exceptions to Table System