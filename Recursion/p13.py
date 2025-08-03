# print("replace pi with 3.14")

def replac(name,i=0,new=" "):
    if i==len(name):
        return new
    else:
        
        if name[i-2]=="P" and name[i-1]=="I" and name[i]=="E":
            new=new +" (3.14)"
            
        else:
            if(name[i]) == "P" or name[i]=="I":
                # print("value is matched")
                pass
            else:
                new=new+name[i]
        return replac(name,i+1,new)
print(replac("the value of pie is PIE and its value is PIE "))

