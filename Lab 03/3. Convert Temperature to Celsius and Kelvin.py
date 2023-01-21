T = float(input())
def convert_to_celsius (T):
 C = round((T - 32) / 1.8, 2)
 print ("The temperature in Celsius is:", C)
def convert_to_kelvin (T):
 K = round(((T - 32) / 1.8) + 273.15, 2)
 print ("The temperature in Kelvin is:", K)

def convert_temp ():
 convert_to_celsius (T)
 convert_to_kelvin (T)
convert_temp ()
