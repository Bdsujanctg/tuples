w=(1,0,0,0,1,1,0)
rain=0
sunny=0
for i in range(0,7):
    if (w[i]==0):
        sunny+=1
    else:
        rain+=1
if (sunny>rain):
    print("Good weather")
else:
    print("Bad weather")