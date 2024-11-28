#Problema "mais_velho" 
#Fazer um programa para ler um conjunto de nomes de pessoas e suas respectivas idades. Os nomes 
#devem ser armazenados em um vetor, e as idades em um outro vetor. Depois, mostrar na tela o nome 
#da pessoa mais velha. 

print('mais velho')

numero_pessoas = int(input('quantas pessoas tem? '))
vetor_nome = []
vetor_idade = []

for i in range(numero_pessoas):
    nome = str(input('seu nome: '))
    idade = int(input('sua idade: '))
    vetor_nome.append(nome)
    vetor_idade.append(idade)
    
pessoa_velha = vetor_nome[0]
mais_idade = vetor_idade[0]

for i in range(1,numero_pessoas):
    if vetor_idade[i] > mais_idade:
        mais_idade = vetor_idade[i]
        pessoa_velha = vetor_nome[i]
         
print(f"a pessoa mais velha é {pessoa_velha}, ela tem {mais_idade}")
        

    
