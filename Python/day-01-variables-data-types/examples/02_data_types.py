"""
Day 01 — Variables & Data Types

Topic: All Six Primitive Types + type() + isinstance()

"""

                        ## SECTION 1: The Six Primitive Data Types — Overview ##

print("-------- Section 1: All Six Primitive Types --------")

# int — whole number
num_layers: int = 6

# float — decimal number
dropout: float = 0.15

# complex — real + imaginary
signal: complex = 3 + 4j

# str — text
model_name: str = "transformer-v2"

# bool — True or False only
is_ready: bool = True

# NoneType — absence of value
result: None = None

# Print them all with their types
print(f"int:     {num_layers!r:<20} type -> {type(num_layers)}")
print(f"float:   {dropout!r:<20} type -> {type(dropout)}")
print(f"complex: {signal!r:<20} type -> {type(signal)}")
print(f"str:     {model_name!r:<20} type -> {type(model_name)}")
print(f"bool:    {is_ready!r:<20} type -> {type(is_ready)}")
print(f"None:    {result!r:<20} type -> {type(result)}")

                        ## SECTION 2: Using type() ##

print("\n-------- Section 2: type() Function --------")

# type() returns the class of the value — NOT a string, an actual class object
print(type(42))              # <class 'int'>
print(type(3.14))            # <class 'float'>
print(type(2 + 3j))          # <class 'complex'>
print(type("hello"))         # <class 'str'>
print(type(True))            # <class 'bool'>
print(type(None))            # <class 'NoneType'>

# Comparing type() output
print(type(42) == int)       # True
print(type(42) == float)     # False
print(type(True) == bool)    # True
print(type(True) == int)     # False  ← type() is EXACT, no inheritance

                        ## SECTION 3: Using isinstance() ##

print("\n-------- Section 3: isinstance() Function --------")

# isinstance() checks type INCLUDING parent classes (subclasses)
print(isinstance(42, int))          # True
print(isinstance(3.14, float))      # True
print(isinstance("hello", str))     # True
print(isinstance(True, bool))       # True
print(isinstance(True, int))        # True  ← bool IS a subclass of int!
print(isinstance(None, type(None))) # True  ← NoneType
print(isinstance(43, float) )        # False

# Checking multiple types at once with a tuple
value = 42
print(isinstance(value, (int, float)))   # True — value is int, which matches

value2 = "hello"
print(isinstance(value2, (int, float)))  # False — str is neither int nor float

                        ## SECTION 4: type() vs isinstance() — the critical difference ##

print("\n-------- Section 4: type() vs isinstance() --------")

# type() is EXACT
print("type() checks:")
print(type(True) == bool)   # True  — True IS a bool
print(type(True) == int)    # False — type() sees only the exact class

# isinstance() includes parent classes
print("\nisinstance() checks:")
print(isinstance(True, bool))   # True  — True is a bool
print(isinstance(True, int))    # True  — bool is a subclass of int!
print(isinstance(True, float))  # False — bool is not a subclass of float

# RULE: In production code, use isinstance() for type-checking logic.
# Use type() for debugging/display only.

                        ## SECTION 5: Checking Types in Real ML-Like Context ##

print("\n-------- Section 5: ML Context Type Checks --------")

learning_rate = 0.001
batch_size = 32 
model_name = "bert-base"
is_training = True
cached_output = None

print(f"learning_rate is float: {isinstance(learning_rate, float)}")
print(f"batch_size is int:      {isinstance(batch_size, int)}")
print(f"model_name is str:      {isinstance(model_name, str)}")
print(f"is_training is bool:    {isinstance(is_training, bool)}")
print(f"cached_output is None:  {cached_output is None}")

