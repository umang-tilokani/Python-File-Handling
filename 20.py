import pickle
# writing into a binary file
def write():
    f = open("BinaryWrite.dat", "wb")
    l = ["Computer Science", "Maths", "Hindi", "English"]
    pickle.dump(l, f)
    print("Data written successfully in file.")
    f.close()
# reading from a binary file
def read():
    f = open("BinaryWrite.dat", "rb")
    l = pickle.load(f)
    print("Data from the file.")
    print(l)
    f.close()
write()
read()
