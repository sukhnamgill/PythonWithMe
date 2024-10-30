print("filter function is here")
lis=[77,23,54,54,5,46,6,23,4,787,74,58,7]
def even_odd(n):
    n=int(n)
    if n%2==1:
        return True
    
    else:
        return False
# fun=even_odd("9814237194")
# lis2=(list(filter(even_odd,lis)))
# print(lis2)
# print(True*False)
# print(True+False)
# print(True*True)
# print(False*False)
lam=lambda x:x%2==1
result=lam(45)
print(result)

print(list(filter(lam,lis)))