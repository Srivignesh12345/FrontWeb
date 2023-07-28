from app import *
print('welcome!')

while True :
    print('1.New policy\n2.Update policy\n3.View all existing polcies\n4.Read policy details\n5.Delete policy\n6.Exit')
    operation=int(input("Enter the number to perform respective process "))
    if operation==1:
        create()
    elif operation==2:
        policynumber=int(input("Enter the policy number to update"))
        update(policynumber)
    elif operation==4:
        policynumber=int(input("Enter the policy number to update"))
        read(policynumber)
    elif operation==3:
        view()
    elif operation==5:
        policynumber=input('Enter thr policy number to delete')
        delete(policynumber)
    else:
        print("Invalid operation")
    
        break