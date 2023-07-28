try:
    a=int(input("Enter the number:"))
except ValueError as e:
    print("Value Error",e)
    raise KeyError("That is value")  
else:
    print("value is",a)  
finally:
    print("Hello the words")    