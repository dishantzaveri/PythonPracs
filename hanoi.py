def hanoi(n,source,destination,auxiliary):
    if n==1:
        print("move disk 1 from source",source,"to destination",destination)
        return
    hanoi(n-1,source,auxiliary,destination)
    print("move disk",n,"from source",source,"to destination",destination)
    hanoi(n-1,auxiliary,destination,source)


hanoi(4,"A","B","C")