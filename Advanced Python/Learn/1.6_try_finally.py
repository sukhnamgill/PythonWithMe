print("importance of using Finally")
try:
    str_i=input("enter an number")
    int_i=int(str_i)
    print(int_i+20)
except Exception as er:
    print("value Error")
    exit()
finally:
    print("iam runnig regardless of error,or in condition of ")
print("iam out of finnally block")