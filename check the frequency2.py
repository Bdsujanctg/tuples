dict={"Years":5,'month':5,'weeks':6,'days':5,'hours':5,'minutes':4,'seconds':4}
print("The original dictionary:", dict)
k=5
result=0
for i in dict:
    if dict[i]==k:
        result+=1
print("The frequency of k is:",result)
