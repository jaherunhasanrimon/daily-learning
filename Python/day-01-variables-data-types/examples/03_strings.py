"""
Day 01 — Variables & Data Types
Topic: The str Data Type — Creation, Quotes, f-Strings, Length, Escape

"""

                            ## SECTION 1: Creating Strings ##

import _frozen_importlib_external
print("-------- Section 1: Creating Strings --------")

single_quoted: str = 'Hello, World!'
double_quoted: str = "Hello, World!"
triple_double: str = """This spans
multiple lines."""
triple_single: str = '''Another
multi-line string.'''
empty_string: str = ""

print(single_quoted)    # Hello, World!
print(double_quoted)    # Hello, World!
print(triple_double)    # This spans\nmultiple lines.
print(triple_single)    # Another\nmulti-line string.
print(repr(empty_string))  # ''
print(f'{empty_string!r}') # ''
print(empty_string) # 


# Professional convention: use double quotes by default
# Exception: when the string itself contains double quotes, use single quotes

                            ## SECTION 2: Escape Characters ##
                         
print("\n-------- Section 2: Escape Characters --------")

newline_demo: str = "Line 1\nLine 2\nLine 3"
print(newline_demo)
# Line 1
# Line 2
# Line 3

tab_demo: str = "Name\tScore\tGrade"
print(tab_demo)
# Name    Score   Grade

quote_demo: str = "She said \"Python is amazing!\""
print(quote_demo)
# She said "Python is amazing!"

backslash_demo: str = "C:\\Users\\Rimon\\data"
print(backslash_demo)
# C:\Users\Rimon\data

# Raw strings: backslash is taken literally (no escape processing)
raw_path: str = r"C:\Users\Rimon\data"
print(raw_path)
# C:\Users\Rimon\data   (same output, but cleaner to write)


                            ## SECTION 3: f-Strings (Formatted String Literals) ##

print("\n-------- Section 3: f-Strings --------")

name: str = "Rimon"
age: int = 24
score: float = 98.567

# Basic interpolation
print(f"Name: {name}")                  # Name: Rimon
print(f"Age: {age}")                    # Age: 24

# Format specifiers inside f-strings
print(f"Score: {score:.2f}")           # Score: 98.57  (2 decimal places)
print(f"Score: {score:.0f}")           # Score: 99     (0 decimal places, rounded)
print(f"Age with padding: {age:05d}")  # Age with padding: 00024

# Expressions directly inside f-strings
print(f"In 5 years: {age + 5}")        # In 5 years: 29
print(f"Score as int: {int(score)}")   # Score as int: 98



                            ## SECTION 4: String Length ##

print("\n-------- Section 4: String Length/ len() --------")

word: str = "Python"
print(f"'{word}' has {len(word)} characters")   # 'Python' has 6 characters

sentence: str = "Machine Learning"
print(f"'{sentence}' has {len(sentence)} characters")  # 16 characters

empty: str = ""
print(f"Empty string length: {len(empty)}")    # 0

                            ## SECTION 5: Strings and Type Checks ##

print("\n-------- Section 5: Strings and Type Checks --------")

text: str = "hello"
print(type(text))               # <class 'str'>
print(isinstance(text, str))    # True

number_as_string = "42"
print(type(number_as_string))   # <class 'str'>
# Even though the content looks like a number, it IS a string.
# You CANNOT do arithmetic on it without casting.

                            ## SECTION 6: Common String Mistakes ##

print("\n-------- Section 6: Common String Mistakes --------")

# Mistake 1: Mixing quotes and creating syntax error
# broken = "He said "hello" "   — SyntaxError!
# Fix: 
fixed1 = "He said \"hello\""
#or
fixed2 = 'He said "hello"'
print(fixed1)
print(fixed2)

# Mistake 2: Confusing None and "None"
actual_none = None
string_none = "None"
print(f"type(actual_none): {type(actual_none)}")   # <class 'NoneType'>
print(f"type(string_none): {type(string_none)}")   # <class 'str'>
print(f"Are they equal? {actual_none == string_none}")  # False

# Mistake 3: Forgetting strings are immutable
greeting = "hello"
# greeting[0] = "H"  — This would cause TypeError
# To change a string, you must create a new one.

print("(String modification covered later)")

