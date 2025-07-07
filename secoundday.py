# practice oop 
# class circle:
#     def __init__(self, radius):
#         self.radius=radius
#     def area(self):
#         return 3.14* self.radius **2
#     def perimeter(self):
#          return 2* 3.14* self.radius **2
     
     
# c = circle(21)
# print(c.area())
# print(c.perimeter())
#questiion2
class emp:
    def __init__(self, roll,salary,dept):
        self.roll=roll
        self.salary=salary
        self.dept=dept
    def showdetail(self):
        print( "hi you r" ,self.roll)
        print( "hi you r" ,self.dept) 
        print( "hi you r" ,self.salary)
        
        

class engineer(emp):
    def __init__(self, age, name):
        self.name=name
        self.age=age
        super().__init__("software enginner", 13333333,"computersciense")
eng1 =engineer("sakinakhan", 20)
eng1.showdetail()
#question3
class order:
    def __init__(self, item , price):
        self.item=item
        self.price=price
    def __gt__(self,ord2):
         return self.price > ord2.price

or1=order("cookies" ,17000)
or2=order("cookies" ,15000)

print(or2>or1)