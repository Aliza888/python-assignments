def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero manually raised!")
    return a / b

try:
    print(divide(10, 0))
except ZeroDivisionError as e:
    print("Error:", e)
