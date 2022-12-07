from datetime import date, datetime

class Ravkav:
    holder_id:str = ''
    holder_name:str = ''
    _balance:int = 0
    ride_dict_price =  {(0,40): {'name': 'short','price': 5.5},
                         (41,60):{'name': 'medium','price': 12},
                        (61,1000):{'name': 'long','price': 23}}
    ride_logs:list = [[datetime],[]] #1st list - dates, #2 list - type


    def __init__(self, holder_id: str, holder_name:str):
        self._holder_id = holder_id
        self._holder_name = holder_name
        self._balance = 0


    def topup(self, amnt:int):
        if amnt > 0:
            self._balance += amnt

    def ride_info(self, km_amnt:int) ->  tuple: #(ride_type, price)
        for range_ride in self.ride_dict_price:
            if range_ride[1] >= km_amnt >= range_ride[0]:
                ride_t = self.ride_dict_price[range_ride]['name']
                ride_p = self.ride_dict_price[range_ride]['price']
                print(ride_p, ride_t)
                return(ride_t, ride_p)

        # update balance according to ride
    def ride(self, km_amnt:int, date:str ) -> tuple:
        print('date = ',date, type(date))
        ride_a = self.ride_info(km_amnt)
        type_a = ride_a[0]
        price_a = ride_a[1]
        if price_a > self._balance:
            print('not enough cash balance')
            return (False,price_a,self._balance)
        self._balance -= price_a
        print(self._balance)
        #adding the type ride and date to lists:
        dates: datetime = datetime.strptime(date, "%d-%m-%Y")
        self.ride_logs[0].append(date)
        self.ride_logs[1].append(type_a)
        return (True, type_a ,price_a, self._balance)

    def count_ride_by_date(self,date:str) -> int:
        date_count = self.ride_logs[0].count(date)
        return date_count

    def count_ride_by_type(self,ride_type) ->int:
        type_count = self.ride_logs[1].count(ride_type)
        return type_count



    def get_current_balance(self):
        return self._balance

ride1 = Ravkav('234234234','noa')
ride1.topup(100)
print(ride1._balance)
ride1.ride_info(20)
ride1.ride(40,'11-10-2000')
print(ride1.count_ride_by_type('medium'))
print(ride1.count_ride_by_type('short'))
print(ride1.ride_logs)
print("by date: ", ride1.count_ride_by_date('11/10/2000'))
