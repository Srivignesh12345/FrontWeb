a=int(input("Enter the mark:"))
if a>=90:
    print("Distinction")
elif a>=70 and a<90:
    print("first class")
elif a>=50 and a<70:
    print("Second class")
elif a>=30 and a<50:
    print("Third class")
else:
    print("You have got failed")

s=20
print(s<52 or s>10)