list1=[11,22,33,333]
list2=["eleven","twenty two","thirty three","three hundred and thirty three"]
list3=list(zip(list1,list2))
print(list3)

list23=[89,60,80,69,38]
list33=[79,35,66,70,56]
for x,y in zip(list23,list33[::-1]) :
    print(x,y)