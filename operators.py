# Program to demonstrate various operators in Python
# ==========================================
# 1. ARITHMETIC OPERATORS
# ==========================================
a, b = 10, 3
print("--- Arithmetic ---")
print(f"Addition (+): 10 + 3 = {a + b}")
print(f"Subtraction (-): 10 - 3 = {a - b}")
print(f"Multiplication (*): 10 * 3 = {a * b}")
print(f"Division (/): 10 / 3 = {a / b}")       # Returns float
print(f"Floor Division (//): 10 // 3 = {a // b}") # Returns truncated int
print(f"Modulus (%): 10 % 3 = {a % b}")         # Returns remainder
print(f"Exponentiation (**): 10 ** 3 = {a ** b}")

# ==========================================
# 2. COMPARISON (RELATIONAL) OPERATORS
# ==========================================
print("\n--- Comparison ---")
print(f"Equal to (==): 10 == 3 is {a == b}")
print(f"Not equal to (!=): 10 != 3 is {a != b}")
print(f"Greater than (>): 10 > 3 is {a > b}")
print(f"Less than (<): 10 < 3 is {a < b}")
print(f"Greater than or equal to (>=): 10 >= 3 is {a >= b}")
print(f"Less than or equal to (<=): 10 <= 3 is {a <= b}")

# ==========================================
# 3. LOGICAL OPERATORS
# ==========================================
t, f = True, False
print("\n--- Logical ---")
print(f"Logical AND (and): True and False = {t and f}")
print(f"Logical OR (or): True or False = {t or f}")
print(f"Logical NOT (not): not True = {not t}")

# ==========================================
# 4. BITWISE OPERATORS
# ==========================================
# 5 is 0101, 3 is 0011 in binary
x, y = 5, 3
print("\n--- Bitwise ---")
print(f"Bitwise AND (&): 5 & 3 = {x & y}")       # 0001 -> 1
print(f"Bitwise OR (|): 5 | 3 = {x | y}")        # 0111 -> 7
print(f"Bitwise XOR (^): 5 ^ 3 = {x ^ y}")       # 0110 -> 6
print(f"Bitwise NOT (~): ~5 = {~x}")             # -(x+1) -> -6
print(f"Bitwise Left Shift (<<): 5 << 1 = {x << 1}") # 1010 -> 10
print(f"Bitwise Right Shift (>>): 5 >> 1 = {x >> 1}") # 0010 -> 2

# ==========================================
# 5. IDENTITY OPERATORS
# ==========================================
list1 = [1, 2, 3]
list2 = [1, 2, 3]
list3 = list1
print("\n--- Identity ---")
print(f"is (same object): list1 is list3 is {list1 is list3}")
print(f"is (different objects): list1 is list2 is {list1 is list2}") 
print(f"is not: list1 is not list2 is {list1 is not list2}")

# ==========================================
# 6. MEMBERSHIP OPERATORS
# ==========================================
my_list = [1, 2, 3, 4, 5]
print("\n--- Membership ---")
print(f"in: 3 in my_list is {3 in my_list}")
print(f"not in: 6 not in my_list is {6 not in my_list}")

# ==========================================
# 7. ASSIGNMENT & AUGMENTED ASSIGNMENT OPERATORS
# ==========================================
print("\n--- Assignment ---")
c = 5; print(f"Basic Assignment (=): c = {c}")
c += 2; print(f"Add and Assign (+=): c = {c}")
c -= 1; print(f"Subtract and Assign (-=): c = {c}")
c *= 3; print(f"Multiply and Assign (*=): c = {c}")
c /= 2; print(f"Divide and Assign (/=): c = {c}")
c //= 2; print(f"Floor Divide and Assign (//=): c = {c}")
c %= 2; print(f"Modulus and Assign (%=): c = {c}")
c = int(c) # cast back to integer for bitwise assignments
c **= 3; print(f"Exponent and Assign (**=): c = {c}")
c &= 2; print(f"Bitwise AND and Assign (&=): c = {c}")
c |= 5; print(f"Bitwise OR and Assign (|=): c = {c}")
c ^= 3; print(f"Bitwise XOR and Assign (^=): c = {c}")
c <<= 1; print(f"Left Shift and Assign (<<=): c = {c}")
c >>= 1; print(f"Right Shift and Assign (>>=): c = {c}")
