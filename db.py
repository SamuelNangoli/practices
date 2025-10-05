radius = 2
pie = 3.14
area_of_a_circle =pie*radius**2
print(area_of_a_circle)

class circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14*self.radius*self.radius
c1 = circle(2)
c2 = circle(1.6)

print(f'The Area of the Circle is',c1.area())
        

class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
    def withdraw(self, amount):
        self.balance -= amount

account = BankAccount(0)
account.deposit(70)
account.withdraw(160)
print(account.balance)

class Phone:
    def __init__(self, brand, storage):
        self.brand = brand
        self.storage = storage

    def call(self, number):
        print(f'calling {number} from {self.brand} !')

    def take_photo(self, camera):
        print(f'Taking photo {camera} from {self.brand}')

    def play_music(self, player):
        print(f'The song playing is {player} from {self.brand}')

#creating phone objects
my_phone = Phone('Samsung','128GB')
work_phone = Phone('iPhone', '256GB')

#call methods
my_phone.call('075-348-0959')

my_phone.take_photo('Nature')
my_phone.play_music('Daily Bundle By Elijah Kitaka')