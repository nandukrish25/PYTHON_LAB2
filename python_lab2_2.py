a=input('enter a string:')
b=[]
for x in a:
	b.append(x) 

c=tuple(b)
for x in c:
   print(x,c.count(x))	