# Crie um programa que calcula a média escolar de um aluno. Use as seguintes notas:

# * Nota 1: 7.5
# * Nota 2: 8.0
# * Nota 3: 6.5
# O programa deve calcular a média e exibir todas as notas e o resultado final, arredondando para duas casas decimais.

def mediaEscolar ():
    primeiraNota = float(7.5)
    segundaNota = float(8.0)
    terceiraNota = float(6.5)
    media = (primeiraNota + segundaNota + terceiraNota) / 3
    print(f"Nota 1: {primeiraNota:.2f}")
    print(f"Nota 2: {segundaNota:.2f}")
    print(f"Nota 3: {terceiraNota:.2f}")
    print(f"Média: {media:.2f}")
    if primeiraNota >= media:
        print('O primeiro aluno foi aprovado.')
    elif primeiraNota < media:
        print('O primeiro aluno foi reprovado.')
    if segundaNota >= media:
        print('O segundo aluno foi aprovado.')
    elif segundaNota < media:
        print('O segundo aluno foi reprovado.')
    if terceiraNota >= media:
        print('O terceiro aluno foi aprovado.')
    elif terceiraNota < media:
        print('O terceiro aluno foi reprovado.')
mediaEscolar()