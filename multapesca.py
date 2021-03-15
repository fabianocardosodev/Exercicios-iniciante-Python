peso_peixe = input("Digite o peso do peixe: ")

pesopei = eval(peso_peixe)

if pesopei > 50:
    excesso = pesopei - 50
    multa = excesso * 4.00

print('O peso do peixe extrapolou o limite em: ' , excesso , 'kg')    
print ('O valor da multa à ser paga é de: R$', multa , 'reais')