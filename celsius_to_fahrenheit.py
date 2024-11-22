def celsius_to_fahrenheit(celsius):

    
    fahrenheit = (9 / 5) * celsius + 32
    return fahrenheit

temperature_celsius = float(input("Enter the temperature in Celsius: "))
temperature_fahrenheit = celsius_to_fahrenheit(temperature_celsius)
print(f"{temperature_celsius}°C is equal to {temperature_fahrenheit}°F.")
