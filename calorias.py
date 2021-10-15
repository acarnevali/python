quantidadeComida = int(input('Quantos refeições foram feitas hoje: '))
comida = ''
calorias = 0

if quantidadeComida > 0:
    for f in range(quantidadeComida):
        comida = (input('Comida: '))
        calorias += int(input('Calorias: '))
    print(f'Total de calorias diária: {calorias}')
else:
    print('Nenhuma caloria foi ingerida')