import pickle
# writing into a binary file
def write():
    f = open("BinaryWrite.dat", "wb")
    # working with list
    l = ["Computer Science", "Maths", "Hindi", "English"]
    # working with dictionary
    d = {"Computer" : 89, "Maths" : 88, "English" : 87, "Hindi" : 86}
    pickle.dump(l, f)
    pickle.dump(d, f)
    print("Data written successfully in file.")
    f.close()
# reading from a binary file
def read():
    f = open("BinaryWrite.dat", "rb")
    l = pickle.load(f)
    d = pickle.load(f)
    print("Data from the file.")
    print(l)
    print(d)
    f.close()
write()
read()
