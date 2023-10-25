import pickle
def write():
    f = open("BinaryWrite.dat", "wb")
    l = ["Computer Science", "Maths", "Hindi", "English"]
    pickle.dump(l, f)
    f.close()

write()
print("Data Written Successfully in file")
