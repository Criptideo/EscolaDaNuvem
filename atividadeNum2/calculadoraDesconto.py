# Desenvolva um programa que calcula o desconto em uma loja. Use as seguintes informações:

#* Nome do produto: "Camiseta"
#* Preço original: R$ 50.00
#* Porcentagem de desconto: 20%
#O programa deve calcular o valor do desconto e o preço final, exibindo todos os detalhes.

def descontoCamiseta():
    produto = 'Camiseta'
    precoOriginal = float(50.00)
    porcentagemDesconto = float(20.0)
    valorDesconto = (porcentagemDesconto / 100) * precoOriginal
    precoFinal = precoOriginal - valorDesconto
    print(f"Preço original: R${precoOriginal:.2f}")
    print(f"O produto aplicando o desconto ficou: R${precoFinal:.2f}")
descontoCamiseta()
