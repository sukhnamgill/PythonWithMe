global_var="iam global variable"
def function_1():
    global global_var
    global_var=10
    print(global_var)

#simple


function_1()
print(global_var)