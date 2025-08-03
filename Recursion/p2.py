# print(factorial of n)
def fact(n):
    if n==0:
        return 1
    else:
        return n* fact(n-1)
    
j=fact(1)
print(j)