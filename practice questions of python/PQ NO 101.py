def celsius_to_fahrenheit(c):
    return c * 9 / 5 + 32

celsius = list(map(float, input("Enter Celsius values separated by space: ").split()))

fahrenheit = list(map(celsius_to_fahrenheit, celsius))

print("Fahrenheit Values:", fahrenheit)