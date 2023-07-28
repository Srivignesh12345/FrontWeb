from pickle import *
name=open("Sri.txt","rb")
while True:
    try:
        sdata=load(name)
        print(sdata)
    except EOFError as e:
        break
name.close()    