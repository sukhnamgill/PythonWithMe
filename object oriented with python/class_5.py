# class Animal:
#     def __init__(self,name):
#         print("iam called",name)
#     def fun2(self):
#         for i in range(10):
#             print(i)

# obj=Animal("Rohan")
# obj.fun2()

class Ac:
  
    def __init__(self):
        print("iam called because iam instructer")
        self.easy()
        
    def easy(self):
        self.a=10
        ab=20
    def printer(self):
        print(self.a)
        # print(ab)
ob=Ac()
ob.printer()
ob.a=20
# print(ob.a)
ob.printer()
