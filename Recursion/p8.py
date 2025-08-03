# print("level two is here ...reverse a string using recursion")
def reverse(name,reve="",i=1):
    if i>len(name):
        return reve
    else:        
        return reverse(name,reve+name[-i],i+1)
# print(reverse("nitin"))    
        
def is_palendrome(name,i=1):
    if i>len(name):
        return True
    else:
        if name[i-1]==name[-i]:
            return is_palendrome(name,i+1)
            # return True
        else:
            return False

print(is_palendrome("nitin"))



