# [1,2,3,1,3,4,6,5,3] get unique numbers from list with basic constructs

nums=[12, 10, 9, 45, 2, 10, 10, 4]

d=dict()

for x in nums:
    if (x not in d.keys()):
        d[x]=1
    else:
        d[x]+=1
        
ans=[k for k,v in d.items() if v==1]            

print(ans)