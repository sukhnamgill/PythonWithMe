print("how to count dagit in number")
def count(digit,i=1):
    if digit<10:
        return i
    else:
        # print(i)
        return count(digit/10,i+1)
        
print(count(134335))