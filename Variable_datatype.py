

# 1.1 INTEGER (int) - Whole numbers without decimal points
age = 25
year = 2024
temperature = -10
large_number = 1000000
binary_number = 0b1010  # Binary representation
octal_number = 0o755    # Octal representation
hex_number = 0xFF       # Hexadecimal representation

import random;
random_number=random.randint(1,100)

random.choice([1,2,3,4,5])
random.shuffle([1,2,3,4,5])

from decimal import Decimal
Decimal('0.1')+Decimal('0.2')+Decimal('0.3')



print(f"Age: {age}, Type: {type(age)}")
print(f"Year: {year}, Type: {type(year)}")
print(f"Temperature: {temperature}")
print(f"Binary (0b1010): {binary_number}")
print(f"Octal (0o755): {octal_number}")
print(f"Hex (0xFF): {hex_number}")
print("hello world","welcome to python programming",sep="-",end="!!!\n",flush=True)


# 1.2 FLOAT (float) - Numbers with decimal points
height = 5.9
pi = 3.14159
scientific = 2.5e3  # Scientific notation (2500.0)
weight = 72.5

print(f"\n--- FLOAT EXAMPLES ---")
print(f"Height: {height}, Type: {type(height)}")
print(f"Pi: {pi}")
print(f"Scientific notation (2.5e3): {scientific}")
print(f"Weight: {weight}")


# 1.3 STRING (str) - Sequence of characters
name = "John Doe"
message = 'Hello, World!'
multiline = """This is a
multiline
string"""
empty_string = ""
with_escape = "Name: \"John\"\nAge: 25"  # Escape sequences

print(f"\n--- STRING EXAMPLES ---")
print(f"Name: {name}, Type: {type(name)}")
print(f"Message: {message}")
print(f"Multiline:\n{multiline}")
print(f"With escape characters:\n{with_escape}")

num_list="0123456789"
num_list[0:5] #output:'01234'
num_list[:]
#output:'0123456789'
num_list[::2]
#output:'02468'
num_list[::-2]
#output:'97531'
num_list[1:8:3]
#output:'147'
value="Hello world"
print(value.__len__())
#output:11
print(value.upper())
#output:'HELLO WORLD'
print(value.lower())
#output:'hello world'
print(value.split())
#output:['Hello', 'world']
print(value.replace("world", "Python"))
#output:'Hello Python'
print(value.find("world"))
#output:6
print(value.count("o"))
#output:2
print(value.join(["Hello", "World"]))
#output:'HelloHello WorldWorld'

# 1.4 BOOLEAN (bool) - True or False
is_student = True
is_employed = False
is_adult = age >= 18
is_valid = not False

print(f"\n--- BOOLEAN EXAMPLES ---")
print(f"is_student: {is_student}, Type: {type(is_student)}")
print(f"is_employed: {is_employed}")
print(f"is_adult (age >= 18): {is_adult}")
print(f"is_valid (not False): {is_valid}")


# 
# 2. COLLECTION DATA TYPES
# 

# 2.1 LIST - Ordered, mutable, allows duplicates
fruits = ["apple", "banana", "orange", "apple"]
numbers = [1, 2, 3, 4, 5]
mixed_list = [1, "hello", 3.14, True, None]
nested_list = [1, [2, 3], [4, [5, 6]]]

print(f"\n--- LIST EXAMPLES ---")
print(f"Fruits: {fruits}")
print(f"Numbers: {numbers}")
print(f"Mixed list: {mixed_list}")
print(f"Nested list: {nested_list}")
print(f"First fruit: {fruits[0]}")
print(f"Last fruit: {fruits[-1]}")
print(f"Slice [1:3]: {numbers[1:3]}")


# List operations
fruits.append("mango")
fruits.remove("apple")
fruits.extend(["grape", "kiwi"])
print(f"Modified fruits: {fruits}")

my_list=["apple","banana","Ginger","Orange","Pinapple"]
my_list[1:3]="Coconut" #['apple', 'C', 'o', 'c', 'o', 'n', 'u', 't', 'Orange', 'Pinapple']
my_list[1:3]=["Coconut" ] #['apple', 'Coconut', 'Orange', 'Pinapple']

my_list.insert(1,"Mango") #['apple', 'Mango', 'Coconut', 'Orange', 'Pineapple']
my_list.pop(2) #['apple', 'Mango', 'Orange', 'Pinapple']
my_list.reverse() #['Pineapple', 'Orange', 'Mango', 'apple']
my_list.sort() #['Mango', 'Orange', 'Pinapple', 'apple']
my_list.clear() #[]

square_num_list=[x**2 for x in range(1,11)]
print(square_num_list) #[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]





# 2.2 TUPLE - Ordered, immutable, allows duplicates
colors = ("red", "green", "blue")
single_tuple = (42,)  # Note the comma for single element
empty_tuple = ()
nested_tuple = (1, (2, 3), (4, 5))

print(f"\n--- TUPLE EXAMPLES ---")
print(f"Colors: {colors}, Type: {type(colors)}")
print(f"Single element tuple: {single_tuple}")
print(f"Empty tuple: {empty_tuple}")
print(f"First color: {colors[0]}")
print(f"Slice [0:2]: {colors[0:2]}")
print(f"Length: {len(colors)}")


# 2.3 DICTIONARY - Unordered (Python 3.7+), mutable, key-value pairs
person = {
    "name": "Alice",
    "age": 30,
    "city": "New York",
    "is_student": False
}
numbers_dict = {1: "one", 2: "two", 3: "three"}
nested_dict = {
    "user1": {"name": "Bob", "age": 25},
    "user2": {"name": "Carol", "age": 28}
}
empty_dict = {}

print(f"\n--- DICTIONARY EXAMPLES ---")
print(f"Person: {person}") #output: 
print(f"Name: {person['name']}")
print(f"Age: {person.get('age')}")
print(f"Keys: {person.keys()}")
print(f"Values: {person.values()}")
print(f"Items: {person.items()}")

# Dictionary operations
person["phone"] = "555-1234"
person.update({"city": "Los Angeles", "country": "USA"})
print(f"Updated person: {person}")

square_dict={x:x**2 for x in range(1,11)}
new_dict=dict.fromkeys(['a','b','c'],0)
print(new_dict) #{'a': 0, 'b': 0, 'c': 0}



# 2.4 SET - Unordered, mutable, no duplicates, unique elements
unique_numbers = {1, 2, 3, 4, 5}
colors_set = {"red", "green", "blue", "red"}  # Duplicates removed
empty_set = set()  # Note: {} creates dict, not set
numbers_set = set([1, 2, 3, 3, 4, 4, 5])

print(f"\n--- SET EXAMPLES ---")
print(f"Unique numbers: {unique_numbers}")
print(f"Colors set (duplicates removed): {colors_set}")
print(f"Numbers set from list: {numbers_set}")
print(f"Length: {len(unique_numbers)}")

# Set operations
unique_numbers.add(6)
unique_numbers.remove(1)
set1 = {1, 2, 3}
set2 = {3, 4, 5}
print(f"Union: {set1 | set2}")
print(f"Intersection: {set1 & set2}")
print(f"Difference: {set1 - set2}")


# 2.5 FROZENSET - Immutable set
frozen = frozenset([1, 2, 3, 4, 5])
print(f"\n--- FROZENSET EXAMPLES ---")
print(f"Frozenset: {frozen}, Type: {type(frozen)}")


# =
# 3. SPECIAL DATA TYPES
# 

# 3.1 NONE - Represents absence of value
empty_value = None
result = None
no_return = None

print(f"\n--- NONE EXAMPLES ---")
print(f"Empty value: {empty_value}, Type: {type(empty_value)}")
print(f"Is None: {result is None}")


# 3.2 BYTES - Immutable sequence of bytes
byte_string = b"Hello"
byte_array = bytes([72, 101, 108, 108, 111])

print(f"\n--- BYTES EXAMPLES ---")
print(f"Byte string: {byte_string}, Type: {type(byte_string)}") #output:Byte string: b'Hello', Type: <class 'bytes'>
print(f"Byte array: {byte_array}") #output:Byte array: b'Hello'


# 3.3 BYTEARRAY - Mutable sequence of bytes
mutable_bytes = bytearray(b"Hello")
mutable_bytes[0] = 74  # Change 'H' (72) to 'J' (74)

print(f"\n--- BYTEARRAY EXAMPLES ---")
print(f"Original: {bytearray(b'Hello')}")
print(f"Modified: {mutable_bytes}")


# 
# 4. TYPE CONVERSION
# 

print(f"\n--- TYPE CONVERSION EXAMPLES ---")

# String to Integer
str_to_int = int("42")
print(f"String '42' to int: {str_to_int}, Type: {type(str_to_int)}")

# String to Float
str_to_float = float("3.14")
print(f"String '3.14' to float: {str_to_float}")

# Integer to String
int_to_str = str(100)
print(f"Integer 100 to string: {int_to_str}, Type: {type(int_to_str)}")

# Float to Integer (truncates decimal)
float_to_int = int(3.14)
print(f"Float 3.14 to int: {float_to_int}")

# Integer to Float
int_to_float = float(42)
print(f"Integer 42 to float: {int_to_float}")

# String to List
str_to_list = list("Hello")
print(f"String 'Hello' to list: {str_to_list}")

# List to Tuple
list_to_tuple = tuple([1, 2, 3])
print(f"List [1,2,3] to tuple: {list_to_tuple}")

# List to Set
list_to_set = set([1, 2, 2, 3, 3])
print(f"List [1,2,2,3,3] to set: {list_to_set}")

# Integer to Boolean
int_to_bool = bool(1)
print(f"Integer 1 to bool: {int_to_bool}") #output:Integer 1 to bool: True
print(f"Integer 0 to bool: {bool(0)}")  #output:Integer 0 to bool: False


# 
# 5. TYPE CHECKING
# 

print(f"\n--- TYPE CHECKING EXAMPLES ---")

# Using type() function
print(f"type(42): {type(42)}")
print(f"type(3.14): {type(3.14)}")
print(f"type('hello'): {type('hello')}")
print(f"type([1,2,3]): {type([1,2,3])}")

# Using isinstance() function
print(f"\nisinstance(1j,complex):{isinstance(1j,complex)}")
print(f"\nisinstance(42, int): {isinstance(42, int)}")
print(f"isinstance(3.14, float): {isinstance(3.14, float)}")
print(f"isinstance('hello', str): {isinstance('hello', str)}")
print(f"isinstance([1,2,3], list): {isinstance([1,2,3], list)}")
print(f"isinstance(True, bool): {isinstance(True, bool)}")
print(f"isinstance(True, int): {isinstance(True, int)}")  # bool is subclass of int


# 
# 6. VARIABLE NAMING CONVENTIONS
# 

print(f"\n--- VARIABLE NAMING CONVENTIONS ---")

# Valid naming conventions
student_name = "John"          # snake_case (recommended for variables)
StudentName = "Jane"           # PascalCase (for classes)
CONSTANT_VALUE = 100           # UPPER_CASE (for constants)
_private_var = "private"       # Leading underscore (convention for private)
__dunder_var = "dunder"        # Double underscore (name mangling)
var123 = "with numbers"        # Can include numbers (not at start)

print(f"student_name: {student_name}")
print(f"StudentName: {StudentName}")
print(f"CONSTANT_VALUE: {CONSTANT_VALUE}")
print(f"_private_var: {_private_var}")


# 
# 7. DYNAMIC TYPING - Variables can change type
# 

print(f"\n--- DYNAMIC TYPING EXAMPLES ---")

# Same variable, different types
value = 42
print(f"value = 42 -> Type: {type(value)}")

value = "Hello"
print(f"value = 'Hello' -> Type: {type(value)}")

value = 3.14
print(f"value = 3.14 -> Type: {type(value)}")

value = [1, 2, 3]
print(f"value = [1, 2, 3] -> Type: {type(value)}")


# 
# 8. MULTIPLE ASSIGNMENTS
# 

print(f"\n--- MULTIPLE ASSIGNMENT EXAMPLES ---")

# Assign multiple variables
x, y, z = 1, 2, 3
print(f"x={x}, y={y}, z={z}")

# Unpacking
data = [10, 20, 30]
a, b, c = data
print(f"Unpacked: a={a}, b={b}, c={c}")

# Swap variables
p, q = 100, 200
p, q = q, p
print(f"After swap: p={p}, q={q}")

# Multiple assignments to same value
m = n = o = 50
print(f"m={m}, n={n}, o={o}")


#
# 9. MEMORY AND OBJECT REFERENCE
# 

print(f"\n--- MEMORY AND OBJECT REFERENCE EXAMPLES ---")

# Same value, same object
num1 = 5
num2 = 5
print(f"num1 is num2: {num1 is num2}")  # True (small integers cached)
print(f"id(num1): {id(num1)}, id(num2): {id(num2)}")

# Lists (mutable) - different objects
list1 = [1, 2, 3]
list2 = [1, 2, 3]
print(f"\nlist1 is list2: {list1 is list2}")  # False
print(f"list1 == list2: {list1 == list2}")   # True (same content)
print(f"id(list1): {id(list1)}, id(list2): {id(list2)}")

# List reference
list3 = list1
print(f"\nlist3 = list1")
print(f"list3 is list1: {list3 is list1}")   # True (same object)
list3.append(4)
print(f"After list3.append(4): list1={list1}")  # list1 also changed


# ============================================================================
# 10. IMMUTABLE VS MUTABLE DATA TYPES
# ============================================================================

print(f"\n--- IMMUTABLE vs MUTABLE EXAMPLES ---")

# IMMUTABLE: int, float, str, tuple, frozenset, bool, None, bytes
immutable_str = "Hello"
immutable_str_2 = immutable_str.upper()  # Creates new string
print(f"Original: {immutable_str}, New: {immutable_str_2}")

# MUTABLE: list, dict, set, bytearray
mutable_list = [1, 2, 3]
mutable_list[0] = 10  # Modifies in place
print(f"Modified list: {mutable_list}")

mutable_dict = {"a": 1}
mutable_dict["b"] = 2  # Modifies in place
print(f"Modified dict: {mutable_dict}")


print("\n" + "="*80)
print("END OF VARIABLES AND DATA TYPES GUIDE")
print("="*80)

