
#exemplo - fatorail de um numero
'''
crie um programa que recebe um numero e imprime o seu fatorial
lembre-se de usar o metodo 5Q's para montar o algoritmo
'''
numero = int(input('digite um numero'))
if numero > 0:
  fatorial = 1
  for item in range(1,numero +1):
    fatorial = fatorial * item
  print(fatorial)
  