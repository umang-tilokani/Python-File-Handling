# seek()
f = open("abc.txt")
print(f.readline())
f.seek(0) # resets the cursor position
print(f.readline())
f.close()
