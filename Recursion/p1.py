# print 1 to n and n  to one/
def printer(n,start):
    if start==n+1:
        return 1
    else:
        print(start)
        print(printer(n,start+1))
        print(start)

printer(10,1)