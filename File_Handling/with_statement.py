#Best way to handle files safely
# with statement automatically file ko close kar deta hai — safe and clean method.
with open("example.txt","r") as file:
    print(file.read())