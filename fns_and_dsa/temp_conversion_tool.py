FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

def convert_to_celsius(fahrenheit):
    """Convert °F to °C."""
    global FAHRENHEIT_TO_CELSIUS_FACTOR
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    """Convert °C to °F."""
    global CELSIUS_TO_FAHRENHEIT_FACTOR
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

def main():
    """Run the temperature conversion tool."""
    try:
        temp_input = input("Enter the temperature to convert: ")
        temperature = float(temp_input)
    except ValueError:
        print("Invalid temperature. Please enter a numeric value.")
        return

    unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()
    if unit == 'C':
        print(f"{temperature}°C is {convert_to_fahrenheit(temperature)}°F")
    elif unit == 'F':
        print(f"{temperature}°F is {convert_to_celsius(temperature)}°C")
    else:
        print("Invalid unit. Please enter C or F.")

if __name__ == "__main__":
    main()