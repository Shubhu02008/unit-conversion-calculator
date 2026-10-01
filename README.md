# Unit Converter

A command-line unit converter written in Python. It converts between units across 8 categories and runs in any terminal.

## Features

- 8 categories: length, weight, temperature, volume, area, speed, time, and data
- Choose a category by number or by name (`3` or `temperature`)
- Type the value and unit together, with or without a space: `700kg`, `700 kg`, `5 gallons`
- Full unit names work too, like `centimeters`, `fahrenheit`, `miles per hour`
- Checks your input and tells you when a unit doesn't belong to the chosen category
- Easy to extend: a new ratio-based category needs only a dictionary of units

## How to run

You need Python 3. No extra libraries are required.

    python unit_converter.py

## Example

    Choose: volume
    Use units: ml, l, m3, tsp, tbsp, floz, cup, pt, qt, gal
    Value: 5 gallons
    To: l
    5 gal = 18.9271 l

## How it works

Length, weight, and similar units are stored in a dictionary relative to one base unit, so every conversion goes through that base. Temperature uses its own formulas, since it isn't a simple ratio.

## What I practiced

Dictionaries, functions, loops, input validation, and string handling.