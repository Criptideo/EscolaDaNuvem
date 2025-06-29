def saudacao():
    print("Olá, seja bem-vindo ao nosso programa!")
saudacao()

def despedida():
    print("Obrigado por usar nosso programa! Até logo!")
despedida()

def cumprimentar(nome, number): #um argumento para a função
    print(nome,number)
    return f"Olá, {nome}! Bem-vindo ao programa!"
resultado = cumprimentar("Miles", 123)

print(resultado)

#estudar mais sobre loops e funções em python :D


def soma(a, b):
    result = a + b
    print(f"A soma de {a} e {b} é {result}")    
    return result
soma(5, 10)

#função lambda é uma função anônima

multiplicar = lambda x, y: x * y
resultado = multiplicar(4, 5)
print(f"O resultado da multiplicação é: {resultado}")

sub = lambda num1, num2: num1 - num2
print(sub(3,5))













