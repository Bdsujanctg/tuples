dictionary={'Codingal': 2,'coding':2 ,'python':3,'days':2}
print("The original dictionary:",dictionary)
k=3
result=0
for i in dictionary:
    if dictionary[i]==k:
        result+=1
print("The frequency of k is:",result)