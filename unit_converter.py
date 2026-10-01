LENGTH = {
    "mm": 0.001,
    "cm": 0.01,
    "m": 1,
    "km": 1000,
    "in": 0.0254,
    "ft": 0.3048,
    "mi": 1609.344,
}

WEIGHT = {
    "g": 1,
    "kg": 1000,
    "oz": 28.3495,
    "lb": 453.592,
}

VOLUME = {
    "ml": 0.001,
    "l": 1,
    "m3": 1000,
    "tsp": 0.00492892,
    "tbsp": 0.0147868,
    "floz": 0.0295735,
    "cup": 0.236588,
    "pt": 0.473176,
    "qt": 0.946353,
    "gal": 3.78541,
}

AREA = {
    "cm2": 0.0001,
    "m2": 1,
    "km2": 1000000,
    "ha": 10000,
    "in2": 0.00064516,
    "ft2": 0.09290304,
    "yd2": 0.83612736,
    "ac": 4046.8564224,
    "mi2": 2589988.110336,
}

SPEED = {
    "m/s": 1,
    "km/h": 1000 / 3600,
    "mph": 0.44704,
    "kn": 0.514444,
    "ft/s": 0.3048,
}

TIME = {
    "ms": 0.001,
    "s": 1,
    "min": 60,
    "h": 3600,
    "d": 86400,
    "wk": 604800,
    "yr": 31557600,
}

DATA = {
    "bit": 0.125,
    "b": 1,
    "kb": 1024,
    "mb": 1024 ** 2,
    "gb": 1024 ** 3,
    "tb": 1024 ** 4,
}

TEMPERATURE = ("c", "f", "k")

CATEGORIES = [
    "length", "weight", "temperature", "volume",
    "area", "speed", "time", "data",
]

TABLES = {
    "length": LENGTH,
    "weight": WEIGHT,
    "volume": VOLUME,
    "area": AREA,
    "speed": SPEED,
    "time": TIME,
    "data": DATA,
}

ALIASES = {
    "millimeter": "mm", "millimeters": "mm",
    "centimeter": "cm", "centimeters": "cm",
    "meter": "m", "meters": "m",
    "kilometer": "km", "kilometers": "km",
    "inch": "in", "inches": "in",
    "foot": "ft", "feet": "ft",
    "mile": "mi", "miles": "mi",
    "gram": "g", "grams": "g",
    "kilogram": "kg", "kilograms": "kg",
    "ounce": "oz", "ounces": "oz",
    "pound": "lb", "pounds": "lb",
    "celsius": "c", "fahrenheit": "f", "kelvin": "k",
    "milliliter": "ml", "milliliters": "ml",
    "liter": "l", "liters": "l", "litre": "l", "litres": "l",
    "cubic meter": "m3", "cubic meters": "m3",
    "teaspoon": "tsp", "teaspoons": "tsp",
    "tablespoon": "tbsp", "tablespoons": "tbsp",
    "fl oz": "floz", "fluid ounce": "floz", "fluid ounces": "floz",
    "cups": "cup",
    "pint": "pt", "pints": "pt",
    "quart": "qt", "quarts": "qt",
    "gallon": "gal", "gallons": "gal",
    "square centimeter": "cm2", "square centimeters": "cm2",
    "square meter": "m2", "square meters": "m2", "sq m": "m2",
    "square kilometer": "km2", "square kilometers": "km2",
    "hectare": "ha", "hectares": "ha",
    "square inch": "in2", "square inches": "in2",
    "square foot": "ft2", "square feet": "ft2", "sq ft": "ft2",
    "square yard": "yd2", "square yards": "yd2",
    "acre": "ac", "acres": "ac",
    "square mile": "mi2", "square miles": "mi2",
    "kmh": "km/h", "kph": "km/h",
    "kilometers per hour": "km/h",
    "miles per hour": "mph",
    "meters per second": "m/s", "mps": "m/s",
    "feet per second": "ft/s",
    "knot": "kn", "knots": "kn",
    "millisecond": "ms", "milliseconds": "ms",
    "second": "s", "seconds": "s", "sec": "s", "secs": "s",
    "minute": "min", "minutes": "min", "mins": "min",
    "hour": "h", "hours": "h", "hr": "h", "hrs": "h",
    "day": "d", "days": "d",
    "week": "wk", "weeks": "wk",
    "year": "yr", "years": "yr",
    "bits": "bit",
    "byte": "b", "bytes": "b",
    "kilobyte": "kb", "kilobytes": "kb",
    "megabyte": "mb", "megabytes": "mb",
    "gigabyte": "gb", "gigabytes": "gb",
    "terabyte": "tb", "terabytes": "tb",
}


def get_unit(text):
    text = text.strip().lower()
    return ALIASES.get(text, text)


def units_text(valid_units):
    if valid_units == TEMPERATURE:
        return "Use units: Celsius (C), Fahrenheit (F), Kelvin (K)"
    return "Use units: " + ", ".join(valid_units)


def format_number(number):
    if number != 0 and (abs(number) < 0.0001 or abs(number) >= 1e12):
        return f"{number:.4e}"
    return f"{number:.4f}".rstrip("0").rstrip(".")


def convert_with_table(value, from_unit, to_unit, table):
    base = value * table[from_unit]
    return base / table[to_unit]


def convert_temperature(value, from_unit, to_unit):
    if from_unit == "f":
        celsius = (value - 32) * 5 / 9
    elif from_unit == "k":
        celsius = value - 273.15
    else:
        celsius = value

    if to_unit == "f":
        return celsius * 9 / 5 + 32
    elif to_unit == "k":
        return celsius + 273.15
    return celsius


def ask_unit(prompt, valid_units, category):
    while True:
        typed = input(prompt).strip()
        unit = get_unit(typed)
        if unit in valid_units:
            return unit
        print(f"{typed} is not a valid unit for {category}.")
        print(units_text(valid_units))


def ask_value_and_units(valid_units, category):
    print(units_text(valid_units))

    while True:
        text = input("Value: ").strip().lower()

        i = 0
        while i < len(text) and (text[i].isdigit() or text[i] in ".-"):
            i += 1

        try:
            value = float(text[:i])
        except ValueError:
            print("Please enter a number.")
            continue

        unit_text = text[i:].strip()

        if unit_text == "":
            from_u = ask_unit("From: ", valid_units, category)
            break

        from_u = get_unit(unit_text)
        if from_u in valid_units:
            break
        print(f"{unit_text} is not a valid unit for {category}.")
        print(units_text(valid_units))

    to_u = ask_unit("To: ", valid_units, category)
    return value, from_u, to_u


def main():
    print("=== Unit Converter ===")

    names = {}
    for number, name in enumerate(CATEGORIES, 1):
        names[name] = str(number)
    quit_choice = str(len(CATEGORIES) + 1)
    names["quit"] = quit_choice

    while True:
        print()
        for number, name in enumerate(CATEGORIES, 1):
            print(f"{number}) {name.title()}")
        print(f"{quit_choice}) Quit")

        choice = input("Choose: ").strip().lower()
        choice = names.get(choice, choice)

        if choice == quit_choice:
            print("Bye!")
            break

        if not choice.isdigit() or not 1 <= int(choice) <= len(CATEGORIES):
            print(f"Please pick 1-{quit_choice}.")
            continue

        category = CATEGORIES[int(choice) - 1]

        if category == "temperature":
            value, from_u, to_u = ask_value_and_units(TEMPERATURE, category)
            result = convert_temperature(value, from_u, to_u)
            print(f"{format_number(value)} {from_u.upper()} = {format_number(result)} {to_u.upper()}")
        else:
            table = TABLES[category]
            value, from_u, to_u = ask_value_and_units(table, category)
            result = convert_with_table(value, from_u, to_u, table)
            print(f"{format_number(value)} {from_u} = {format_number(result)} {to_u}")


main()
