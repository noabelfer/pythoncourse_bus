


def car(list_1, list_2) -> dict:
    my_dict = dict(zip(list_1,list_2))
    return (my_dict)


list_1 = ["Mazda 3",     "Toyota Yaris",     "Volvo S40",    "Mazda 2",  "Toyota Yaris", "Volvo S40"]
list_2 = ["red",         "white",            "red",          "blue",     "black",        "red"]

c = car(list_1,list_2)
print(c)