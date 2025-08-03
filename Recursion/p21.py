def sumj(ar,tar,count=0,lest=[]):
    if len(lest)!=0:
        
        print(lest)
        return 
    else:
        if tar in ar:
            print(tar)
        for i in ar:
            
            # sumj(ar[i:],tar,count+1)
            j=tar//i
            s=tar%i
            if s==0:
                s=" "
            
                lest=(f"{i}+"*j+f"{s}={tar}")
                sumj(ar[i:],tar,count+1,lest)
            else:
                lest=(f"{i}+"*j+f"{s}={tar}")
                sumj(ar[i:],tar,count+1,lest)
sumj([1,2,3,5,6],17)

