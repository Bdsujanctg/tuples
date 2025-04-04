list1=[1,2,3,4,5,6,7,8,9]
list2=[2,1,3,4,7,6,9,8,5]
result= map(lambda x,y:x+y,list1,list2)
print(list(result))

list3=[12,32,56,76,86]
def sq(n):
    return n*n
result2= map(sq,list3)
print(list(result2))