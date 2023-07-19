"""
convert_to_celsius: It takes a temperature in Fahrenheit as input and returns the temperature in Celsius
fahrenheit - input temperature in fahrenheit
return - Temperature in Celsius
"""
def convert_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5 / 9
    return celsius
