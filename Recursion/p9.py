def find_max(arr,grater=0,i=1):
    if i==len(arr):
        return grater
    else:
        if arr[i-1]>=grater:
            grater=arr[i-1]
        else:
            pass
        
        return find_max(arr,grater,i+1)
ary=[600,700,45,34]
print(find_max(ary))