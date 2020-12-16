# nome = str(input('Qual é seu nome? '))

# if nome == 'Gustavo':
#    print('Que nome Lindo!')
# elif nome == 'Paulo' or nome == 'Guilherme':
#    print('Seu nome é bem popular no Brasil.')
# else:
#    print('Seu nome não é tão legal.')

# ----------------------------------------------------------

# valorCasa = float(input('Qual o valor da Casa? '))
# salario = float(input('Quanto é seu salario? '))
# qtdprestacoes = int(input('Em quantas prestações você quer fazer? '))

# valorprestacao = valorCasa / qtdprestacoes

# if valorprestacao > (salario / 100) * 30:
#    print('Infelizmente seu emprestimo foi negado')

# else:
#    print('Parabens, Seu emprestimo foi aceito!')

# ----------------------------------------------------------

# numero = int(input('Digite um numero: '))
# numero2 = int(input('Digite outro numero: '))

# if numero > numero2:
#    print('O primeiro valor é maior.')
# elif numero < numero2:
#    print('O segundo valor é maior.')
# else:
#    print('Ambos ão Iguais.')

# ----------------------------------------------------------

# anoNacimento = int(input('Informe seu ano de nascimento: '))

# anoatual = 2020

# if (anoatual - anoNacimento) < 18:
#    print('Ainda não é o momento de se alistar, falta {} ano(s)'.format(18 - (anoatual - anoNacimento)))

# elif (anoatual - anoNacimento) == 18:
#    print('Este é o ano que você precisa se alistar!')

# elif (anoatual - anoNacimento) > 18:
#    print('Passou do ano de se alistar em  {} ano(s)'.format((anoatual - anoNacimento) - 18 ))

# ----------------------------------------------------------

# nota1 = float(input('Insira a primeira nota: '))
# nota2 = float(input('Insira a segunda nota: '))

# media = (nota1 + nota2) / 2

# print('sua media {}'.format(media))
# if media < 5.0:
#    print('Reprovado')
# elif media > 6.9:
#    print('Aprovado')
# else:
#    print('Recuperação.')

# ----------------------------------------------------------

# anoNascimento = int(input('Seu ano de nascimento '))

# anoAtual = 2020
# idade = anoAtual - anoNascimento

# if idade <= 9:
#    print('Mirim')
# elif idade > 9 and idade <= 14:
#    print('Infantil')
# elif idade > 14 and idade <= 19:
#    print('Junior')
# elif idade == 20:
#    print('Senior')
# elif idade > 20:
#    print('Master')

# ----------------------------------------------------------

# tam1 = float(input('Insira o primeiro tamanho: '))
# tam2 = float(input('Insira o segundo tamanho: '))
# tam3 = float(input('Insira o terceiro tamanho: '))

# if tam1 == tam2 and tam1 == tam3:
#    print('Equilatero')

# elif tam1 != tam2 and tam1 != tam3 and tam2 != tam3:
#    print('Escaleno')

# elif tam1 == tam2 and tam1 != tam3 or tam1 == tam3 and tam1 != tam2 or tam2 == tam3 and tam2 != tam1:
#    print('Isosceles')

# ----------------------------------------------------------

# peso = float(input('Seu Peso: '))
# altura = float(input('Sua altura: '))

# imc = peso / (altura * altura)

# if imc < 18.5:
#    print('Abaixo do peso')

# elif imc >= 18.5 and imc < 25:
#    print('Peso Ideal')

# elif imc >= 25 and imc < 30:
#    print('sobrepeso')

# elif imc >= 30 and imc < 40:
#    print('Obeso')

# elif imc > 40:
#    print('Obeso Morbido')

# ----------------------------------------------------------

# metodoDePagamento = int(input(' o valor do produto é de R$500,00.'
#                             '\n Informe o metodo de pagamento: '
#                             '\n 1 - Dinheiro/Cheque'
#                             '\n 2 - Cartão Avista'
#                             '\n 3 - Cartão parcelado até 2x '
#                             '\n 4 - Cartão parcelado em 3x ou mais'))

# if metodoDePagamento == 1:
#    print((500 / 100) * 90)
# elif metodoDePagamento == 2:
#    print((500 / 100) * 95)
# elif metodoDePagamento == 3:
#    parcelas = int(input('Em quantas vezes? '))
#    if parcelas > 2:
#        print('Negado')
#    else:
#        print('Valor total {}, em {} vezes de {}'.format(500, parcelas, 500 / parcelas))
# elif metodoDePagamento == 4:
#    parcelas = int(input('Em quantas vezes? '))
#    if parcelas < 3:
#        print('Negado')
#    else:
#        print('Valor total {}, em {} vezes de {}'.format((500/100)*120, parcelas, (500/100)*120 / parcelas))

# ----------------------------------------------------------

# import random

# sinal = int(input(' Escolha seu sinal: '
#                  '\n 1 - Pedra'
#                  '\n 2 - Papel'
#                  '\n 3 - Pesoura '))

# pc = random.randint(1, 3)

# if sinal == 1:
#   sinal = str('Pedra')

# elif sinal == 2:
#   sinal = str('Papel')

# elif sinal == 3:
#   sinal = str('Tesoura')

# if pc == 1:
#   pc = 'Pedra'

# elif pc == 2:
#   pc = 'Papel'

# elif pc == 3:
#   pc = 'Tesoura'
# else:
#   print(' ')

# print(sinal)
# print(pc)

# ----------------------------------------------------------

# num = int(input('Insira um numero:  '))
# opcao = int(input('Insira um numero de 1 a 3: '))

# if opcao == 1:
#    print(bin(num)[2:])
# elif opcao == 2:
#    print(oct(num)[2:])
# elif opcao == 3:
#    print(hex(num)[2:])
# else:
#    print('Tenten novamente!')

# ----------------------------------------------------------


