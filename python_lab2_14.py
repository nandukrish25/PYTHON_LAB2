a={1,2,5,6,8,0}
b=int(input('enter a number between 0-9:'))
if b in a:
	a.remove(b)
	print('the item has deleted',a)

else:
  print('item is not present in the set')	