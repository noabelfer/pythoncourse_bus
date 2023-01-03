
def c(list_1):
    my_dict = {}
    for f in list_1:
        my_dict[f] =list_1.count(f)
    return my_dict


list_1 = ["sun", "water", "air", "water", "water", "apple", "air"]

car = c(list_1)
print(car)