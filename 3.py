f = open("abc.txt")
content = f.read(14)
print("1:", content)
content = f.read(5)
print("2:", content)
f.close()
