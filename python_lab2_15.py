import random
small=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y'
'z']

capital=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H','I', 'J', 'K', 'M', 'N', 'O', 'P', 'Q','R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
'Z']
 
number=['0','1','2','3','4','5','6','7','8','9']
symbl=['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>','*', '(', ')', '<']
password=''

pswrd=random.choices(capital,k=3)+random.choices(number,k=3)+random.choices(symbl,k=3)+random.choices(small,k=3)
for x in pswrd:
	password+=x

print(password)