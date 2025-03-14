def palind(r):
    e=len(r)-1
    s=0
    while(s<e):
        if (r[s]!=r[e]):
            return False
        s+=1
        e-=1
    return True
r=(2,6,5,5,6,2)
if (palind(r)):
    print("The tuple is a palindrome")
else:
    print("Your tuple is NOT a palindrome")