print("print subsequence of string")
def sub(name,new=""):
    if name=="":
        print(new)
        return 
    else:

        rest=name[1:]
        first=name[0]
        sub(rest,new+first)
        sub(rest,new)
        

sub("ABCD")