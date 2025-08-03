# print("is array sorted or not")
def is_sorted(i=0,a=[],):
    # if i>=len(a):
    #     print("linit exceed")
    if i==len(a):
        return True
    else:
        
        if a[i-1]<=a[i]:
            print(f" a[{i-1}]{a[i-1]} is smaller than a[{i}]{a[i]}")
            if is_sorted(i+1,a):
                return True
            return False
            
        else:
            return False


arr=[5,10,20,25,30,35,40]
print(is_sorted(1,arr))