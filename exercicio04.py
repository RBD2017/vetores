N = int(input('Quantos números você vai digitar: '))

vetor = []

for i in range(N):
    numero = float(input(f"Digite um número {i + 1}: "))
    vetor.append(numero)

maior = vetor[0]  
posicao_maior = 0  

for i in range(1, N):
    if vetor[i] > maior:
        maior = vetor[i]
        posicao_maior = i

print(f'Vetor: {vetor}')
print(f'Maior número: {maior}')
print(f'Posição do maior número: {posicao_maior}')


        