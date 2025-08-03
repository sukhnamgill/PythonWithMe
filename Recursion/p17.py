print("printing palindrome")
def pdrome(name,pa=""):
    if name=="":
        print(pa)
        return
    else:
        for i in range(len(name)):
            j=name[i]
            # print(j)
            new=name[:i]+name[i+1:]
            # print("new is ",new)
            pdrome(new,pa+j)
            

pdrome("ABC")

