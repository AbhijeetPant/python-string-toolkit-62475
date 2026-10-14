## 1. Introduction to Python Strings

A **string** is a sequence of characters used to represent text. In Python, strings are written inside single quotes or double quotes.

```python
name = "Python"
message = 'Hello World'
```

Strings can contain letters, digits, spaces, punctuation and other characters.

### 1.1 Accessing characters

Each character in a string has a position called an index. Python uses zero-based indexing.

```python
text = "Python"

print(text[0])   # P
print(text[1])   # y
print(text[-1])  # n
```

### 1.2 String length

The `len()` function returns the number of characters in a string.

```python
text = "Python"
print(len(text))  # 6
```

Spaces and punctuation also count as characters.

### 1.3 String methods

Python provides several built-in methods for working with strings.

```python
text = "Hello World"

print(text.lower())       # hello world
print(text.upper())       # HELLO WORLD
print(text.replace("o", "0"))  # Hell0 W0rld
print(text.split())       # ['Hello', 'World']
```

### 1.4 Traversing a string using a loop

A string can be processed one character at a time.

```python
text = "Python"

for ch in text:
    print(ch)
```

### 1.5 Using conditions

Conditions allow us to perform operations only when a particular requirement is satisfied.

```python
text = "Python"
count = 0

for ch in text.lower():
    if ch in "aeiou":
        count += 1

print(count)  # 1
```

This program counts vowels in a string. Similar logic can be used to count digits, spaces, uppercase letters and many other character types.

### 1.6 String indexing and slicing

Slicing extracts part of a string.

```python
text = "Python"

print(text[0:3])  # Pyt
print(text[2:])   # thon
print(text[::-1]) # nohtyP
```

Strings are immutable, which means individual characters cannot be changed directly. Operations such as replacement produce a new string.

These basic operations are sufficient for the functions assigned in this activity.

---

## 2. Activity: Build the String Toolkit

Each student has been assigned a unique function in the assignment list.

Examples of assigned functions include:

- `count_vowels(text)`
- `reverse_text(text)`
- `count_words(text)`
- `remove_vowels(text)`
- `is_palindrome(text)`
- `character_frequency(text)`

**You must implement the function assigned to you. Do not implement a different function.**

### What you must do

1. Find your student ID and assigned function in the assignment list.
2. Understand the function's purpose and expected output.
3. Write the function using Python.
4. Submit your code through GitHub using a pull request.
5. Review the assigned classmate's contribution.

### Important rules

- Use basic Python only. Do not use external libraries.
- Follow the exact function name and parameters specified in your assignment.
- Follow the input/output examples and rules.
- Include meaningful variable names and appropriate indentation.
- Your submission must contain a function definition, not just a sequence of print statements.
- Do not copy another student's implementation.
- Do not modify other students' files or shared integration files.
- Do not merge your own pull request into the original repository.

---

## 4. How to Write Your Function

Suppose your assigned function is `count_vowels(text)`.

Your task is to return the number of vowels in the supplied string.

Example implementation:

```python
def count_vowels(text):
    count = 0

    for ch in text.lower():
        if ch in "aeiou":
            count += 1

    return count
```

The function can be tested as follows:

```python
print(count_vowels("hello"))  # 2
print(count_vowels("rhythm")) # 0
print(count_vowels(""))       # 0
```

Notice that the function uses `return` to provide a result. The calling program can then print the result or use it in another computation.

You may use this example to understand the structure of a function, but you must write your own assigned function.

---


## 5. How to Contribute Using GitHub

You will contribute through a **fork and pull request**. You do not need direct write access to the original repository.

### Step 1: Fork the repository

1. Open the original Python String Toolkit repository.
2. Click **Fork**.
3. Select your own GitHub account as the destination.
4. Create the fork.

You now have your own copy of the repository.

### Step 2: Create a branch

Open your fork and create a new branch for this assignment.

Use a descriptive name, for example:

`activity1-s01-count-vowels`

Replace `s01` with your assigned student ID.

### Step 3: Add your Python file

Inside the `submissions/` folder, create the file assigned to you.

For example:

`submissions/s01.py`

Your file should contain the function definition and any necessary comments.

Do not edit the original repository directly.


### Step 4: Commit your changes

Commit your files to your branch with a meaningful message, such as:

`Add count_vowels function and tests`

### Step 5: Open a pull request

From your fork, open a pull request targeting the original repository.

Check that:

- **Base repository:** the instructor's original repository.
- **Base branch:** `main`.
- **Head repository:** your fork.
- **Compare branch:** your assignment branch.

Do not open a pull request targeting your own fork.

### Step 6: Describe your contribution

Include the following information in the pull request description:

- Your student ID.
- Your assigned function name.
- A brief explanation of what the function does.
- Confirmation that you tested your function.
- Any assumptions or limitations.

### Step 7: Respond to review feedback

Another student will review your contribution. If changes are requested, update your branch and push the corrections. The pull request will update automatically.

The instructor will review and merge accepted contributions into the original repository.

**Do not merge your own pull request.**

---

## 6. Pull Request Checklist

Before submitting, confirm every item below.

- [ ] I implemented my assigned function.
- [ ] My function name and parameters match the assignment.
- [ ] My code uses appropriate Python syntax and indentation.
- [ ] I tested at least three cases.
- [ ] I included my assigned `.py` file.
- [ ] My files are in the correct folders.
- [ ] I created a branch in my fork.
- [ ] My pull request targets the original repository's `main` branch.
- [ ] My pull request contains a clear description.
- [ ] I am ready to explain my code individually.

---

## 7. Peer Review

Each student will review one other student's contribution.

During the review, check:

1. Does the code solve the assigned problem?
2. Does the function return the correct output?
3. Are the variable names understandable?
4. Are the tests meaningful?
5. Is there an edge case that has not been tested?
6. Is the code readable and appropriately formatted?

A peer review is a learning activity. Be respectful and explain why you recommend a change rather than simply stating that the code is wrong.

---

## Final Outcome

Once the contributions are reviewed and merged, the class will have a shared collection of 54 Python string-processing functions.

This toolkit will serve as the starting point for future assignments. As we learn additional Python concepts, we will extend our collaborative library with more functions for data processing and, eventually, AI/ML workflows.

Remember: **you are responsible for your own function, but together we are responsible for building a reliable toolkit.**

Happy coding!
