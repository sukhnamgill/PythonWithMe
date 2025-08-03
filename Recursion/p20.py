# subset sum problem
def sbsm(arr,target,inc=0,exc=0,i=0,nam=""):
    if i>=len(arr):
        # print("index out of range")
        if target== inc or exc:
            print("target matvhed !",nam,"=",target)
            
            return 
        
    else:
        
        sbsm(arr,target,inc+arr[i],exc,i+1,nam+"+"+str(arr[i]))
        sbsm(arr,target,inc,exc,i+1,nam)
        
        # print(j,a)
        # sbsm(arr,target,j,a,i+1)
        # return j or a
        


sbsm([1,2,6],7)
