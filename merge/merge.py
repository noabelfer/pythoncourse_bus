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
# for example
#  num1 [1,3,5,7,9,0,0,0]  
#  num2 [2,4,6]      
def merge3(num1:list, num2: list):
    if(num1 == []):
        for cu in num2:
            num1.append(cu)
        return num1 
    for item_num2 in num2:
       
        #find the location of item_num2  in num1
        for i ,v in enumerate(num1):
            if(item_num2 < v) or (v==0):
                # item_num2 = 2
                # i = 1
                # v = 3
                #The next loop will shit num1
                #befor the loop num1 [1,3,5,7,9,0,0,0]
                for j in range(len(num1)-1,i,-1):                   
                    num1[j] = num1[j-1]
                #after the loop num1 [1,3,3,5,7,9,0,0]
                #put item_num2 in num1
                num1[i] = item_num2
                #now num1 [1,2,3,5,7,9,0,0]
                break
    return num1
                
        
#print('Smple: ',merge(  [1,3,5,7,9,0,0,0],[2,4,6]))
print('Smple2:',merge2([1,3,5,7,9,0,0,0],[2,4,6]))
print('Smple3:',merge3([1,3,5,7,9,0,0,0],[2,4,6]))

print('second2 empty: ',merge2([1,3,5,7,9,0,0],[]))
print('second3 empty: ',merge3([1,3,5,7,9,0,0],[]))

#print('third  empty: ',merge([],[1,2,3]))
print('third2 empty: ',merge2([],[1,2,3]))
print('third3 empty: ',merge3([],[1,2,3]))

#print('both  empty: ',merge([],[]))
#print('both2 empty: ',merge2([],[]))

#print('first negative:  ',merge([-9,-7,-5,-3,0,0,0],[2,4,6]))
print('first negative2: ',merge2([-9,-7,-5,-3,0,0,0],[2,4,6]))
print('first negative3: ',merge3([-9,-7,-5,-3,0,0,0],[2,4,6]))