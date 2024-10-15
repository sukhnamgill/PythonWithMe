class Sample:
    class_var ="Iam class variable"
    @property
    def name(self):
        print(f" Iam property function{self.fname}")

    @name.setter
    def names(self,value):
        if(value=="sukhnam"):
            print("hello")
        else:
            print("not hello")


obj =Sample()
obj.names="sukhnamd"
# obj.name()
# print(obj.fname)
# obj.name()