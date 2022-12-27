import threading

def a_lot_of_calc(num:int):
    print(f"started a_lot_of_calc with {num}")
    s = 0
    for i in range(500):
        s+= num**i
    print (s)

if __name__ == '__main__':
    print("hello")
    # t = threading.Thread()
    num = int(input("insert num: "))
    t = threading.Thread(target=a_lot_of_calc,args=(num, ))
    t.start()
    print(a_lot_of_calc(num))


    num1 = int(input("insert num: "))
    t1 = threading.Thread(target=a_lot_of_calc,args=(num, ))
    t1.start()
    t.join()
    t1.join()
    print("bye")