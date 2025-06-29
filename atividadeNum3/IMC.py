#Desenvolva um programa que calcule o Índice de Massa Corporal (IMC) de uma pessoa. 
#O programa deve solicitar o peso (em kg) e a altura (em metros) do usuário, 
#calcular o IMC e fornecer a classificação de acordo com a tabela padrão de IMC.

# IMC = peso / (altura ** 2)

def calcular_imc():
    try:
        peso = float(input("Digite o seu peso em kg: "))
        altura = float(input("Digite a sua altura em metros: "))
        calculoIMC = peso / (altura ** 2)
        print(f"Seu IMC é: {calculoIMC:.2f}")
        if calculoIMC < 18.5:
            print("Classificação: Abaixo do peso")
        elif 18.5 <= calculoIMC < 24.9:
            print("Classificação: Peso normal")
        elif 25 <= calculoIMC < 29.9:
            print("Classificação: Sobrepeso")
        elif 30 <= calculoIMC < 34.9:
            print("Classificação: Obesidade grau 1")
        elif 35 <= calculoIMC < 39.9:
            print("Classificação: Obesidade grau 2")
        else:
            print("Classificação: Obesidade grau 3 ou mórbida")
    except ValueError:
        print("Por favor, insira valores numéricos válidos para peso e altura.")
        return
calcular_imc()