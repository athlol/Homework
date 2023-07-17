def convert_temperature(temp, unit):
    if unit == "C":
        fahrenheit = (temp * 9/5) + 32
        return fahrenheit
    elif unit == "F":
        celsius = (temp - 32) * 5/9
        return celsius
    else:
        return "Invalid unit entered"

temp = float(input("Enter the temperature value: "))
unit = input("Enter the temperature unit (C for Celsius, F for Fahrenheit): ")

converted_temp = convert_temperature(temp, unit)
if isinstance(converted_temp, str):
    print(converted_temp)
else:
    print("The converted temperature is:", converted_temp)
