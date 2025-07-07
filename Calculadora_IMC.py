altura = float(input("digite a sua altura: "))
peso = float(input("digite o seu peso: "))
imc = peso  / (altura ** 2) 


if imc < 18.5:
    print("""BAIXO PESO""")
elif imc == 18.5 or imc < 24.9:    
    print("""PESO ADEQUADO """)
elif  imc  <= 25 or imc < 29.9:      
    print("""SOBREPESO """)
elif imc <= 30  or imc < 34.9:
    print("""OBESIDADE GRAU 1.""")
elif imc <=35 or imc < 39.9:
    print("""OBESIDADE GRAU 2""")
else:
    print("""OBESIDADE GRAU 3""")
print(imc)