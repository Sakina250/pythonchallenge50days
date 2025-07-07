#pratice  for oop

# class account:
#     def __init__(self, bal ,acc):
        
#         self. bal = bal
#         self. acc =acc
#     def credit(self,amount):
#         self.bal =+amount
#         print( "your credit is " ,amount)
#         print("your balance is " ,self.bal)
#     def debit(self,amount):
#         self.bal =-amount
#         print( "your debit is " ,amount)  
#         print("your balance is " ,self.bal)
#     def getbal(self ):
#         return self.bal

        
# acc1 = account(100000,12345)
# print(acc1.acc)
# print (acc1.bal)
# acc1.credit(100999)
# acc1.debit(66666)
# acc1.getbal()
#=====================================================================
# practice for oop
# class student:
#      def __init__(self , name , marks):
#         self.name= name
#         self.marks=marks
#      def getavg(self):
#          sum=0
#          for i in self.marks:
#             sum+=i
#          print( " my average is" ,sum/3)
            
# std=student("ali", [99,90,89])
# std.getavg()
# static method
# class student:
#    @staticmethod
#    def hello():
#      print("hello")
# std=student()
# std.hello()