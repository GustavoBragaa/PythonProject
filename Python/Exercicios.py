import math

# print('ola, mundo')
# print(2+3)
# print('2'+'3')

# num1 = int(input('numero: '))
# num2 = int(input('outro numero: '))

# print('seu valor foi: ', num1 + num2)

# como descobrir o tipo de uma variavel
# print('o tipo da variavel é: ', type(num1))

# novo metodo de print
# print('valor 1: {}, valor 2: {}'.format(num1,num2))


# aula 7
# ordem de precedencia
# () Parenteses

#  ** potencia

# expressoes aritimeticas 1 * e / e // e %

# expressoes aritimeticas 2 + e -

# exercicios aula 7

# Desafio 1

# valor1 = int(input('Informe um numero: '))

# print('seu numero: {}, valor antecessor: {}, valor sucessor {}'.format(valor1, valor1 - 1, valor1 + 1) )

# Desafio 2

# valor2 = int(input('Informe um numero: '))

# print('seu numero: {}, o dobro: {}, o triplo: {}, a raiz quadrada {}'.format(valor2, valor2*2, valor2*3, valor2**(1/2)))


# Desafio 2

# valor3 = float(input('Primeira nota: '))
# valor4 = float(input('Segunda nota: '))

# print('Primeira nota: {}, Segunda nota: {}, Media da nota: {}'.format(valor3, valor4, (valor3 + valor4)/2))

# Desafio 3

# valor5 = int(input('valor em metros: '))

# print('valor em metros: {}, valor em centimetros: {}cm, valor em milimetros: {}mm'.format(valor5, valor5*100, valor5*1000))

# Desafio 4

# valor6 = int(input('valor para calculo: '))

# print('seu valor: {}'.format(valor6))
# print('multiplicado por 2: {}'.format(valor6*2))
# print('multiplicado por 3: {}'.format(valor6*3))
# print('multiplicado por 4: {}'.format(valor6*4))
# print('multiplicado por 5: {}'.format(valor6*5))
# print('multiplicado por 6: {}'.format(valor6*6))
# print('multiplicado por 7: {}'.format(valor6*7))
# print('multiplicado por 8: {}'.format(valor6*8))
# print('multiplicado por 9: {}'.format(valor6*9))
# print('multiplicado por 10: {}'.format(valor6*10))

# Desafio 5


# valor7 = float(input('Quanto dinheiro você tem? '))
# valor8 = valor7/3.27

# print('você tem: R${}, você pode comprar: U${:.2f} em dolares'.format(valor7, valor8))

# Desafio 6

# valor9 = float(input('Altura: '))
# valor10 = float(input('Largura: '))

# print('Altura: {}m, Largura: {}m, sua area é: {}m², você precisara de: {}Ls de tinta'.format(valor9, valor10, valor9*valor10,(valor9*valor10)/4))

# Desafio 7

# valor11 = float(input('Preço: '))

# print('o preço informado: {}, o preço com 5% de desconto:{:.2f}'.format(valor11, (valor11/100)*95))


# Desafio 8

# valor12 = float(input('Salario: R$'))

# print('o Salario informado: R${}, o Salario com 15% de aumento: R${:.2f}'.format(valor12, (valor12/100)*115))


# Desafio 14

# c = float(input('Insira a temperatura em C: '))
# f = 9 * c / 5 + 32

# print('A temperatura de {}ºC corresponde a {}°F'.format(c, f))

# Desafio 15

# km = int(input('Informe os quilometros percorridos: '))
# dias = float(input('Informe quantos dias foram necessarios: '))

# print('O valor a ser pago é de : R${:.2f}'.format(km * 0.15 + dias * 60))

# ----------------------------------------------------------


# nome = str(input('Insira seu nome completo: '))

# print(nome.upper())
# print(nome.lower())
# print(len(nome.strip()) - nome.count(' '))

# nome2 = nome.split()
# nome3 = nome2[1]
# print(nome3)
# print(len(nome3))
# print(nome.find(' '))#Identifica o primeiro espaço e escreve o texto anterior


# ----------------------------------------------------------

# numero = int(input('insira um numero de 0 a 9999:'))
# u = numero // 1 %10
# d = numero // 10 %10
# c = numero // 100 %10
# m = numero // 1000 %10

# print('Unidade: {}'.format(u))
# print('Dezena: {}'.format(d))
# print('Centena: {}'.format(c))
# print('Milhar: {}'.format(m))

# ----------------------------------------------------------

# nome = str(input('Escreva o nome da cidade em que você nasceu: '))

# nome2 = nome.split()
# nome3 = nome2[0]
# print('SANTO' in nome3)

# ----------------------------------------------------------

# nome = str(input('Escreva uma frase: ')).strip()

# nome2 = nome.lower()

# print('A letra A aparece {} vezes na frase.'.format(nome2.count('a')))
# print('A letra A aparece a primeira vez na posição {}.'.format(nome2.find('a')+1))
# print('A letra A aparece a ultima vez na posição {}.'.format(nome2.rfind('a')+1))

# ----------------------------------------------------------

# nome = str(input('Insira seu nome completo: '))

# quebra = nome.split()
# primeiroNome = quebra[0]
# print(primeiroNome)

# calculaNomes = int(len(quebra)-1)
# segundoNome = quebra[calculaNomes]
# print(segundoNome)

# ----------------------------------------------------------

'''[print('', x, end='\t')
 for x in "Hello World"];
print()

[print(ord(x), end='\t')
 for x in "Hello World"]
print()'''

# ----------------------------------------------------------

'''import time

while True:
    tab = 1
    num = int(input("Insira o valor da tabuada: "))

    print(f"Tabuada de {num}:")

    for n in range(1, 11):
        time.sleep(0.1)
        print(f'{num} x {tab} = {num * tab}')

        tab += 1

    resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if resp == 'N':
        break'''