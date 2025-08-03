# print(Find first and last occurrence of an element)
name="google"
def first_last(name,n,cha=[],i=0):
    if len(cha)==2:
       return cha
    elif i==len(name):
        return cha
    
    else:
        if len(cha)<1:
            if n==name[i]:
                cha.append(f"The  first index of {n}-> {i}")
                
        elif(len(cha)>=1):
          
          if n==name[-i]:
                # print("hello",n,i)
                cha.append(f"The last index of {n}-> {-i+len(name)}")
        
        return first_last(name,n,cha,i+1)
        

print(first_last("SOOggSGjdjcnS","S"))