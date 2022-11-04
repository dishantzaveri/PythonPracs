d={
'a':1,
'b':2,
'c':3,
'd':4
}
print(f"items: {d.items()}")
print(f"keys: {d.keys()}")
print(f"values: {d.values()}")
print(f"pop: {d.pop('a')}")

print(f"get: {d.get('c')}") 
d.clear()
print(f"clear: {d}")