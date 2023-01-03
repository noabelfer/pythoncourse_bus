#Implement generator fib that yields infinite Fibonacci sequence

def gen_fibonacci():
    n1 = 0
    n2 = 1
    while True:
        yield n1
        n1, n2 = n2, n1 + n2

for i in gen_fibonacci():
    print(i)





