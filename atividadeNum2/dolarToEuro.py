# Valmir pediu para fazer um conversor de Reais para Dólar e Euro.

def dolarAndEuro ():
    reais = int(100)
    taxaDolar = float(5.25)
    taxaEuro = float(6.15)
    # O programa deve calcular e exibir os valores convertidos, arredondando para duas casas decimais.
    dolar = reais / taxaDolar
    euro = reais / taxaEuro
    print(f"R$ {reais} em Dólar é: ${dolar:.2f}")
    print(f"R$ {reais} em Euro é: €{euro:.2f}")
dolarAndEuro()

