print('soma vetor')

numero = int(input('quantos numeros vai digitar '))
valores = []
soma = 0

for i in range(numero):
    numeros_reais = float(input('digite um numero '))
    soma += numeros_reais
    valores.append(numeros_reais)
    media = soma / numero
    
print(F" a soma dos numeros {soma}")  
print(F"a media {media}")
print(F"a lista de {valores}")
    