fruits = ["apple" ,"orange","cherry"]
print(list(('apple','orange','cherry')))
print(len(fruits))
print(fruits.index("apple"))
fruits.append("grapes")
print(fruits)
fruits.insert(3,"banana") # inserted at index 3
print(fruits)
print(fruits.count("apple"))
fruits.remove("grapes")
print(fruits)
print(fruits.pop())
fruits.reverse()
print(fruits)
fruits.sort()
print(fruits)
cpy = fruits.copy()
print("cpy -- " ,cpy)
print("clear cpy --",cpy.clear())
fruits.extend(list(('apple','orange','cherry')))
print(fruits)