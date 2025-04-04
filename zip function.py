set1=(56,78,86)
set2=('b','n','m')
set3= list(zip(set1,set2))
print(set3, "\n")
#zip elements using loops
list1=[10,20,30,40]
list2=[10000,20000,30000,40000]
for x,y in zip(list1,list2[::-1]):
    print(x,y)

#zip in dictionary
stocks=['mango','apple','strawberry']
prices=[1000,2000,30000]
new_dict={stocks: prices for stocks,prices in zip(stocks,prices)}
print("\n",new_dict)