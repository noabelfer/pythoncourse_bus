
def c(list_1):
    my_dict = {}
    for i,v in enumerate(list_1):
        my_dict[i+1] =v
    return my_dict


list_1 = ["sun", "water", "air", "water", "water", "apple", "air"]

car = c(list_1)
print(car)