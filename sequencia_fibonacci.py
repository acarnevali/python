num = int(input('Digite um número: '))
anterior = 0
prox = 1
soma = 0

while prox < num:
    soma = prox + anterior
    anterior = prox
    prox = soma

if num == prox:
    print(f'Número: {num}. Sucesso! Está na sequência!')
else:
    print(f'Número: {num}. FALHA! Não está na sequência!')