#Write generator batches(n, my_list) that returns batches of length n of the given list



def batches(n, my_list):
    for i in range(0, len(my_list), n):
        yield my_list[i:i+n]

for batch in batches(3,[1,2,3,4,5,6,7,8,9]):
    print(batch)









