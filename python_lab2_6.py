color_dict = {'red':'#FF0000',
              'green':'#008000',
              'black':'#000000',
              'white':'#FFFFFF'}

a=[] 
b={}             

for x in color_dict:
      a.append(x)
      

a.sort()


for x in a:
     b=x:color_dict[x]


print(b)    

