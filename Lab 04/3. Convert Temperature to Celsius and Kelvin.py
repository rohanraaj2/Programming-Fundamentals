def convert_fahrenheit_to_celsius(F):
 C = round((((F - 32) / 1.8)), 2)
 return C
def convert_celsius_to_kelvin(x):
 K = round((x + 273.15), 2)
 return K
def convert_temp(F):
 a = convert_fahrenheit_to_celsius (F)
 print("The temperature in Celsius is:", a)
 print("The temperature in Kelvin is:", convert_celsius_to_kelvin(a))
