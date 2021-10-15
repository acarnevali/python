quanTrasacao = int(input('Quantas transações foram realizadas hoje? '))
quantia = 0
quantiaTotal = 0
media = 0

if quanTrasacao > 0:
    for f in range(quanTrasacao):
        quantia += float(input('Valor da Transação é: '))
        
    media = quantia / quanTrasacao
    print('Valor Total é: R${:.2f}'.format(quantia))
    print('Valor Médio é: R${:.2f}'.format(media))
else:
    print('Nenhuma transação realizada')