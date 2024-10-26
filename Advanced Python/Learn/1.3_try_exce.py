print("iam running..")
try:
    sn=input("Enter integer to duvide vlaue with 5")
    sn=int(sn)
    print(sn/5)
except ValueError as err:
    print("value eror")
except ZeroDivisionError as er:
    print("divide eror")