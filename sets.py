l1=[6,5,3,8,3,2,1,6,5,6,5,54]
l={1,3,6,8,5,6,2,65,4,9,2}
print(l)

l.add(10) 
print(f"add: {l}") 
l.discard(5) 
print(f"discard: {l}")
print(f"pop: {l.pop()}") 
l.update(l1) 
print(f"update: {l}")