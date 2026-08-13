"""
Day 01 — Variables & Data Types
File: 05_booleans.py
Topic: bool — True/False, Truthiness, bool() Casting, bool as int

Run this file:   python 05_booleans.py
"""

# =============================================================================
# SECTION 1: Basic Boolean Values
# =============================================================================

print("--- Section 1: Basic Booleans ---")

# Only two possible values — always capitalized
is_training: bool = True
model_loaded: bool = False
use_gpu: bool = True
has_error: bool = False

print(f"is_training:  {is_training}")    # True
print(f"model_loaded: {model_loaded}")   # False
print(f"use_gpu:      {use_gpu}")        # True
print(f"has_error:    {has_error}")      # False
print(f"type(True):   {type(True)}")     # <class 'bool'>

# Critical: True and False are CAPITALIZED in Python
# 'true' and 'false' are NOT Python keywords — they would be variable names
# (and undefined ones at that, causing NameError)

# =============================================================================
# SECTION 2: Booleans Are Integers
# =============================================================================

print("\n--- Section 2: bool is a subclass of int ---")

# True equals 1, False equals 0
print(f"True == 1:    {True == 1}")         # True
print(f"False == 0:   {False == 0}")        # True
print(f"True + True:  {True + True}")       # 2
print(f"True + False: {True + False}")      # 1
print(f"True * 10:    {True * 10}")         # 10
print(f"False * 999:  {False * 999}")       # 0

# isinstance check
print(f"\nisinstance(True, bool):  {isinstance(True, bool)}")   # True
print(f"isinstance(True, int):   {isinstance(True, int)}")    # True!
print(f"isinstance(False, int):  {isinstance(False, int)}")   # True!

# ML Use: count correct predictions
# predictions = [True, False, True, True, False, True]
# correct = True + False + True + True + False + True = 4
# (We'll use sum() in Day 05 — for now just know booleans add as 0s and 1s)

# =============================================================================
# SECTION 3: Truthy and Falsy Values
# =============================================================================

print("\n--- Section 3: Truthy and Falsy ---")

# Falsy values — evaluate to False in a boolean context
print("Falsy values:")
print(f"  bool(False):  {bool(False)}")    # False
print(f"  bool(0):      {bool(0)}")        # False
print(f"  bool(0.0):    {bool(0.0)}")      # False
print(f"  bool(''):     {bool('')}")       # False
print(f"  bool(None):   {bool(None)}")     # False

# Truthy values — everything else
print("\nTruthy values:")
print(f"  bool(True):   {bool(True)}")     # True
print(f"  bool(1):      {bool(1)}")        # True
print(f"  bool(-1):     {bool(-1)}")       # True — non-zero!
print(f"  bool(0.001):  {bool(0.001)}")    # True — non-zero!
print(f"  bool('hi'):   {bool('hi')}")     # True — non-empty!
print(f"  bool(' '):    {bool(' ')}")      # True — space is not empty!

# =============================================================================
# SECTION 4: bool() Casting
# =============================================================================

print("\n--- Section 4: bool() Casting ---")

# Cast any value to bool explicitly
print(bool(42))        # True  — non-zero int
print(bool(0))         # False — zero int
print(bool(-5))        # True  — non-zero int (even negative!)
print(bool(0.0001))    # True  — non-zero float
print(bool("Python"))  # True  — non-empty string
print(bool(""))        # False — empty string
print(bool(None))      # False — None is always falsy

# =============================================================================
# SECTION 5: Common Boolean Mistakes
# =============================================================================

print("\n--- Section 5: Common Mistakes ---")

# Mistake 1: Using lowercase true/false
# is_active = true   → NameError: name 'true' is not defined
is_active = True     # Correct

# Mistake 2: Comparing bool to string
flag = True
print(f"True == 'True': {True == 'True'}")    # False!
# True (bool) is NOT the same as "True" (string)

# Mistake 3: Forgetting zero is falsy
error_count = 0
# Later in Day 03 you will write: if error_count: ... 
# This evaluates False because 0 is falsy — be careful!
print(f"bool(0) is falsy: {bool(error_count)}")   # False

# =============================================================================
# EXPECTED OUTPUT
# =============================================================================
#
# --- Section 1: Basic Booleans ---
# is_training:  True
# model_loaded: False
# use_gpu:      True
# has_error:    False
# type(True):   <class 'bool'>
#
# --- Section 2: bool is a subclass of int ---
# True == 1:    True
# False == 0:   True
# True + True:  2
# True + False: 1
# True * 10:    10
# False * 999:  0
# isinstance(True, bool):  True
# isinstance(True, int):   True
# isinstance(False, int):  True
#
# --- Section 3: Truthy and Falsy ---
# Falsy values:
#   bool(False):  False
#   bool(0):      False
#   bool(0.0):    False
#   bool(''):     False
#   bool(None):   False
# Truthy values:
#   bool(True):   True
#   bool(1):      True
#   bool(-1):     True
#   bool(0.001):  True
#   bool('hi'):   True
#   bool(' '):    True
