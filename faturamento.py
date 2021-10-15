assinatura = input('Insira o tipo de assinatura:')
faturamento = float(input('Insira faturamento anual:'))
bonus = 0

if assinatura == 'Basic':
    bonus = faturamento * 0.3
elif assinatura == 'Silver':
    bonus = faturamento * 0.2
elif assinatura == 'Gold':
    bonus = faturamento * 0.1
elif assinatura == 'Platinum':
    bonus = faturamento * 0.05

print('Total de Bônus é: {:.2f}'.format(bonus))
