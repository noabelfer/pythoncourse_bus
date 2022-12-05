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
            
def merge3(num1:list, num2: list):
    if(num1 == []):
        for cu in num2:
            num1.append(cu)
        return num1 
    while(len(num2) > 0):
        #pull the first item from num2
        ch = num2.pop(0)
        #find the location of the pulled item in list1
        for i ,v in enumerate(num1):
            if(ch < v) or (v==0):
                #here we found the the location of ch in num1 is i
                #So we move all items in num1[i:len()-1] to [i+1:len()-1] .
                #the item located in num1[len()-1] is discarded. 
                #num1[i] is replaced by ch 
                #For example: num1 [1,3,5,7,9,0,0,0]
                #             num2 [2,4,6]
                # we compare 2 to num1[] and find out that 2 should be locate between 1 and 3 in num1
                # Next step is to move num1[2:8] to num1[3,8] the last 0 is thrown out .
                # Now num1[2] is updated by ch and the result for i=1 is [1,2,3,5,7,9,0,0]
                # The same is done for all iitems of num2 
                for j in range(len(num1)-1,i,-1):                   
                    num1[j] = num1[j-1]
                #put ch in num1
                num1[i] = ch
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