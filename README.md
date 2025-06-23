# Python Programming Concepts Project

This repository is a comprehensive collection of Python scripts and modules designed to demonstrate and practice core programming concepts, including control flow, functions, data structures, object-oriented programming (OOP), and different programming paradigms. The project is organized into thematic directories, each focusing on a specific area of Python programming.

## Table of Contents
- [Project Structure](#project-structure)
- [Directory Overviews](#directory-overviews)
  - [python_introduction](#python_introduction)
  - [control-flow](#control-flow)
  - [fns_and_dsa](#fns_and_dsa)
  - [oop](#oop)
  - [programming_paradigm](#programming_paradigm)
- [How to Run](#how-to-run)
- [Contributing](#contributing)

---

## Project Structure

```
.
├── python_introduction/
├── control-flow/
├── fns_and_dsa/
├── oop/
└── programming_paradigm/
```

## Directory Overviews

### python_introduction
Basic Python scripts for beginners, covering fundamental operations and calculations:
- **basic_operations.py**: Demonstrates addition, subtraction, and multiplication.
- **future_age_calculator.py**: Calculates your age in the year 2050.
- **hours_to_seconds.py**: Converts hours to seconds.
- **rectangle_area.py**: Computes the area of a rectangle.
- **simple_interest.py**: Calculates simple interest for a given principal, rate, and time.

### control-flow
Scripts focusing on control flow statements, user input, and decision making:
- **daily_reminder.py**: Task reminder with priority and time-bound logic using `match` statements.
- **match_case_calculator.py**: Simple calculator using Python's `match` statement for operation selection.
- **multiplication_table.py**: Prints a multiplication table.
- **pattern_drawing.py**: Draws patterns using loops.
- **weather_advice.py**: Gives clothing advice based on weather input.

### fns_and_dsa
Explores functions and basic data structures/algorithms:
- **arithmetic_operations.py**: Performs arithmetic operations based on user input.
- **explore_datetime.py**: Displays current date/time and calculates future dates.
- **shopping_list_manager.py**: Manages a shopping list interactively.
- **temp_conversion_tool.py**: Converts temperatures between Celsius and Fahrenheit.

### oop
Object-Oriented Programming concepts and examples:
- **book_class.py**: Defines a `Book` class with string representation and cleanup.
- **class_static_methods_demo.py**: Demonstrates static and class methods in a `Calculator` class.
- **library_system.py**: Models a library system with books and print books using inheritance.
- **polymorphism_demo.py**: Shows polymorphism with a `Shape` base class and a `Rectangle` subclass.

### programming_paradigm
Demonstrates different programming paradigms and robust coding practices:
- **bank_account.py**: Implements a simple `BankAccount` class with deposit, withdraw, and balance display methods.
- **library_management.py**: Models a library with book checkout/return and availability tracking.
- **main.py**: Entry point for a command-line bank account manager. Usage: `python main.py <command>:<amount>` (commands: deposit, withdraw, display).
- **robust_division_calculator.py**: Safe division function handling errors gracefully.
- **test_simple_calculator.py**: Unit tests for a simple calculator class (requires `simple_calculator.py`).

## How to Run

Most scripts can be run directly with Python 3:
```bash
python path/to/script.py
```
Some scripts require user input from the terminal. For example, to use the bank account manager:
```bash
cd programming_paradigm
python main.py deposit:100
python main.py withdraw:50
python main.py display
```

## Contributing
Contributions are welcome! Please fork the repository and submit a pull request for review.