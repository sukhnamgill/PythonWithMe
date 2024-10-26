print("iam running...")

while(True):
    try:
        str_a=input("Enter an integer")
        int_a=int(str_a)
        print("The integer value is :",int_a)
        q_input=input("Enter Q to Quit the programme other wise Pres Enter")
        if (q_input=='Q'):
            break
    except Exception as err:
        print("There is value eror")
        
print("thanks for using this programme")


