"""
Day 01 — Variables & Data Types
File: 04_numbers.py
Topic: int, float, complex — Properties, Precision, Special Values

"""

                            ## SECTION 1: Integers (int) ##

print("-------- Section 1: Integers --------")

# Basic integer values
samples: int = 50_000        # underscore separator for readability
negative: int = -273         # negative integer
zero: int = 0

print(f"samples: {samples}")           # 50000
print(f"negative: {negative}")        # -273
print(f"zero: {zero}")               # 0

# Python integers have UNLIMITED precision
very_large: int = 2 ** 100
print(f"2^100 = {very_large}")
# 1267650600228229401496703205376

# Different number bases
binary_value = 0b1010       # Binary (base 2) — prefix 0b
octal_value = 0o12          # Octal (base 8) — prefix 0o
hex_value = 0xFF            # Hexadecimal (base 16) — prefix 0x

print(f"Binary 0b1010    = {binary_value}")    # 10
print(f"Octal 0o12       = {octal_value}")     # 10
print(f"Hex 0xFF         = {hex_value}")       # 255

# =============================================================================
# SECTION 2: Floats (float)
# =============================================================================

print("\n--- Section 2: Floats ---")

accuracy: float = 0.9742
pi: float = 3.14159
learning_rate: float = 0.001
negative_float: float = -36.6

print(f"accuracy: {accuracy}")
print(f"pi: {pi}")
print(f"learning_rate: {learning_rate}")

# Scientific notation
tiny: float = 1.5e-10         # 1.5 × 10⁻¹⁰
huge: float = 1.5e8           # 150,000,000.0
print(f"tiny: {tiny}")         # 1.5e-10
print(f"huge: {huge}")         # 150000000.0

# =============================================================================
# SECTION 3: The Floating-Point Precision Trap
# =============================================================================

print("\n--- Section 3: Float Precision ---")

# This is NOT a Python bug — it affects ALL languages using IEEE 754
result = 0.1 + 0.2
print(f"0.1 + 0.2 = {result}")                # 0.30000000000000004
print(f"Is it exactly 0.3? {result == 0.3}")  # False!

# How it looks when formatted
print(f"Formatted: {result:.1f}")              # 0.3  (formatted, but stored value is not 0.3)

# Special float values
infinity: float = float('inf')
neg_infinity: float = float('-inf')
not_a_number: float = float('nan')

print(f"\ninfinity:     {infinity}")       # inf
print(f"neg_infinity: {neg_infinity}")     # -inf
print(f"NaN:          {not_a_number}")     # nan

# NaN is unusual — it does not equal itself
print(f"nan == nan:   {not_a_number == not_a_number}")  # False!

# =============================================================================
# SECTION 4: int vs float Arithmetic Preview
# =============================================================================

print("\n--- Section 4: int vs float Result Types ---")

# int + int → int
a = 5
b = 3
result_int = a + b
print(f"{a} + {b} = {result_int}, type: {type(result_int)}")   # <class 'int'>

# int + float → float (Python promotes to the more precise type)
c = 5
d = 3.0
result_float = c + d
print(f"{c} + {d} = {result_float}, type: {type(result_float)}")   # <class 'float'>

# / always returns float (even for whole-number results)
division_result = 10 / 2
print(f"10 / 2 = {division_result}, type: {type(division_result)}")  # 5.0, <class 'float'>
# Full operator coverage in Day 02!

# =============================================================================
# SECTION 5: Complex Numbers
# =============================================================================

print("\n--- Section 5: Complex Numbers ---")

# Complex: real_part + imaginary_part * j
signal: complex = 3 + 4j
print(f"signal: {signal}")              # (3+4j)
print(f"real part: {signal.real}")      # 3.0
print(f"imaginary part: {signal.imag}") # 4.0
print(f"type: {type(signal)}")          # <class 'complex'>

pure_imaginary = 0 + 2j
print(f"pure imaginary: {pure_imaginary}")  # 2j

# Note: Complex numbers are more relevant in signal processing
# and some advanced math — you'll encounter them in ML later.

# =============================================================================
# EXPECTED OUTPUT (abbreviated)
# =============================================================================
#
# --- Section 1: Integers ---
# samples: 50000
# negative: -273
# zero: 0
# 2^100 = 1267650600228229401496703205376
# ...
# --- Section 3: Float Precision ---
# 0.1 + 0.2 = 0.30000000000000004
# Is it exactly 0.3? False
# Formatted: 0.3
# ...
# nan == nan:   False
