from datetime import datetime
import enum

        
class Rideoption(enum.Enum):
    short = 'short'
    medium = 'medium'
    long = 'long'

    
class Ravkav:

    class LOGR_IND(enum.Enum):
        TYPE = 0
        DATE = 1
        
    def __init__(self,holder_id,holder_name):
        self.holder_id = holder_id
        self.holder_name = holder_name
        self.balance = 0
        self.logrides = [[],[]]  # list of touples (type,date)
        
    ravkav_dic = {
        (0,40): {'name': Rideoption.short,'price': 5.5},
        (41,60):{'name': Rideoption.medium,'price': 12},  
        (61,1000):{'name': Rideoption.long,'price': 23}} 
        
    def display(self):
        print (self.ravkav_dic)
 
    def topup(self,shekels):
        self.balance += shekels
    
    def __getinfo(self,distance)->tuple:
        for rng  in self.ravkav_dic:
            if(distance >= rng[0] and distance <= rng[1]):
                return (self.ravkav_dic[rng]['name'], self.ravkav_dic[rng]['price'])
                
    def ride(self,km:int,ridedate:str)->tuple:
        d = datetime.strptime(ridedate, "%Y-%m-%d")
        info = self.__getinfo(km)
        if(info[1] > self.balance):
            return (False,info[1],info[0],self.balance)
        self.logrides[self.LOGR_IND.TYPE.value].append(info[0])
        self.logrides[self.LOGR_IND.DATE.value].append(d)
        self.balance -= info[1]
        return (True,info[1],info[0],self.balance)
        
    def get_current_balance()->float:
        return self.balance
        
    def get_rides_by_date(self,ridedate:str)->int:
        d = datetime.strptime(ridedate, "%Y-%m-%d")
        return self.logrides[1].count(d)

        
    def get_rides_by_type(self,type:Rideoption)->int:
        return self.logrides[0].count(type)
              
a = Ravkav(3,"moshe")
a.display()
a.topup(300)
a.display()
a.ride(45,'2022-09-24')
a.ride(46,'2022-09-24')
a.ride(5,'2022-09-24')
a.ride(26,'2022-09-24')

print('short count: ',a.get_rides_by_type(Rideoption.short))
print('medium count: ',a.get_rides_by_type(Rideoption.medium))
print('long count: ',a.get_rides_by_type(Rideoption.long))
print('date count: ',a.get_rides_by_date('2022-09-24'))

