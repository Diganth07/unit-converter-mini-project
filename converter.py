"""Conversion logic for the unit converter application."""

UNITS = {
    "Length": {
        "Meter": 1,
        "Kilometer": 1000,
        "Centimeter": 0.01,
        "Millimeter": 0.001,
        "Mile": 1609.344,
        "Yard": 0.9144,
        "Foot": 0.3048,
        "Inch": 0.0254,
    },
    "Weight": {
        "Kilogram": 1,
        "Gram": 0.001,
        "Milligram": 0.000001,
        "Pound": 0.45359237,
        "Ounce": 0.028349523125,
    },
    "Volume": {
        "Liter": 1,
        "Milliliter": 0.001,
        "Cubic meter": 1000,
        "Gallon (US)": 3.785411784,
        "Cup (US)": 0.2365882365,
        "Pint (US)": 0.473176473,
    },
}

TEMPERATURE_UNITS = ("Celsius", "Fahrenheit", "Kelvin")


def convert(value: float, category: str, source: str, target: str) -> float:
    """Convert a numeric value between two units in a category."""
    if category == "Temperature":
        celsius = {
            "Celsius": value,
            "Fahrenheit": (value - 32) * 5 / 9,
            "Kelvin": value - 273.15,
        }[source]
        return {
            "Celsius": celsius,
            "Fahrenheit": celsius * 9 / 5 + 32,
            "Kelvin": celsius + 273.15,
        }[target]

    units = UNITS[category]
    return value * units[source] / units[target]
