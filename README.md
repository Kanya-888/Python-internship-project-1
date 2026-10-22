# Python-internship-project-1
# Interactive Calculator & Unit Converter

A menu-driven command-line program in Python that does basic arithmetic and unit conversions. It keeps running until the user chooses to quit.

Built as Project 1 of my Python Programming virtual internship at InternCircle.

## Features

- Basic arithmetic: addition, subtraction, multiplication, division
- Unit conversions:
  - Kilometres to miles
  - Celsius to Fahrenheit
  - Kilograms to pounds
- Input validation: letters, empty input and invalid menu choices are handled without crashing
- Division by zero shows a clear message instead of an error
- Conversion factors are stored in one dictionary, so they are easy to change

## Requirements

- Python 3.10 or newer

Check your version:

```
python --version
```

## How to Run

1. Download or clone this repository.
2. Open a terminal in the project folder.
3. Run:

```
python calculator.py
```

## Sample Run

```
1) Add  2) Subtract  3) Multiply  4) Divide  5) Convert units  6) Quit
Choose an option: 1
First number: 12
Second number: 3.5
Result: 15.5
```

## Project Structure

```
calculator.py   # main program
README.md       # project documentation
```

## How It Works

- `read_number()` keeps asking until the user enters a valid number, using `try/except`.
- Each operation and conversion has its own function.
- `main()` shows the menu in a `while True` loop and exits only when the user picks Quit.

## Testing

I tested the program with these inputs:

| Input | Expected result |
|---|---|
| Letters instead of a number | Friendly error message, asks again |
| Empty input | Friendly error message, asks again |
| Negative numbers | Calculated correctly |
| Divide by zero | "Cannot divide by zero." |
| Invalid menu choice (e.g. 9) | "Please pick a number from 1 to 6." |
| Decimal numbers (e.g. 3.5) | Calculated correctly |

## What I Learned

- Reading input and converting it to numbers
- Writing functions that each do one job
- Using `if/elif` and `while` loops
- Handling bad input without crashing

## Author

Palvadi Kanya Kusuma Priya
InternCircle Python Programming Internship
