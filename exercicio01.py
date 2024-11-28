print('---------------------------------')
print('negativos')
print('---------------------------------')

numeros_positivos = int(input('quantos numeros voce vai digitar? '))
if numeros_positivos > 10:
        print('o maximo são 10')
else:
    numero_negativo = []
    
for i in range(numeros_positivos):
    numero = int(input('digite um numero '))
    if numero < 0:
        numero_negativo.append(numero)
        
if numero_negativo:
        print('numeros negativos',numero_negativo)
else:
        print('não há números negativos')
        
