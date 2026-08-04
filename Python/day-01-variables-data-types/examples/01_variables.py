"""
Day 01 — Variables & Data Types
File: 01_variables.py
Topic: Variable Assignment, Naming, and Rebinding

"""


                            ## SECTION 1: Basic Variable Assignment  ##

# The = sign assigns a value to a name.

full_name = "Jahirun Hassan Rimon"
age = 24
height_cm = 175.5
is_student = True
current_project = None

print("------- Section 1: Basic Assignment -------")
print(full_name)      # Jahirun Hassan Rimon
print(age)            # 24
print(height_cm)      # 175.5
print(is_student)     # True
print(current_project)  # None



                            ## SECTION 2: Type Annotations (Professional Habit) ##

# Type annotations document what type a variable holds.
# Python does NOT enforce them — they are hints, not rules.
# But use them! They make code readable and enable tooling.

full_name: str = "Jahirun Hassan Rimon"
age: int = 24
height_cm: float = 175.5
is_student: bool = True
current_project: None = None

print("\n------- Section 2: Annotated Variables -------")
print(f"Full name: {full_name}")
print(f"Age: {age}")
print(f"Height: {height_cm} cm")
print(f"Is student: {is_student}")
print(f"Current project: {current_project}")


                            ## SECTION 3: Variable Rebinding (Dynamic Typing) ##

# Python variables can point to any type at any time.
# The NAME stays, but what it POINTS TO can change completely.

score = 98              # score points to integer 98
print("\n------- Section 3: Rebinding ------- ")
print(f"score is {score}, type: {type(score)}")   # <class 'int'>

score = 90.009909
print(f"score is {score}, type: {type(score)}")   # <class 'float'>

score = 98.5            # score now points to float 98.5
print(f"score is {score}, type: {type(score)}")   # <class 'float'>

score = "A+"            # score now points to string "A+"
print(f"score is {score}, type: {type(score)}")   # <class 'str'>

# This is dynamic typing. Use it carefully — it can lead to bugs if you accidentally overwrite a variable with the wrong type.


                            ## SECTION 4: Multiple Assignment Patterns ##

print("\n------- Section 4: Multiple Assignment --------")

# Assign the same value to multiple names at once
x = y = z = 0
print(f"x={x}, y={y}, z={z}") # x=0, y=0, z=0

# Constants should use UPPER_SNAKE_CASE
MAX_EPOCHS: int = 100
DEFAULT_LEARNING_RATE: float = 0.001
MODEL_NAME: str = "gpt-mini"

print(f"MAX_EPOCHS: {MAX_EPOCHS}")
print(f"DEFAULT_LEARNING_RATE: {DEFAULT_LEARNING_RATE}")
print(f"MODEL_NAME: {MODEL_NAME}")

                            ## SECTION 5: Variable Naming — Valid and Invalid ##

print("\n------- Section 5: Naming Rules --------")

# All of these are VALID variable names
first_name = "Rimon"        # snake_case — recommended
_private = "hidden"         # leading underscore — indicates internal use
score2 = 95                 # letters followed by digits — valid
CONSTANT = 42               # uppercase — constant convention

print(first_name, _private, score2, CONSTANT)

# COMMON MISTAKE: Do not use reserved keywords as variable names.
# These would cause SyntaxError:
# if = 5         → SyntaxError
# for = 10       → SyntaxError
# class = "A"    → SyntaxError

                            ## SECTION 6: Professional Naming for ML Context ##

print("\n-------- Section 6: ML-Relevant Naming --------")

# Hyperparameters (model training settings)
learning_rate: float = 0.001 
batch_size: int = 32
num_epochs: int = 50
dropout_rate: float = 0.2

# Data info
num_training_samples: int = 60_000    # underscore separator — readable!
num_test_samples: int = 10_000
num_features: int = 128
num_layers: int = 6

# Flags
use_gpu: bool = True
is_training: bool = True
save_checkpoints: bool = False

# Uninitialized state
model_weights: None = None
training_loss: None = None

print(f"Learning rate: {learning_rate}")
print(f"Batch size: {batch_size}")
print(f"Training samples: {num_training_samples:,}")   # comma formatting
print(f"Using GPU: {use_gpu}")
print(f"Model weights loaded: {model_weights is not None}")

