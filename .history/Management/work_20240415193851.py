import Management
import pickle
s=[]
f=open("password.dat","rb")
try:
    while True:
        s=pickle.load(f)
except EOFError:
    f.close()


print("Welcome to the Management System\nChoose your role: \n1. Admin\n2. Staff")
en = input("Enter your choice:")

if en.lower() in "01admin":

    if input("Enter pin:") == s[4]:

        while True: 
            print("Welcome to the Admin Panel")
            Management.admin() # type: ignore
            print("Thank you for using the Management System")
            print("Do you want to continue?\n1. Yes\n2. No")
            en = input("Enter your choice:").lower()
            if en in "01yes":
                continue

            elif en in "02no":
                break

            else:
                print("Sorry! No such option available")
                break


elif en.lower() in "02staff":
    
    if input("Enter pin:") == s[5]:
        print("Welcome to the Staff Panel")

        while True:
            Management.staff() # type: ignore
            print("Thank you for using the Management System")
            print("Do you want to continue?\n1. Yes\n2. No")
            en = input("Enter your choice:").lower()

            if en in "01yes":
                continue

            elif en in "02no":
                break

            else:
                print("Sorry! No such option available")
                break


else:
    print("Sorry! No such option available")
