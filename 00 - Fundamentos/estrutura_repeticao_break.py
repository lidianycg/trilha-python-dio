numero = -1

while True:
    numero = int(input("Informe um número: "))

    if numero == 10:
        break

    print(numero)

# Break:

for numero in range(100):

    if numero ==12:
        break

    print(numero, end=" ")

# Continue:

for numero in range(100):

    if numero ==12:
        continue

    print(numero, end=" ")

# Continue vai pular a execução, não irá exibir. No exemplo abaixo, irá imprimir na tela somente os números ímpares:

for numero in range(100):
    if numero % 2 == 0:
        continue
    print(numero, end=" ")


# O exemplo abaixo só funciona nessa ordem. Se invertermos, o laço não corta e a execução nunca termina. Isso ocorre porque
# o 10 é um número par. Sendo assim, o programa vai pular e não vai continuar a execução embaixo.
# O continue é usado quando você quer pular uma execução, e o break quando você quer cortar a execução da sua estrutura de repetição.

while True:
    numero = int(input("Informe um número: "))

    if numero == 10:
        break
    if numero % 2 == 0:
        continue
    print(numero)