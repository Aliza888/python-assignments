try:
    number = int(input("Enter a number: "))
    print("you entered:", number)
except ValueError:
    print("Invalid input! Please enter a number.")