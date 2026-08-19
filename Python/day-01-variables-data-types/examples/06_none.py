"""
Day 01 — Variables & Data Types
File: 06_none.py
Topic: NoneType — Python's Null Value

Run this file:   python 06_none.py
"""

# =============================================================================
# SECTION 1: What is None?
# =============================================================================

print("--- Section 1: None Basics ---")

result: None = None
user_input: None = None
cached_value: None = None

print(f"result:       {result}")            # None
print(f"type(None):   {type(None)}")        # <class 'NoneType'>
print(f"type(result): {type(result)}")      # <class 'NoneType'>

# None is not zero, not empty string, not False — it is absence of value
print(f"\nNone == 0:     {None == 0}")        # False
print(f"None == '':    {None == ''}")        # False
print(f"None == False: {None == False}")     # False
print(f"bool(None):    {bool(None)}")        # False (None is falsy, but NOT False)

# =============================================================================
# SECTION 2: None is a Singleton
# =============================================================================

print("\n--- Section 2: None is a Singleton ---")

# There is exactly ONE None object in all of Python
a = None
b = None
c = None

# All three point to the SAME None object
print(f"a is b: {a is b}")    # True — same object!
print(f"b is c: {b is c}")    # True — same object!
print(f"a is c: {a is c}")    # True — same object!

# Therefore: use 'is' to check for None (not ==)
# == checks value equality, 'is' checks identity (same object)

# =============================================================================
# SECTION 3: Checking for None — the Right Way
# =============================================================================

print("\n--- Section 3: Correct None Checking ---")

model_output = None

# ✅ Correct — uses identity check
print(f"model_output is None:     {model_output is None}")      # True
print(f"model_output is not None: {model_output is not None}")  # False

# ❌ Works but not Pythonic — avoid in professional code
print(f"model_output == None:     {model_output == None}")      # True (but not best practice)

# =============================================================================
# SECTION 4: Real-World None Usage
# =============================================================================

print("\n--- Section 4: Real-World Usage ---")

# Pattern: Initialize to None, assign later when available
training_accuracy: None = None
validation_accuracy: None = None
model_name: str = "bert-v2"

print(f"Model: {model_name}")
print(f"Training accuracy: {training_accuracy}")       # None — not computed yet
print(f"Validation accuracy: {validation_accuracy}")   # None — not computed yet

# After "training" (just reassigning in this example):
training_accuracy = 0.9821
validation_accuracy = 0.9412

print(f"\nAfter training:")
print(f"Training accuracy: {training_accuracy}")       # 0.9821
print(f"Validation accuracy: {validation_accuracy}")   # 0.9412

# =============================================================================
# SECTION 5: None vs "None" — Critical Distinction
# =============================================================================

print("\n--- Section 5: None vs 'None' String ---")

actual_none = None
string_none = "None"

print(f"actual_none type: {type(actual_none)}")  # <class 'NoneType'>
print(f"string_none type: {type(string_none)}")  # <class 'str'>
print(f"Are they equal? {actual_none == string_none}")  # False!
print(f"actual_none is None: {actual_none is None}")    # True
print(f"string_none is None: {string_none is None}")    # False

# This distinction matters: if you read "None" from a CSV file,
# it is a string, not Python's None. You must handle this explicitly.
# (CSV reading is covered in Data-Analysis module.)

# =============================================================================
# EXPECTED OUTPUT
# =============================================================================
#
# --- Section 1: None Basics ---
# result:       None
# type(None):   <class 'NoneType'>
# type(result): <class 'NoneType'>
# None == 0:     False
# None == '':    False
# None == False: False
# bool(None):    False
#
# --- Section 2: None is a Singleton ---
# a is b: True
# b is c: True
# a is c: True
#
# --- Section 3: Correct None Checking ---
# model_output is None:     True
# model_output is not None: False
# model_output == None:     True
