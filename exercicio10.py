print('Dados Pessoas')

qnt_pessoas = int(input('Número de pessoas: '))

maior_altura = 0
menor_altura = float('inf')  #
total_homens = 0
soma_altura_mulheres = 0
quantidade_mulheres = 0

for i in range(qnt_pessoas):
    altura = float(input(f'Sua altura (em metros) para a pessoa {i+1}: '))
    genero = input('Seu gênero (F/M): ').upper().strip()  

    if altura > maior_altura:
        maior_altura = altura
    if altura < menor_altura:
        menor_altura = altura
    
    if genero == 'F':
        soma_altura_mulheres += altura
        quantidade_mulheres += 1
    elif genero == 'M':
        total_homens += 1

if quantidade_mulheres > 0:
    media_altura_mulheres = soma_altura_mulheres / quantidade_mulheres
else:
    media_altura_mulheres = 0

print(f'A maior altura é: {maior_altura:.2f} metros')
print(f'A menor altura é: {menor_altura:.2f} metros')
print(f'A média de altura das mulheres é: {media_altura_mulheres:.2f} metros')
print(f'O número total de homens é: {total_homens}')
