peso = float(input('Digite seu Peso(kg):'))
altura = float(input('Digite sua Altura(m):'))

imc = peso/(altura ** 2)

if imc < 16.00:
    print('Baixo peso Grau III')
elif 16.00 <= imc < 16.99:
    print('Baixo peso Grau II')
elif 17.00 <= imc < 18.49:
    print('Baixo peso Grau I')
elif 18.5 <= imc < 24.99:
    print('Peso Ideal')
elif 25.00 <= imc < 29.99:
    print('Sobrepeso')
elif 30.00 <= imc < 34.99:
    print('Obseidade Grau I')
elif 35.00 <= imc < 39.99:
    print('Obesidade Grau II')
elif imc >= 40.00:
    print('Obesidade Grau III')