try:
    set=int(input("Enter the password:"))
    con=int(input("Confirm the password:"))
    if set!=con:
        raise inputerror
    
    else:
        print("Password was set successfully")
except inputerror as ss:
    print(ss) 
finally:
    print("Successfully login")       