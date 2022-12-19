# Use lambda and filter/map/sort. Given a list of strings,
#            filter out those containing less than 2 "a" chars.
# For example, for ["apple", "ananas", "banana", "pear"], your code should return ["ananas", "banana"]


# for word in list_1:
#     for letter in word:
#         if letter =='a':



list_1 = ["apple", "ananas", "banana", "pear"]
new_list = filter(lambda x: (x.count('a') >1 ), list_1)
print(list(new_list))
