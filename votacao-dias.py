seg = int(input('Insira votos para Segunda: '))
ter = int(input('Insira votos para Terça: '))
qua = int(input('Insira votos para Quarta: '))
qui = int(input('Insira votos para Quinta: '))
sex = int(input('Insira votos para Sexta: '))

if seg > ter and seg > qua and seg > qui and seg > sex:
    print('O dia escolhido para lives foi Segunda!')
elif ter > seg and ter > qua and ter > qui and ter > sex:
    print('O dia escolhido para lives foi Terça!')
elif qua > seg and qua > ter and qua > qui and qua > sex:
    print('O dia escolhido para lives foi Quarta!')
elif qui > seg and qui > ter and qui > qua and qui > sex:
    print('O dia escolhido para lives foi Quinta!')
elif sex > seg and sex > ter and sex > qua and sex > qui:
    print('O dia escolhido para lives foi Sexta!')