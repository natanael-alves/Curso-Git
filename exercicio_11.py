limite = int (input("Informe o limite: "))
produtorio = 1


for i in range(1, limite + 1):
    produtorio = produtorio * i

print(f"Resultado do produtório: {produtorio}")