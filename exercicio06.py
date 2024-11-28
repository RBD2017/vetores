print('abaixo_da_media')

n1 = int(input('Quantos elementos vai ter o vetor'))
vetor_float = []
soma_vetor = 0

for i in range(n1):
    valor_vetor = float(input('Digite um numero: '))
    soma_vetor += valor_vetor
    vetor_float.append(valor_vetor)
    
media = soma_vetor / n1
print(f"media de vetores  {media:.3f}") 

for r in vetor_float:
        if r < media:
            print(f"abaixo media {r:.1f}")
    



    