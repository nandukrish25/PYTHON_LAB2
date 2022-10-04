a=(12,13,14,15,16)
b=[]
i=len(a)-1

while i>=0:
	b.append(a[i])
	i-=1

print(tuple(b))