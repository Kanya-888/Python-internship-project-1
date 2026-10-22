
# Project 1: Interactive Calculator and Unit Converter
# Python Programming Internship

# Store all conversion factors in one place
CONVERSION_FACTORS = {
    "km_to_miles": 0.621371,
    "kg_to_pounds": 2.20462
}


# Read a number safely and keep asking until valid input is entered
def read_number(prompt):
    while True:
        try:
            value = input(prompt).strip()

            if value == "":
                print("Input cannot be empty. Please enter a number.")
                continue

            return float(value)

        except ValueError:
            print("Invalid input! Please enter a valid number.")


# Arithmetic functions
def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return "Cannot divide by zero."
    return a / b


# Unit conversion functions
def km_to_miles(km):
    return km * CONVERSION_FACTORS["km_to_miles"]


def celsius_to_fahrenheit(celsius):
    return celsius * 9 / 5 + 32


def kg_to_pounds(kg):
    return kg * CONVERSION_FACTORS["kg_to_pounds"]


# Display the unit conversion menu
def convert_units():
    while True:
        print("\n--- Unit Converter ---")
        print("1. Kilometres to Miles")
        print("2. Celsius to Fahrenheit")
        print("3. Kilograms to Pounds")
        print("4. Back to Main Menu")

        choice = input("Choose a conversion (1-4): ").strip()

        if choice == "1":
            km = read_number("Enter distance in kilometres: ")
            print(f"{km} km = {km_to_miles(km):.4f} miles")

        elif choice == "2":
            celsius = read_number("Enter temperature in Celsius: ")
            fahrenheit = celsius_to_fahrenheit(celsius)
            print(f"{celsius} C = {fahrenheit:.2f} F")

        elif choice == "3":
            kg = read_number("Enter weight in kilograms: ")
            pounds = kg_to_pounds(kg)
            print(f"{kg} kg = {pounds:.4f} pounds")

        elif choice == "4":
            return

        else:
            print("Invalid choice! Please select an option from 1 to 4.")


# Main menu of the program
def main():
    while True:
        print("\n===== INTERACTIVE CALCULATOR =====")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Convert Units")
        print("6. Quit")

        choice = input("Choose an option (1-6): ").strip()

        if choice == "6":
            print("Thank you for using the calculator. Goodbye!")
            break

        elif choice in ("1", "2", "3", "4"):
            a = read_number("Enter the first number: ")
            b = read_number("Enter the second number: ")

            if choice == "1":
                result = add(a, b)
            elif choice == "2":
                result = subtract(a, b)
            elif choice == "3":
                result = multiply(a, b)
            else:
                result = divide(a, b)

            print("Result:", result)

        elif choice == "5":
            convert_units()

        else:
            print("Invalid choice! Please select a number from 1 to 6.")


# Start the program
if __name__ == "__main__":
    main()
