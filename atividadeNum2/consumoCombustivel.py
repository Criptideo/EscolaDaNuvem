#Desenvolva um programa que calcula o consumo médio de combustível de um veículo. Use os seguintes dados:

#* Distância percorrida: 300 km
#* Combustível gasto: 25 litros
#O programa deve calcular o consumo médio (km/l) e exibir todos os dados da viagem, incluindo o resultado final arredondado para duas casas decimais.

def consumoMedio ():
    distanciaPercorrida = float(300)
    combustivelGasto = float(25)
    consumo = distanciaPercorrida / combustivelGasto
    print(f"Distância percorrida: {distanciaPercorrida:.2f}km")
    print(f"Combustível gasto: {combustivelGasto:.2f} litros")
    print(f"Consumo médio: {consumo:.2f} km/l")
consumoMedio()