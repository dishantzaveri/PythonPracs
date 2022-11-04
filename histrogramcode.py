def histogram(l): 
    l2=list(set(l)) 
    l2.sort()
    fr=[]
    for el in l2: 
        fr.append(l.count(el))
    d= dict(zip(l2,fr))
    sorted_v = sorted(d.values()) 
    sorted_d={}
    for val in sorted_v: 
        for i in d:
            if d[i]==val: 
                sorted_d[i]=val
    return sorted_d


print(histogram([3,2,1,3,4,3,7,7,3,4,2]))