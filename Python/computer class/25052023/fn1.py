def register(name,location,prefix="Mr/Miss/Mrs"):
    if location =="Tiruchengode":
        print(prefix,name,"has approved in",location)
    elif location == "Chennai":
        print(prefix,name,"Has gone under waiting state since its",location)
    else:
        print("Business not approved")

register("Srivignesh business tech corp","Tiruchengode")
register("Srihari tesla","Chennai","Mr.")
register("Has been completed.....","sssss")
