altura = float(input("digite a sua altura: "))
peso = float(input("digite o seu peso: "))
imc = peso  / (altura ** 2) 


if imc < 18.5:
    print("""BAIXO PESO: É recomendado procurar um médico para avaliação
 criteriosa do resultado. Pode indicar um estado de consumo do organismo, com
 poucas reservas e riscos associados.""")
elif imc == 18.5 or imc < 24.9:    
    print("""PESO ADEQUADO: Tudo indica que está tudo bem, mas é
 importante avaliar outros parâmetros da composição corporal, para compreender se
 estão dentro do recomendado. Algumas pessoas apresentam IMC dentro da
 normalidade, mas têm circunferência abdominal maior que a recomendada e/ou
 quantidade de massa gorda acima do ideal. """)
elif  imc  <= 25 or imc < 29.9:      
    print("""SOBREPESO: O sobrepeso está associado ao risco de doenças
 como diabetes e hipertensão. Então, atenção! Consulte um médico e reveja hábitos
 para reverter o quadro. Também é importante avaliar outros parâmetros, como a
 circunferência abdominal. """)
elif imc <= 30  or imc < 34.9:
    print("""OBESIDADE GRAU I:  É importante buscar orientação médica e
 nutricional para entender melhor o seu caso, mesmo que os exames (colesterol e
 glicemia, por exemplo estejam normais.""")
elif imc <=35 or imc < 39.9:
    print("""OBESIDADE GRAU II: Indica um quadro de obesidade mais
 evoluído em relação à classificação anterior e, mesmo com exames laboratoriais
 dentro da normalidade, não se deve atrasar a busca por orientação médica e
 nutricional. """)
else:
    print("""OBESIDADE GRAU III:  Nesse ponto, a chance de já estarmos diante
 de outras doenças associadas é mais elevada. É fundamental buscar orientação
 médica. """)
print(imc)