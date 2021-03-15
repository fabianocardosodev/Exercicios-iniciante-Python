altura = input('Digite sua altura: ')
sexo = input('Digite seu sexo: ')

alt1 = eval(altura)

# calcule seu peso ideal, usando a seguinte fórmula
if sexo == 'h':
    peso = (72.7 * alt1) - 58
else :
    peso = (62.1 * alt1) -44.7
print("Seu peso ideal é: " , peso)


