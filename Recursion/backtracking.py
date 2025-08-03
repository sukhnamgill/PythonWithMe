print("this code for ,how to backtracking in recursion")

def sample(n,index=0):
    if index==n:
        return 
    else:
        print("steping forwaed",index)
        sample(n,index+1)
        print("backktracking",index)
        return 
sample(5)