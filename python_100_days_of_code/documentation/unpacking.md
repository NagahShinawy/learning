# Unpacking in Loops in Python

## Overview

Unpacking is a feature in Python that allows you to extract individual elements from a collection (like a list or tuple) and assign them to variables. This is especially useful in loops, where you want to work with multiple elements of a collection simultaneously.

This document explains unpacking in loops with examples and how it applies to real-world projects.

---

## How Unpacking Works

Consider the following code, where a list of tuples represents students and their total grades:

```python
students = [('Alice', 92), ('Bob', 85), ('Charlie', 78), ('David', 95), ('Eva', 66)]

for name, degree in students:
    print(f"Name is {name}")
    print(f"Degree is {degree}")
    print("#" * 10)

```

# How It Works:
`students` is a list of tuples where each tuple contains a student name and their grade.
The loop` for name, degree in students` extracts each tuple and assigns its first element to `name` and the second to `degree`.
This avoids accessing tuple elements by index (like `student[0]`, `student[1]`), making the code cleaner and more readable.

# Why Use Unpacking?
Unpacking improves code clarity and reduces complexity, especially when working with collections of tuples, dictionaries, or other iterable objects that contain multiple values.

## Benefits:
**Cleaner Code**: Instead of accessing elements by their index, you work directly with variable names.

**Better Readability**: Assigning meaningful names to variables makes the code easier to understand and maintain.

