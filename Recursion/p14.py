def sum(no):
    if no<=10:
        return no
    else:
        rem=(no%10)
        # print(rem)
        return rem+sum(no//10)
    
print(sum(12345678919))

