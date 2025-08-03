print("power for example 2's 3")
def power(dagit,powera,i=1):
    if i==powera:
        
        return dagit
    else:
        # print(i)
        return dagit*(power(dagit,powera,i+1))
    
print(power(2,6))