#medidor de velocidade
'''
demonstre no painel de o motorista levou multa ou não ao passar pelo radar
lembre-se de usar o metodo 5Q's para montar o algoritmo
'''

velocidade = int(input('digite a velocidade '))
limiar = int(input('digite a velocidade maxima '))
if velocidade <= limiar:
 print ('nao  houve multa')
elif velocidade > limiar and velocidade <= limiar*1.1:
 print ('multa leve')
elif velocidade > limiar*1.1 and velocidade <= limiar*1.2:
 print ('multa grave')
elif velocidade > limiar*1.2:
 print ('multa gravissima')