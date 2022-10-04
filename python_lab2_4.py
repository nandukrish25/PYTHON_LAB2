a=tuple(input('enter a string:'))
for x in a:
    b=a.count(x)
    if b>1:
        print(x,b)
