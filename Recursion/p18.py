print("subsequene of set")

ed=[1,2,3]

def subset(old,new=[],idx=0):
    if idx==len(old):
        print(new)
        return
    else:
        subset(old,new+[old[idx]],idx+1),subset(old,new,idx+1)
        

subset(ed)