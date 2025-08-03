# ha(ve to print balanced parentheseis
# ()()()
def bp(n,left=0,right=0,li=""):
    if n*2==len(li):
        if right==left:
            print(li)
            return
    else:
        if right>left:
            # print("leftrun")
            bp(n,left+1,right,li+"(")
        if left>right:
            # print("rightrun")
            bp(n,left,right+1,li+")")
        
        bp(n,left+1,right,li+"(")
            
        # bp(n,left,right+1,li+")")

bp(2)