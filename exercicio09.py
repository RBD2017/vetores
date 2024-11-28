print('aprovados')
qnt_alunos = int(input('Quantos alunos serao digitados '))
nomes_alunos = []
notas1 = []
notas2 = []
for i in range(qnt_alunos):
    nome = str(input('seu nome '))
    nota1 = int(input('nota primeiro semestre'))
    nota2 = int(input('nota segundo semestre'))
    
    nomes_alunos.append(nome)
    notas1.append(nota1)
    notas2.append(nota2)
    
for i in range(qnt_alunos):
    media = (notas1[i] + notas2[i]) / 2
    if media >= 6:
        print(f"{nomes_alunos[i]} - media: {media:.2f}")