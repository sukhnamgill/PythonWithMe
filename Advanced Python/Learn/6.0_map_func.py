print("Today iam map function")
def square(a):
    return ("the square of {} is {}".format(a,a*a))
list_of_numb=[13,23,8,45,18,77]
if __name__=='__main__':
    # print(list(map(square,list_of_numb)))
    # with lambda
    print(list(map(lambda x:x**3,list_of_numb)))