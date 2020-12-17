'''Para criar uma função é necessario por 'def' antes'''

# def nome(str):
#   print('-' * 10)
#   print(f"{str:^10}")
#   print('-'*10)


# name = input(str('Insira o que vc quiser: ')).upper()
# nome(name)

# ----------------------------------------------------------

# def nome(str):
#    print('-' * 10)
#    print(f"{str:^10}")
#    print('-' * 10)

# nome('QUALQUER COISA')

# ----------------------------------------------------------

'''Empacotar parametros'''

# def contador(*num):
#    print(len(num))


# contador(1, 2, 3)
# contador(5, 8, 6, 7)

# ----------------------------------------------------------

"""print('-' * 20)
print('CALCULO DE ÁREA')
print('-' * 20)


def area(t, l):
    area = t * l
    print('-' * 20)
    print(f'Você inseriu o tamanho {t} e largura {l}, O calculo da area é {area}m²')


tamanho = float(input('Insira o tamanho: '))
largura = float(input('Insira a largura: '))

area(tamanho, largura)"""

# ----------------------------------------------------------

"""def nome(str):
    tmn = len(str) + 4
    print('-' * tmn)
    print(f'  {str}')
    print('-' * tmn)


name = input(str('Insira o que vc quiser: ')).upper()
nome(name)"""

# ----------------------------------------------------------

'''import time


def contador(i, f, p):
    for c in range(i, f + 1, p):
        print(c, end=' ')
        time.sleep(0.5)


for c in range(1, 11):
    print(c, end=' ')
    time.sleep(0.5)
print()
for c in range(10, 0, -2):
    print(c, end=' ')
    time.sleep(0.5)
print()

i = int(input('Insira o incio: '))
f = int(input('Insira o fim: '))
p = int(input('Insira o passo: '))
contador(i, f, p)'''

# ----------------------------------------------------------

'''import time
from random import randint
cont = 0
lst = list()
vzs = randint(1, 10)

for n in range(1, vzs+1):
    qtd = randint(1, 10)
    if qtd not in lst:
        lst.append(qtd)
lst.sort()
for i in range(1, len(lst)+1):
    print(lst[cont], end=' ')
    time.sleep(0.3)
    cont += 1
print(f'Foram informados {len(lst)} valores')
print(f'o Maior valor informado foi {max(lst)}')'''

# ----------------------------------------------------------

'''from random import randint


def sorteio(lts):
    qtd = 6
    for n in range(1, 6):
        sorteio = randint(1, 10)
        lts.append(sorteio)
    print(f'sorteando 5 valores da lista: {lts}')


def somaPar():
    soma = 0
    for x in lista:
        if x % 2 == 0:
            soma += x
    lista.sort()
    print(f'Somando os valores pares de {lista}, temos {soma}')


lista = list()
sorteio(lista)
somaPar()'''

# ----------------------------------------------------------

'''Aula 2'''
'''Ajuda Interativa'''
# help()
# print(input.__doc__)

'''DOCSTRINGS'''
'''Documentando sua função particular '''
'''Para documentar sua função, é ne abrir 3 aspas duplas abaixo 
do inicio da função 'def', apertar enter e descrever oque seu codigo faz'''

# ----------------------------------------------------------

'''PARAMETROS OPCIONAIS'''
'''Informar na declaração do codigo o valor de 0 para a variavel
ela serviara como contingencia caso o usuario não informe valor'''

# def somar(a=0, b=0, c=0):
#   s = a + b + c
#   print(f'{s}')


# somar(1, 2, 3)
# somar(1, 2)

# ----------------------------------------------------------

'''ESCOPO DE VARIAVEIS'''

# Para usar uma variavel global dentro de funções, supondo que a variavel fora da funcao seja 'a'
# def funcao():
#      global a

# ----------------------------------------------------------

'''RETORNO DE VARIAVEIS'''

# def somar(a=0, b=0, c=0):
#   s = a + b + c
#   return s


# resp = somar(1, 2, 3)
# print(somar(1, 2, 3))