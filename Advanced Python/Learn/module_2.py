sukhnam_age=19
def greet(name,am_pm):

    if am_pm=='am':
        print(f"hello {name},Good morning")
    elif(am_pm=='pm'):
        print(f"Hello {name },Good Evening sir")
    else:
        print("choose am or pm correctly !")
if __name__=='__main__':
    print("printing name:::",__name__)

    greet("sukhnam",'am')
    print("Iam from module")