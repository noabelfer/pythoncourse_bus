import datetime

class Ravkav:
    holder_id=0
    holder_name=""
    balance = 0
    logrides = [[],[]]  # list of touples (type,date)
    def __init__(self,holder_id,holder_name):
        self.holder_id = holder_id
        self.holder_name = holder_name
        
    ravkav_dic = {
        (0,40): {'name': 'short','price': 5.5},
        (41,60):{'name': 'medium','price': 12},  
        (61,1000):{'name': 'long','price': 23}} 
        
    def display(self):
        print (self.ravkav_dic)
 
    def topup(self,shekels):
        self.balance += shekels
    
    def getinfo(self,distance)->tuple:
        for rng  in self.ravkav_dic:
            if(distance >= rng[0] and distance <= rng[1]):
                return (self.ravkav_dic[rng]['name'], self.ravkav_dic[rng]['price'])
                
    def ride(km,ridedate)->tuple:
        info = getinfo(km)
        if(info[0] > self.balance):
            return (False,info[1],info[0],self.balance)
        self.logrides.append(info[0],info[0])
        self.logrides.append(info[1],ridedate)
        self.balance -= info[0]
        return (True,info[1],info[0],self.balance)
        
    def get_current_balance()->float:
        return self.balance
        
    def get_rides_by_date(self,ridedate:datetime)->int:
        return self.logrides[1].count(ridedate)

        
    def get_rides_by_type(self,type:str)->int:
        return self.logrides[0].count(type)
              
a = Ravkav(3,"moshe")
a.display()
a.topup(12)
a.display()
b = a.getinfo(12)
print(b)
print('short count: ',a.get_rides_by_type('short'))

