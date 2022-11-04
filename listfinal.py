l=[1,3,6,8,5,6,2,65,4,9,2]
print(l) 
l.append(8)
print(f"append: {l}")
l1=[5,6,8,6,3,78,2]
l.extend(l1) 
print(f"extend: {l}") 
print(f"index: {l.index(5)}")
print(f"pop: {l.pop(5)}") 
l.sort()
print(f"sort: {l}") 
l.reverse() 
print(f"reverse: {l}")