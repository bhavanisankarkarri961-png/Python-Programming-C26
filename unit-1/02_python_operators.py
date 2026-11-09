# ==========================================
#       PYTHON OPERATORS - UNIT 1
# ==========================================

a = 10
b = 3

# 1. ARITHMETIC OPERATORS
print("\n--- Arithmetic Operators ---")

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Floor Division:", a // b)
print("Modulus:", a % b)
print("Exponentiation:", a ** b)


# 2. ASSIGNMENT OPERATORS
print("\n--- Assignment Operators ---")

x = 10

x += 5
print("Addition Assignment:", x)

x -= 3
print("Subtraction Assignment:", x)

x *= 2
print("Multiplication Assignment:", x)

x /= 4
print("Division Assignment:", x)

x //= 2
print("Floor Division Assignment:", x)

x %= 3
print("Modulus Assignment:", x)

x **= 2
print("Exponent Assignment:", x)


# 3. COMPARISON OPERATORS
print("\n--- Comparison Operators ---")

print("Equal to:", a == b)
print("Not equal to:", a != b)
print("Greater than:", a > b)
print("Less than:", a < b)
print("Greater than or equal:", a >= b)
print("Less than or equal:", a <= b)


# 4. LOGICAL OPERATORS
print("\n--- Logical Operators ---")

print("AND:", a > 5 and b < 5)
print("OR:", a < 5 or b < 5)
print("NOT:", not(a > 5))


# 5. MEMBERSHIP OPERATORS
print("\n--- Membership Operators ---")

numbers = [10, 20, 30, 40, 50]

print("10 in numbers:", 10 in numbers)
print("60 in numbers:", 60 in numbers)
print("10 not in numbers:", 10 not in numbers)


# 6. IDENTITY OPERATORS
print("\n--- Identity Operators ---")

list1 = [1, 2, 3]
list2 = [1, 2, 3]
list3 = list1

print("list1 is list2:", list1 is list2)
print("list1 is list3:", list1 is list3)
print("list1 is not list2:", list1 is not list2)


# 7. BITWISE OPERATORS
print("\n--- Bitwise Operators ---")

p = 5
q = 3

print("Bitwise AND:", p & q)
print("Bitwise OR:", p | q)
print("Bitwise XOR:", p ^ q)
print("Bitwise NOT:", ~p)
print("Left Shift:", p << 1)
print("Right Shift:", p >> 1)


# ==========================================
#             END OF OPERATORS
# ==========================================