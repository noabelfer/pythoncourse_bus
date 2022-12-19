
def stocks(list_1, list_2) ->dict:
    my_dict_1 = {}
    my_dict_2 = {}
    for i,date in enumerate(list_1):
        if date in my_dict_1.keys():
            my_dict_1[date] = my_dict_1[date],list_2[i]
        else:
            my_dict_1[date] = list_2[i]


    for i,s in enumerate(list_2):
        if s in my_dict_2.keys():
            my_dict_2[s] = my_dict_2[s],list_1[i]
        else:
            my_dict_2[s] = list_1[i]

    print(my_dict_1)
    print(my_dict_2)





list_1 = ["11-05-22",    "12-05-22", "13-05-22", "12-05-22", "11-05-22", "11-05-22"]
list_2 = ["TSLA",        "TSLA",     "AAPL",     "MSFT",     "AAPL",     "IBM"]

s= stocks(list_1,list_2)
print(s)