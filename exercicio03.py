print('Alturas')

numero_pessoas = int(input('Quantas pessoas serão digitadas? '))

nome_pessoas = []
alturas = 0
total_menores_16 = 0

for i in range(numero_pessoas):
    print(f"Dados da {i + 1}ª pessoa")
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    altura = float(input('Altura: '))

    
    alturas += altura
    
    
    if idade < 16:
        total_menores_16 += 1
        nome_pessoas.append(nome)


media_altura = alturas / numero_pessoas


porcentagem_menores_16 = (total_menores_16 / numero_pessoas) * 100


print(f"A média de altura é: {media_altura:.2f} metros")
print(f"A porcentagem de pessoas com menos de 16 anos é: {porcentagem_menores_16:.2f}%")


if nome_pessoas:
    print("Pessoas com menos de 16 anos:")
    for nome in nome_pessoas:
        print(nome)
else:
    print("Não há pessoas com menos de 16 anos.")
