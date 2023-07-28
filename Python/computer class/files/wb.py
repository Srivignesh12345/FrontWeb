from pickle import *
name=open("Sri.txt","wb")
sdata=["kumar","raja"]
dump(sdata,name)
value=("Ganesh")
dump(value,name)
name.close()