graus_fahrenheit = input('Digite quantos graus Fahrenheit: ')

temp = eval(graus_fahrenheit)
# vamos transformar o fahrenheit em celsius
celsius = 5 * ((temp-32) / 9)

print ('Em Celsius a temperatura é : ' , celsius ,  ' graus ')


