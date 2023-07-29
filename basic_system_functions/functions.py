from PIL import Image, ImageFilter

def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    if num2 != 0:
        return num1 / num2
    else:
        return None

def power(num1, num2):
    return num1 ** num2

def perform_calculation(num1, num2, operation):
    """Perform the selected calculation operation"""
    try:
        num1_value = float(num1)
        num2_value = float(num2)
    except ValueError:
        return None

    if operation == 'Add':
        return add(num1_value, num2_value)
    elif operation == 'Subtract':
        return subtract(num1_value, num2_value)
    elif operation == 'Multiply':
        return multiply(num1_value, num2_value)
    elif operation == 'Divide':
        return divide(num1_value, num2_value)
    elif operation == 'Power':
        return power(num1_value, num2_value)
    else:
        return None

def calculate_average(numbers):
    """Calculate the average of a list of numbers"""
    if numbers:
        return sum(numbers) / len(numbers)
    else:
        return None

def resize_image(image, width, height):
    """Resize the image"""
    return image.resize((width, height))

def crop_image(image, left, upper, right, lower):
    """Crop the image"""
    return image.crop((left, upper, right, lower))

def apply_filter(image, filter_type):
    """Apply the selected filter to the image"""
    if filter_type == 'Grayscale':
        return image.convert('L')
    elif filter_type == 'Blur':
        return image.filter(ImageFilter.BLUR)
    elif filter_type == 'Edge':
        return image.filter(ImageFilter.FIND_EDGES)
    elif filter_type == 'Sharpen':
        return image.filter(ImageFilter.SHARPEN)
    else:
        return image

def flip_image(image):
    """Flip the image horizontally"""
    return image.transpose(Image.FLIP_LEFT_RIGHT)

def convert_length(value, from_unit, to_unit):
    """Convert length between different units"""
    conversion_rates = {
        'cm': 1,
        'm': 0.01,
        'km': 0.00001,
        'inch': 0.393701,
        'ft': 0.0328084,
        'yd': 0.0109361,
        'mile': 0.00000621371
    }

    if from_unit in conversion_rates and to_unit in conversion_rates:
        return value * conversion_rates[from_unit] / conversion_rates[to_unit]

    return None  # Invalid conversion

def convert_weight(value, from_unit, to_unit):
    """Convert weight between different units"""
    conversion_rates = {
        'kg': 1,
        'g': 1000,
        'lb': 2.20462,
        'oz': 35.274
    }

    if from_unit in conversion_rates and to_unit in conversion_rates:
        return value * conversion_rates[from_unit] / conversion_rates[to_unit]

    return None  # Invalid conversion

def convert_temperature(value, from_unit, to_unit):
    """Convert temperature between Celsius, Fahrenheit, and Kelvin"""
    if from_unit == to_unit:
        return value

    if from_unit == 'Celsius':
        if to_unit == 'Fahrenheit':
            return (value * 9/5) + 32
        elif to_unit == 'Kelvin':
            return value + 273.15
    elif from_unit == 'Fahrenheit':
        if to_unit == 'Celsius':
            return (value - 32) * 5/9
        elif to_unit == 'Kelvin':
            return (value + 459.67) * 5/9
    elif from_unit == 'Kelvin':
        if to_unit == 'Celsius':
            return value - 273.15
        elif to_unit == 'Fahrenheit':
            return (value * 9/5) - 459.67

    return None  # Invalid conversion
