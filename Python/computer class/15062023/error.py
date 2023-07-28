try:
    li=[10,45,78,54,34]
    print(li[8])
except IndexError as e:
    print("Index Error",e)
#KEY ERROR
try:
    dd={"Name":"sam","Name1":"pk"}
    print(dd['age'])
except KeyError as e:
    print("Key Error",e)
 #Attribute Error
try:
    class a:
        pass
    A=a()
    a.hello()
except AttributeError as e:
    print("Attribute Error",e)

