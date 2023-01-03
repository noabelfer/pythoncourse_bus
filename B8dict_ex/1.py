


def car(list_1, list_2) -> dict:
    my_dict = {}
    for i,v in enumerate(list_1):
        if v not in my_dict.keys():
            my_dict[v] = [list_2[i]]
        else:
            my_dict[v].append(list_2[i])
    return (my_dict)



list_1 = ["Mazda 3",     "Toyota Yaris",     "Volvo S40",    "Mazda 2",  "Toyota Yaris", "Volvo S40"]
list_2 = ["red",         "white",            "red",          "blue",     "black",        "red"]

c = car(list_1,list_2)
print(c)