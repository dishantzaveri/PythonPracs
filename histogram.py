def histogram(l):
    count=0
    x=[]
    k=[]
    for i in range(len(1)):
        index=i
        count=0
        for j in range(index,len(1)):
            if l[index] == l[j] and l[index] not in k:
                count+=1
        k=k+ [l[index]]
        
    
