nome = "LiDiAnY"

print(nome.upper())
print(nome.lower())
print(nome.title())

# Remove espaços em branco:

texto = "  Olá, mundo     "
print(texto + ".")
print(texto.strip() + ".")
print(texto.rstrip() + ".")
print(texto.lstrip() + ".")

# Junção e centralização:

menu = "Python"
print("####" + menu + "####")
print(menu.center(14))
print(menu.center(14, "#"))

for letra in menu:
    print(letra, end="-")
print()

print("-".join(menu))
