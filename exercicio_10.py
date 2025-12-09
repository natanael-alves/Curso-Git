numero_lido = int(input("Informe um número: "))
somatorio = 0


while numero_lido != 0:
    somatorio = somatorio + numero_lido
    numero_lido = int(input("Mais um número: "))

print(f"Somatório dos números: {somatorio}")