try:
    file = open("somefile.txt", "r")
    print(file.read())
except FileNotFoundError:
    print("File not found.")
finally:
    print("Program ended.")
