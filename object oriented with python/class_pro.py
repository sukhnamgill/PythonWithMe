class New:
    def __init__(self,n):
        self.new =n
    
    @property
    def show(self):
        print('The output is ',self.new*5)
    @show.setter
    def show_ch(self,value):
        self.new=value*10
        

    

obj=New(5)
obj.show
obj.show_ch=50
obj.show
# obj.area()


# print(obj.n) it ouput 5