#Handle file errors
# Agar file exist nahi karti to program crash nahi hota, error handle ho jata hai.
try:
    file = open("missig.txt", "r")
    print(file.read())
except FileNotFoundError:
    print("Print file not found!")