print('Comerciante')

mercadorias = int(input('Quantos produtos serão digitados? '))
soma_compra = 0
soma_venda = 0
lucro_abaixo_10 = 0
lucro_entre_10_20 = 0
lucro_acima_20 = 0

for i in range(mercadorias):
    print(f"Produto {i + 1}:")
    nome = str(input('Nome do produto: '))
    compra = float(input('Preço da compra R$: '))
    venda = float(input('Preço da venda R$: '))
    
    lucro = venda - compra  
    porcetagem_lucro = (lucro / compra) * 100  
    
    soma_compra += compra
    soma_venda += venda
    
    
    if porcetagem_lucro < 10:
        lucro_abaixo_10 += 1
    elif 10 <= porcetagem_lucro <= 20:
        lucro_entre_10_20 += 1
    else:
        lucro_acima_20 += 1

lucro_total = soma_venda - soma_compra

print(f"\nTotal de mercadorias com lucro abaixo de 10%: {lucro_abaixo_10}")
print(f"Total de mercadorias com lucro entre 10% e 20%: {lucro_entre_10_20}")
print(f"Total de mercadorias com lucro acima de 20%: {lucro_acima_20}")
print(f"\nValor total de compra: R$ {soma_compra:.2f}")
print(f"Valor total de venda: R$ {soma_venda:.2f}")
print(f"Lucro total: R$ {lucro_total:.2f}")
