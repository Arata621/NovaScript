![Version](https://img.shields.io/badge/version-1.0.0-blue)
![License](https://img.shields.io/badge/license-MIT-orange)
![For Education](https://img.shields.io/badge/For-Education-brightgreen)
![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-blue)
![Code Style: NovaScript](https://img.shields.io/badge/code%20style-NovaScript-blueviolet)

# NovaScript
## Table of Contents
1. Introduction
2. Language Overview
3. Getting Started
4. Syntax and Structure
5. Data Types
6. Variables and Constants
7. Operators and Expressions
8. Control Flow
9. Functions
10. Object-Oriented Programming (OOP)
11. Modules and Imports
12. File Handling
13. Error Handling
14. Debugging and Troubleshooting
15. Standard Library
16. Sample Projects
17. Best Practices
18. Frequently Asked Questions (FAQ)

---

## 1. Introduction
NovaScript is an educational programming language designed to help beginners grasp fundamental coding concepts before transitioning to languages like C, C++, C#, Python, or Java. Its clear syntax and minimal setup make it a great entry point for new programmers.

### Why NovaScript?
✅ Simple, readable syntax  
✅ Object-oriented programming support  
✅ File handling capabilities  
✅ Structured control flow statements  
✅ Built-in error handling  
✅ Interpreted execution  

---

## 2. Language Overview
NovaScript is:
- **Beginner-Friendly**: Designed for those new to coding.
- **Lightweight**: Requires only a simple interpreter.
- **Structured**: Supports functions, loops, and OOP.

It bridges the gap between visual programming (like Scratch) and text-based languages.

---

## 3. Getting Started
### Installation
1. Download the NovaScript interpreter.
2. Save NovaScript files with the `.nsc` extension.
3. Run scripts using:
   ```sh
   python novascript.py my_script.nsc
   ```

### Your First NovaScript Program
```nsc
print "Hello, World!"
```

---

## 4. Syntax and Structure
NovaScript is structured yet flexible.

### Statements
```nsc
x = 10
if x > 5
    print "x is greater than 5"
endif
```

---

## 5. Data Types
- Integer
- Float
- String
- Boolean
- Lists

Example:
```nsc
a = 5
b = "Hello"
c = True
d = [1, 2, 3]
```

---

## 6. Variables and Constants
```nsc
x = 100
const PI = 3.14
```

---

## 7. Operators and Expressions
### Arithmetic Operators
```nsc
+  - Addition
-  - Subtraction
*  - Multiplication
/  - Division
```

### Logical Operators
```nsc
and - Logical AND
or  - Logical OR
not - Logical NOT
```

---

## 8. Control Flow
### If-Else Statements
```nsc
if x > 5
    print "x is greater than 5"
else
    print "x is 5 or less"
endif
```

### Loops
```nsc
for i in 1 to 5
    print i
endfor
```

---

## 9. Functions
```nsc
def add(a, b)
    return a + b
enddef

print add(5, 3)
```

---

## 10. Object-Oriented Programming
```nsc
class Animal
    def speak()
        print "This animal speaks."
    enddef
endclass

new Animal as dog
dog.speak()
```

---

## 11. Modules and Imports
```nsc
import "mymodule.nsc"
```

---

## 12. File Handling
```nsc
writefile "example.txt", "Hello, NovaScript!"
readfile "example.txt"
```

---

## 13. Error Handling
```nsc
try
    x = 5 / 0
except
    print "An error occurred"
endtry
```

---

## 14. Debugging and Troubleshooting
- Use `print` statements for debugging.
- Check syntax errors.
- Verify function parameters.

---

## 15. Standard Library
NovaScript includes built-in functions for:
- String manipulation
- Mathematical operations
- List handling
- File processing

---

## 16. Sample Projects
### Basic Calculator
```nsc
def add(a, b)
    return a + b
enddef
print add(10, 5)
```

### Number Guessing Game
```nsc
secret = 7
guess = input "Guess a number: "
if guess == secret
    print "You guessed right!"
else
    print "Try again!"
endif
```

---

## 17. Best Practices
- Use meaningful variable names.
- Keep functions short and modular.
- Handle errors gracefully.
- Follow consistent indentation.

---

## 18. Frequently Asked Questions (FAQ)
### Q1: How do I install NovaScript?
**A:** Download the interpreter and run `.nsc` files using Python.

### Q2: Can I use NovaScript for real applications?
**A:** It's mainly for learning, but small projects are possible.

### Q3: Does NovaScript support graphics?
**A:** Future updates may include graphical capabilities.

---

**Happy Coding with NovaScript!**

