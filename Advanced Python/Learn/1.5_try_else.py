print("lesson for try and else")
try:
    inpt=input("Enter The Value")
    int_inpt=int(inpt)
    print(int_inpt+5)
except Exception as epp:
    print("This is value Error..String is not allowed")
else:
    print("the programme run sucessfully")