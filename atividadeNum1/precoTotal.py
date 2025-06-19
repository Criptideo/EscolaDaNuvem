# 4- Calculadora de Preço Total
# Desenvolva um programa que calcula o preço total de uma compra. Use as seguintes informações:

# Nome do produto: "Cadeira Infantil"
# Preço unitário: R$ 12.40
# Quantidade: 3
# O programa deve calcular o preço total e exibir todas as informações, incluindo o resultado final.

nomeProduto = str("Cadeira Infantil")
precoUnitario = float(12.40)
quantidade = int(3)
precoTotal = precoUnitario * quantidade

print(f"{quantidade} unidades do item {nomeProduto} foram compradas, totalizando R${precoTotal:.2f}")