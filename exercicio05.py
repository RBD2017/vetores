n = int(input("Digite o tamanho dos vetores: "))

A = []
B = []

print("Digite os elementos do vetor A:")
for i in range(n):
    A.append(int(input()))

print("Digite os elementos do vetor B:")
for i in range(n):
    B.append(int(input()))

C = []
for i in range(n):
    C.append(A[i] + B[i])

print("Vetor C (A + B):", C)
