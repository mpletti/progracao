#calculadora_imc
peso = float(input('Informe o peso: (kg) '))
altura = float(input('informe a sua altura: (M)' ))
imc =- peso / (altura ** 2)

print(f'O seu IMC é:{imc:.2f}')

if imc < 18.5:
    print('Você encontra-se abaixo do peso ideal')
elif 18.5 <= imc < 24.9:
    print ('Peso normal')
elif 25 <= imc < 29.9:
    print('Você encontra-se com sobrepeso')
elif 30 <= imc < 34.9:
    print('Obesidade Grau I')
elif 35 <= imc < 39.9:
    print('Obesidade Grau II')
else: 
    print('Obesidade Mórbida')
