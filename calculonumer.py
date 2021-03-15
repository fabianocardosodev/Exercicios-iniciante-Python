numero1 = input('Digite um numero inteiro: ')
numero2 = input('Digite outro numero inteiro: ')
numero3 = input('Digite agora um numero real: ')

num1 = eval(numero1)
num2 = eval(numero2)
num3 = eval(numero3)

# primeiro vamos calcular o produto do dobro do primeiro com metade do segundo
calculo1 = (num1 * 2) + (num2 / 2)

#a soma do triplo do primeiro com o terceiro. 
calculo2 = int(num1 * 3 ) + float(num3)

# o terceiro elevado ao cubo. 
calculo3 = float(num3 ** 3) 

print('O produto do dobro do primeiro com metade do segundo é: ' , calculo1)
print('A soma do triplo do primeiro com o terceiro é: ' , calculo2)
print('O terceiro elevado ao cubo é: ', calculo3)