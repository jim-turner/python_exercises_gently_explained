
def convertToFahrenheit(degreesCelsius):
    return degreesCelsius * (9 / 5) + 32

def convertToCelsius(degreesFahrenheit):
    return (degreesFahrenheit - 32) * (5 / 9)

# 1. Get input and convert to float
degreesFahrenheit = float(input("What is your temperature in Fahrenheit? "))

# 2. Pass number to function
result = convertToCelsius(degreesFahrenheit)

# 3. Print result safely
print(f"This is your temperature converted to Celsius: {result: 1f}")

print(f"{result:.1f}")
