from myapp import myapp
from pickle import*

policy=[]

#file=open('insurance policy.doc','wb')
#file.close()

def readfile():
    try:
        mypolicy=open('insurance policy.doc','rb')
        return load(mypolicy)
    except FileNotFoundError as FNF:
        print("Data file is not exists")
        return []
    except EOFError as e:
        return [] 

def writefile(what):
    mypolicy=open('insurance policy.doc','wb')
    dump(what,mypolicy)
    mypolicy.close()
    print('work done!')

def create():
    number=int(input('enter the policy number '))
    nominee=input('enter the name of the nominee ')
    period=int(input("enter the term of ur policy(in yrs)"))
    members=int(input('how many members u want to include in this policy? '))
    sumassure=int(input('choose the sumassure u want? 1)1000000, 2)500000 ,3)200000' ))
    if sumassure==1: 
        print('u have to pay Rs. 10000/- per month')
        sumassure=1000000
    elif sumassure==2: 
        print('u have to pay Rs. 5000/- per month')
        sumassure=500000
    elif sumassure==3: 
        print('u have to pay Rs. 1000/- per month')
        sumassure=200000
    else: print('pls choose from the above sumassure')

    if sumassure==1000000 or sumassure==500000 or sumassure==200000:
        Policy=myapp(number,nominee,period,members,sumassure)

        mypolicy=readfile()

        mypolicy.append(Policy)
        writefile(mypolicy)
    else: print('policy has not reated due to invlid sumassure')

def view():
    mypolicy=readfile()
    for x in mypolicy:
        print(x)

def update(policynumber):
    mypolicy=readfile()
    #policynumber=int(input('enter ur policy no.'))
    for i in range(len(mypolicy)):
        if mypolicy[i].number==policynumber:
            question=input('what would u like to update in ur existing policy')
            if question=='nominee':
                change=input('enter the name of new nominee')
                mypolicy[i].nominee=change
                writefile(mypolicy) 
                print('nominee name has been changed')
                return
            elif question=='members':
                changes=int(input('enter how many members u need to change'))
                mypolicy[i].members=changes
                writefile(mypolicy) 
                print ('ur policy has been updated')
                return
            elif question=='sumassure':
                sumassure=int(input('choose the sumassure u want? 1)1000000, 2)500000 ,3)200000' ))
                if sumassure==1: 
                    print('u have to pay Rs. 10000/- per month')
                    sumassure=1000000
                elif sumassure==2: 
                    print('u have to pay Rs. 5000/- per month')
                    sumassure=500000
                elif sumassure==3: 
                    print('u have to pay Rs. 1000/- per month')
                    sumassure=200000
                else: print('pls choose from the above sumassure')

                if sumassure==1000000 or sumassure==500000 or sumassure==200000:
                    print('ur summasure has been changed')
                writefile(mypolicy) 
                return
            else: print("Invalid option")
    else: print("policy number doesn't exist")

def read(policynumber):
    mypolicy=readfile()
    #policynumber=int(input('enter ur policy no.'))
    for i in range(len(mypolicy)):
        if mypolicy[i].number==policynumber:
            print(mypolicy[i])
            return

    else: print("policy number doesn't exist")

def delete(policynumber):
    #policynumber=int(input('enter the policy number'))
    mypolicy=readfile()
    position=-1
    for s in range(len(mypolicy)):
        if mypolicy[s].number==policynumber:
            position=s
            break
    if position!=-1:
        mypolicy.pop(position)
        writefile(mypolicy)
    else:
        print('policy number not found')

#create()
#view()
#update()
#read()
#delete()