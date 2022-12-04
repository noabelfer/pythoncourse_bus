def merge(num1:list, num2: list):
    num1.sort(reverse = True)
#    print(enumerate(num1[::-1]))
    for i, n in enumerate(num1[::-1]):
#        print(i,n)
        if n == 0:
            num1.remove(n)
    for i in num2:
        num1.append(i)
    sorted(num1)
    return(sorted(num1))

def merge2(num1:list, num2: list):
    out = []
    while(len(num1) > 0 and len(num2) > 0):
        if(num1[0] == 0):
            while(len(num2) > 0):
                out.append(num2.pop(0))
            return out
        if(num1[0] < num2[0]):
            out.append(num1.pop(0))
        else:
            out.append(num2.pop(0))
    while(len(num1) > 0):
        if(num1[0] == 0):
            return out
        out.append(num1.pop(0))
    while(len(num2) > 0):
        out.append(num2.pop(0))
    return out
            
    
        
print('Smple: ',merge(  [1,3,5,7,9,0,0,0],[2,4,6]))
print('Smple2:',merge2([1,3,5,7,9,0,0,0],[2,4,6]))

print('second  empty: ',merge([1,3,5,7,9,0,0],[]))
print('second2 empty: ',merge2([1,3,5,7,9,0,0],[]))

print('third  empty: ',merge([],[1,2,3]))
print('third2 empty: ',merge2([],[1,2,3]))

print('both  empty: ',merge([],[]))
print('both2 empty: ',merge2([],[]))

print('first negative:  ',merge([-9,-7,-5,-3,0,0,0],[2,4,6]))
print('first negative2: ',merge2([-9,-7,-5,-3,0,0,0],[2,4,6]))