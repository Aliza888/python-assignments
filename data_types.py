#1. String (str)
# A string stores text. It must be written inside single (' '), double (" "), or triple (""" """) quotes.

name:str = 'Ali Raza'
city = "Karachi"
message = """Hello,how are you?"""

print(name)
print(type(city))

#2. Integer (int)
# An integer stores whole numbers (without decimals).
x = 22
y = -3
year = 2025
print(type(y))

# 3. Float (float) - Decimal Numbers
# A float stores numbers with decimals.

a = 3.22
b = -0.5
pi = 22/7
temperature = 36.6

print(type(a))

# 4. Boolean (bool) - True or False
# A boolean stores only True or False values.

is_raining = True
is_sunny = False
passed_exam = True
print(type(is_raining))


#  5. List (list) - Ordered Collection (Allows Duplicates)
# A list can store multiple values and can be changed (mutable). It allows duplicate values.

#  When to Use 
# Use a List when you need to modify data.

numbers = [1,2,3,4,5]
fruits = ["apple","banana","mango"]
mixed = ["Ali",2,4.22,True]
print(type(mixed))

#  When to Use 
# Use a List when you need to modify data.
shopping_list = ["milk", "eggs", "bread"]
shopping_list.append("butter")  # Can add items
shopping_list[0] = "almond milk"  # Can change items


#  6. Tuple (tuple) - Ordered Collection (Cannot Change)
# A tuple is like a list, but cannot be modified (immutable).

coordinates = (10.2,20.2)
fruits = ("apple","banana","cherry")
rgb_colors = (255,0,128)
print(type(rgb_colors))

#  Use a Tuple when data should stay the same.
weekdays = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday")  
# These are fixed and should not be changed


#  7. Dictionary (dict) - Key-Value Pairs
# A dictionary stores data in key-value pairs, like a real dictionary.

student = {"name": "Owais","Age": 22,"city": "karachi"}
car = {"brand": "Toyota", "model": "Corolla", "year": 2020}  
print(type(student))


# 8. Set (set) - Unique Values (Unordered)
# A set stores only unique values and does not allow duplicates.

unique_numbers = {1,2,3,4,5,5}
print(unique_numbers)
print(type(unique_numbers))

# 9. None Type (None) - Empty or No Value
# None represents no value or an empty variable.


x = None

def test ():
    return None
print(type(x))


# 10. Frozen Set (frozenset) - Immutable Set
# A frozen set is like a set, but cannot be changed (immutable).

frozen_numbers = frozenset([1,2,3,4,5])
frozen_vowels = frozenset(['a','e','i','o','u'])
print(type(frozen_numbers))