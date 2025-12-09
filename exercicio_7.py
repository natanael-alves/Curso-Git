idade = int(input("Informe sua idade: "))

if idade <6:
    print("Tarifa gratuita.")

elif (idade >= 6) and (idade< 18):
    print("Pagará meia tarifa que é R$ 5.00 ") 

elif idade >= 18 and idade < 60:
    print("Pagara a tarifa inteira que é R$ 10.00 ")

else:
    print("Tarifa gratuita ! ")