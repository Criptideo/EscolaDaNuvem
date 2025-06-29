#Crie um programa que converta temperaturas entre Celsius, Fahrenheit e Kelvin. 
#O usuário deve informar a temperatura, a unidade de origem e a unidade para qual deseja converter.

def celsius_to_fahrenheit_to_kelvin():
    celsius = float(input("Digite a temperatura em Celsius: "))
    fahrenheit = (celsius * 9/5) + 32
    kelvin = celsius + 273.15
    print(f"{celsius}°C é igual a {fahrenheit}°F e {kelvin}K")
celsius_to_fahrenheit_to_kelvin()
