# print(sum of n first natural number)
def sum_no(n,i=0):
    if i==n:
        return n
    else:
        return i+sum_no(n,i+1)

print(sum_no(10))