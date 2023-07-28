a=('sam','ganesh','anu','priya')
b=list(a)
b.append("sathish")
a=tuple(b)
print(a)
#adding tuple in tuple
a=('sam','sathish','anu','priya')
b=("ganesh",)
a+=b
print(a)