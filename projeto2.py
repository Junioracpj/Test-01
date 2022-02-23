#chute um numero
'''
Escreva um programa que, ao iniciar gera um valor aleatório de 1 a 10 e permite que o usuario chute um numero até que o valor alaetório gerado do programa seja chutado corretamente.
lembre-se de usar o metodo 5Q's para montar o algoritmo
'''

import random
valor_aleatorio = random.randint(1,10)
acertou = False
while acertou == False:
  chute = int(input('chute um valor de 1 a 10 '))
  if chute > valor_aleatorio:
    print('chute foi maior que o valor gerado')
  elif chute < valor_aleatorio:
    print('chute foi menor que o valor gerado')
  elif chute == valor_aleatorio:
    acertou = True
    print('voce acertou')