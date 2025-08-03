# print("remove duplicate from string ")
def rm_db(name,new="",i=0):
    if i==len(name):
        return new
    else:
        if not name[i] in new:
            new=new+name[i]
        else:
            pass
        return rm_db(name,new,i+1)
    
print(rm_db("google"))