# handling read and write both (r+ mode)
f = open("abc.txt", "r+")
print(f.read())
f.write("\n THANK YOU!")
f.close()
