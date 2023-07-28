mark1=int(input("Enter the mark of first mark:"))
mark2=int(input("Enter the mark of second mark:"))
avg=mark1+mark2/2
if avg >=80:
    print("Grade A")
elif avg>=70 and avg<60:
    print("Grade B")
elif avg>=60 and avg<50:
    print("Grade C")
elif avg>=50 and avg<40:
    print("Grade D")
else:
    print("Grade E")
