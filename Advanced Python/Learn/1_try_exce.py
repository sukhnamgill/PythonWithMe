#here is try and execept
int_a=input("enter an value value should be integer")
# print(int_a)

try:
    dcasting=int(int_a)
    print(dcasting+"iam  string")
except Exception as e:
    print("Int and string can-not cancatenate with: ( + )sign...eror from sukhnam ")
