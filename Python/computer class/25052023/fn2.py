def demo():
    name=input("Enter your name:")
    exp=int(input("Enter your experience:"))
    skill=input("Tellus your skill:")
    if exp>=4 and exp<6 and skill == 'Python' or skill =='Java':
        return "promoted as Team leader"
    elif exp>=10 and exp<14 and skill =="c++" or skill =="Java":
        return "Promoted as Project Manager"
    
desig= demo()
print(desig)    
    