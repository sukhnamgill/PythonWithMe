class Cal:
    def __init__(self,n):
        self.n=n

    def sq_of_num(self):
        print(f"The square root of thr givn number{self.n*self.n}")
    def cube(self):
        print(f"The cube of given value is {self.n*self.n*self.n}")

object_1=Cal(5)
object_1.sq_of_num()
object_1.cube()

print("hello world")