# 📚 Phase 1: Python Fundamentals - Week 1

**Week 1 Goal:** Understand variables, data types, and how Python stores information

**Duration:** May 14-20, 2026
**Time Commitment:** 1-1.5 hours/day (ideal: 5-6 days)

---

## 📖 What You'll Learn This Week

1. **Variables** - How to store data
2. **Data Types** - Different kinds of information (strings, integers, floats, booleans)
3. **Type Conversion** - Converting between types
4. **Basic Operations** - Math and string operations

---

## 🎯 By Friday, You Should Be Able To:

✅ Create variables and assign values
✅ Understand different data types
✅ Convert between types
✅ Do basic math operations
✅ Combine strings together

---

## 📅 Daily Breakdown

### **Monday: Variables & Data Types Basics**

**What you'll learn (45 min):**

Python stores information in **variables**. Think of them as labeled boxes:

```python
name = "Alice"          # Box labeled "name" contains "Alice"
age = 25               # Box labeled "age" contains 25
height = 5.6           # Box labeled "height" contains 5.6
is_student = True      # Box labeled "is_student" contains True
```

**Data Types:**
- **String** (`"text"`) - Text data
- **Integer** (`42`) - Whole numbers
- **Float** (`3.14`) - Decimal numbers
- **Boolean** (`True`/`False`) - Yes/No values

**Practice (45 min):**

Create a file: `python-basics/01-variables/day-1-variables.py`

```python
# Monday Practice: Variables & Data Types

# Create variables with different data types
name = "Your Name"
age = 0
height = 0.0
is_learning = True

# Print them out
print(f"Name: {name}")
print(f"Age: {age}")
print(f"Height: {height}")
print(f"Currently learning: {is_learning}")

# Now update them with YOUR info
name = "blaNq"
age = 25  # Replace with your age
height = 5.8  # Replace with your height
is_learning = True

# Print again
print("\n--- Updated Info ---")
print(f"Name: {name}")
print(f"Age: {age}")
print(f"Height: {height}")
print(f"Currently learning: {is_learning}")
```

**Run it:**
```bash
python3 python-basics/01-variables/day-1-variables.py
```

**Commit it:**
```bash
cd ~/coding-journey
git add python-basics/01-variables/day-1-variables.py
git commit -m "Day 1: Learn variables and data types"
git push
```

---

### **Tuesday: Practice & Type Conversion**

**What you'll learn (45 min):**

Sometimes you need to convert data from one type to another:

```python
# String to Integer
age_text = "25"
age_number = int(age_text)  # Now it's 25 (number), not "25" (text)

# Integer to String
number = 42
text = str(number)  # Now it's "42" (text)

# String to Float
height_text = "5.8"
height_number = float(height_text)  # Now it's 5.8 (decimal)
```

**Why?** Because you can do math with numbers, but not with text strings!

```python
age = "25"
next_year = age + 1  # ERROR! Can't add text + number

age = int("25")
next_year = age + 1  # Works! Result: 26
```

**Practice (45 min):**

Create a file: `python-basics/01-variables/day-2-conversion.py`

```python
# Tuesday Practice: Type Conversion

# Get user input (remember: input() always returns STRING)
name = input("What's your name? : ")
age_text = input("How old are you? : ")
height_text = input("What's your height (in feet)? : ")

# Convert to numbers
age = int(age_text)
height = float(height_text)

# Do some math
next_year_age = age + 1
double_height = height * 2

# Print results
print(f"\n--- Your Info ---")
print(f"Name: {name}")
print(f"Current age: {age}")
print(f"Next year you'll be: {next_year_age}")
print(f"Your height: {height} feet")
print(f"Double your height: {double_height} feet")

# Challenge: Calculate age in months
age_in_months = age * 12
print(f"\nYou are approximately {age_in_months} months old!")
```

**Run it:**
```bash
python3 python-basics/01-variables/day-2-conversion.py
```

**Commit it:**
```bash
git add python-basics/01-variables/day-2-conversion.py
git commit -m "Day 2: Learn type conversion (int, float, str)"
git push
```

---

### **Wednesday: Math & String Operations**

**What you'll learn (45 min):**

**Math operations with numbers:**
```python
x = 10
y = 3

addition = x + y        # 13
subtraction = x - y     # 7
multiplication = x * y  # 30
division = x / y        # 3.333...
floor_division = x // y # 3 (rounds down)
modulo = x % y          # 1 (remainder)
power = x ** y          # 1000 (10 to the power of 3)
```

**String operations:**
```python
first_name = "John"
last_name = "Doe"

full_name = first_name + " " + last_name  # "John Doe"
repeated = "Ha" * 3                        # "HaHaHa"
```

**Practice (45 min):**

Create a file: `python-basics/01-variables/day-3-operations.py`

```python
# Wednesday Practice: Math & String Operations

print("=== MATH OPERATIONS ===")

num1 = 15
num2 = 4

print(f"{num1} + {num2} = {num1 + num2}")
print(f"{num1} - {num2} = {num1 - num2}")
print(f"{num1} * {num2} = {num1 * num2}")
print(f"{num1} / {num2} = {num1 / num2}")
print(f"{num1} // {num2} = {num1 // num2}")
print(f"{num1} % {num2} = {num1 % num2}")
print(f"{num1} ** {num2} = {num1 ** num2}")

print("\n=== STRING OPERATIONS ===")

first = "Python"
second = "Rocks"

combined = first + " " + second
print(f"Combined: {combined}")
print(f"Repeated: {'Coding! ' * 3}")

print("\n=== CHALLENGE ===")

# Get two numbers from user
num_a = int(input("Give me a number: "))
num_b = int(input("Give me another number: "))

# Calculate and display
print(f"\n{num_a} + {num_b} = {num_a + num_b}")
print(f"{num_a} * {num_b} = {num_a * num_b}")
print(f"{num_a} / {num_b} = {num_a / num_b}")
print(f"{num_a} % {num_b} = {num_a % num_b}")
```

**Run it:**
```bash
python3 python-basics/01-variables/day-3-operations.py
```

**Commit it:**
```bash
git add python-basics/01-variables/day-3-operations.py
git commit -m "Day 3: Learn math and string operations"
git push
```

---

### **Thursday: Review & Consolidate**

**What to do (1.5 hours):**

1. **Review** (30 min)
   - Re-read Monday's material
   - Run Monday-Wednesday's code again
   - Write down anything you don't understand

2. **Practice** (45 min)

Create a file: `python-basics/01-variables/day-4-review.py`

```python
# Thursday: Review all Week 1 concepts

print("=== WEEK 1 REVIEW ===\n")

# TASK 1: Create variables and display them
book_title = "Python for Beginners"
num_chapters = 20
avg_pages_per_chapter = 25.5
is_finished = False

print("TASK 1: Book Info")
print(f"Title: {book_title}")
print(f"Chapters: {num_chapters}")
print(f"Avg pages per chapter: {avg_pages_per_chapter}")
print(f"Is finished? {is_finished}")

# TASK 2: Type conversion
print("\nTASK 2: Type Conversion")
total_pages = int(num_chapters * avg_pages_per_chapter)
print(f"Total pages (approx): {total_pages}")

# TASK 3: Math operations
print("\nTASK 3: Math Operations")
pages_read_per_day = 10
days_to_finish = total_pages / pages_read_per_day
print(f"If you read {pages_read_per_day} pages/day, finish in {days_to_finish} days")

# TASK 4: String operations
print("\nTASK 4: String Combinations")
author_first = "John"
author_last = "Smith"
full_name = author_first + " " + author_last
print(f"Author: {full_name}")

# TASK 5: User interaction
print("\nTASK 5: Interactive")
your_name = input("What's your name? : ")
favorite_number = int(input("What's your favorite number? : "))
lucky_number = favorite_number * 7
print(f"{your_name}, your lucky number is {lucky_number}!")
```

**Run it and review:**
```bash
python3 python-basics/01-variables/day-4-review.py
```

**Commit it:**
```bash
git add python-basics/01-variables/day-4-review.py
git commit -m "Day 4: Review all variables and operations concepts"
git push
```

---

### **Friday: Mini Challenge & Commit**

**Challenge (1.5 hours):**

Create a file: `python-basics/01-variables/day-5-challenge.py`

```python
# Friday Mini-Challenge: Build a Simple Profile Creator

print("=== PROFILE CREATOR ===\n")

# Get user information
name = input("What's your name? : ")
age = int(input("How old are you? : "))
city = input("What city are you in? : ")
hobby = input("What's your favorite hobby? : ")

# Calculate some interesting facts
birth_decade = (age // 10) * 10
next_milestone_age = ((age // 10) + 1) * 10
years_to_milestone = next_milestone_age - age

# Create a fun profile
print("\n" + "="*50)
print(f"✨ PROFILE: {name.upper()} ✨")
print("="*50)
print(f"Age: {age} years old")
print(f"Location: {city}")
print(f"Hobby: {hobby}")
print(f"\nFun facts:")
print(f"  - Born in the {birth_decade}s")
print(f"  - {years_to_milestone} years until age {next_milestone_age}!")
print(f"  - That's {age * 365} days of life!")
print("="*50)
```

**Run it:**
```bash
python3 python-basics/01-variables/day-5-challenge.py
```

**Test it a few times with different inputs!**

**Commit it:**
```bash
git add python-basics/01-variables/day-5-challenge.py
git commit -m "Day 5: Mini-challenge - Profile Creator"
git push
```

---

## 🎯 Week 1 Checklist

- [ ] Completed Day 1 (Variables)
- [ ] Completed Day 2 (Type Conversion)
- [ ] Completed Day 3 (Operations)
- [ ] Completed Day 4 (Review)
- [ ] Completed Day 5 (Challenge)
- [ ] All files committed to GitHub
- [ ] Updated PROGRESS.md with checkmarks

---

## 📝 Notes & Reflection

**After this week, answer these:**

1. What was the easiest concept this week?
2. What was confusing? (Write it down to review!)
3. Did you enjoy any of the exercises?

---

## 🚀 Next Week Preview

**Week 2:** Input & Output Deep Dive
- More about `input()` and `print()`
- String formatting
- Creating interactive programs

---

**You've got this!** 💪 Once you're done with this week, move on to Week 2!
