# perfect_intro_to_python.py
# Comprehensive Python Introduction Script

# === 1. VARIABLES AND DATA TYPES ===
# Demonstrates different basic data types
user_name = "Alice"            # String
user_age = 25                  # Integer
user_height = 5.6              # Float
is_enrolled = True             # Boolean

print("=== Basic Information ===")
print("Name:", user_name)
print("Age:", user_age)
print("Height:", user_height)
print("Student:", is_enrolled)

# === 2. BASIC OPERATORS ===
# Demonstrates arithmetic operations
num1 = 10
num2 = 3

print("\n=== Arithmetic Operations ===")
print("Addition:", num1 + num2)
print("Subtraction:", num1 - num2)
print("Multiplication:", num1 * num2)
print("Division:", num1 / num2)
print("Modulus:", num1 % num2)

# === 3. USER INPUT WITH VALIDATION ===
# Gets user name and grade with error checking
print("\n=== User Interaction ===")
user_name_input = input("Enter your name: ")
print(f"Hello, {user_name_input}! Let's check your grade.")

# Validate numeric input for score
while True:
    try:
        user_score = int(input("Enter your test score (0–100): "))
        if 0 <= user_score <= 100:
            break
        else:
            print("Please enter a number between 0 and 100.")
    except ValueError:
        print("Invalid input. Please enter a number.")

# === 4. CONTROL FLOW ===
# Uses if-elif-else statements to assign a grade
print("\n=== Grading Result ===")
if user_score >= 90:
    print("Grade: A")
elif user_score >= 80:
    print("Grade: B")
elif user_score >= 70:
    print("Grade: C")
else:
    print("Grade: Needs Improvement")

# === 5. LOOPS ===
# For and while loop examples
print("\n=== For Loop: Counting 1–5 ===")
for i in range(1, 6):
    print(i)

print("\n=== While Loop: Countdown from 5 ===")
count = 5
while count > 0:
    print(count)
    count -= 1

# === 6. FUNCTION WITH DOCSTRING & ERROR HANDLING ===
def simple_calculator(x, y):
    """
    Performs basic arithmetic operations between two numbers.
    
    Parameters:
    x (float): First number
    y (float): Second number

    Prints the results of addition, subtraction, multiplication, and division.
    Handles division by zero.
    """
    print("\n=== Simple Calculator ===")
    print("Inputs:", x, "and", y)
    print("Sum:", x + y)
    print("Difference:", x - y)
    print("Product:", x * y)
    try:
        print("Quotient:", x / y)
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")

# Example calculator usage
simple_calculator(12, 4)
simple_calculator(10, 0)

# === 7. STRING METHODS ===
# Demonstrates common string manipulations
print("\n=== String Methods ===")
example_string = "   Python is FUN!   "
print("Original:", example_string)
print("Lowercase:", example_string.lower())         # Converts to lowercase
print("Stripped:", example_string.strip())          # Removes whitespace
print("Replaced:", example_string.replace("FUN", "awesome"))  # Replaces word

# === 8. LISTS ===
# Basic list operations
print("\n=== List Example ===")
fruit_list = ["apple", "banana", "cherry"]
fruit_list.append("orange")  # Adds a new fruit to the list
print("Fruits:", fruit_list)
print("First fruit:", fruit_list[0])

# === 9. DICTIONARIES ===
# Basic dictionary usage
print("\n=== Dictionary Example ===")
person_profile = {
    "name": "Bob",
    "age": 30,
    "city": "New York"
}
print("Profile:", person_profile)
print("Name from profile:", person_profile["name"])
