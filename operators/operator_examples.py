
# Arithmetic Operators (Mathematical Operations)
a = 10
b = 3
print("Addition:", a + b)       # 10 + 3 = 13
print("Subtraction:", a - b)    # 10 - 3 = 7
print("Multiplication:", a * b) # 10 * 3 = 30
print("Division:", a / b)       # 10 / 3 = 3.33
print("Modulus:", a % b)        # 10 % 3 = 1
print("Exponentiation:", a ** b) # 10^3 = 1000
print("Floor Division:", a // b) # 10 // 3 = 3

# Assignment Operators (Value Update Karne Wale)
x = 10
x += 5  # x = x + 5
print("After +=:", x)  # 15
x *= 2  # x = x * 2
print("After *=:", x)  # 30

# Comparison Operators (isEqual, notEqual, greater thn , less thn)
print(a == b)  # False 
print(a != b)  # True 
print(a > b)   # True 
print(a < b)   # False

# Logical Operators (AND, OR, NOT)
print(True and False) # False
print(True or False)  # True
print(not True)       # False

# Identity Operators (`is` aur `is not`)
c = [1, 2, 3]
d = [1, 2, 3]
e = c
print(c is e)  # True (Dono same object hain)
print(c is d)  # False (Alag-alag objects hain)

# Membership Operators (`in` aur `not in`)
numbers = [1, 2, 3, 4, 5]
print(3 in numbers)  # True
print(10 in numbers) # False

# Bitwise Operators (Binary level wale)
a = 5  # 0101
b = 3  # 0011
print(a & b)  # 0001 = 1
print(a | b)  # 0111 = 7
print(a ^ b)  # 0110 = 6

