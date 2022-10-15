# __Learning Objectives__
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

## General
- [x] Why Python programming is awesome
- [x] What is OOP
- [x] “first-class everything”
- [x] What is a class
- [x] What is an object and an instance
- [x] What is the difference between a class and an object or instance
- [x] What is an attribute
- [x] What are and how to use public, protected and private attributes
- [x] What is self
- [x] What is a method
- [x] What is the special __init__ method and how to use it
- [x] What is Data Abstraction, Data Encapsulation, and Information Hiding
- [x] What is a property
- [x] What is the difference between an attribute and a property in Python
- [x] What is the Pythonic way to write getters and setters in Python
- [x] How to dynamically create arbitrary new attributes for existing instances of a class
- [x] How to bind attributes to object and classes
- [x] What is the __dict__ of a class and/or instance of a class and what does it contain
- [x] How does Python find the attributes of an object or class
- [x] How to use the getattr function

### General

#### Allowed editors: vi, vim, emacs
* All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
* All your files should end with a new line
* The first line of all your files should be exactly #!/usr/bin/python3
* A README.md file, at the root of the folder of the project, is mandatory
* Your code should use the pycodestyle (version 2.8.*)
* All your files must be executable
* The length of your files will be tested using wc
* All your modules should have a documentation (python3 -c 'print(__import__("my_module").__doc__)')
* All your classes should have a documentation (python3 -c 'print(__import__("my_module").MyClass.__doc__)')
* All your functions (inside and outside a class) should have a documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)')
* A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)

# __Tasks__
## __0. My first square__
__0-square.py__
Write an empty class Square that defines a square:

* You are not allowed to import any module
## __1. Square with size__
__1-square.py
Write a class Square that defines a square by: (based on 0-square.py)

* Private instance attribute: size
* Instantiation with size (no type/value verification)
* You are not allowed to import any module
* Why?

__Why size is private attribute?__

The size of a square is crucial for a square, many things depend of it (area computation, etc.), so you, as class builder, must control the type and value of this attribute. One way to have the control is to keep it privately. You will see in next tasks how to get, update and validate the size value.

## __2. Size validation__

Write a class Square that defines a square by: (based on 1-square.py)

* Private instance attribute: size
* Instantiation with optional size: def __init__(self, size=0):
* size must be an integer, otherwise raise a TypeError exception with the message size must be an integer
* if size is less than 0, raise a ValueError exception with the message size must be >= 0
* You are not allowed to import any module