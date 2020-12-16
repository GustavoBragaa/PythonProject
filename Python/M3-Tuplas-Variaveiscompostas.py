'''
Tipos de variaveis compostas
Tuplas
Listas
Dicionarios

As Tuplas são imutáveis ou seja nã podem ser alteradas
'''

'''variavel simples'''
# lanche = ('Hamburgues')

''' Variavel composta'''
# lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim')

# print(len(lanche))

# for cont in range(0, len(lanche)):
#    print(f'Eu vou comer {lanche[cont]} na posição {cont}')

# for pos, c in enumerate(lanche):
#   print(f'Eu vou comer {c} na posição {pos}')

''' Organiza em ordem'''
# print(sorted(lanche))

# a = 1, 2, 3
# b = 3, 4, 5
# c = a + b
# print(c.count(b))

'''Mostra qual posição esta o numero em parametro'''
# print(c.index(5))

# pessoa = ('Gustavo', 23, 'M', 1.79)

# print(pessoa[0:2])

'''Apagando a Tupla da memória'''
# del (pessoa)

# ----------------------------------------------------------

'''tupla = 'Zero', 'Um', 'Dois', 'Tres', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez',
 'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte'

resp = 0


while  0 <= resp <= 20:
    resp = int(input('Insira um numero: '))
    print(tupla[resp])'''

# ----------------------------------------------------------

'''times = 'Internacional', 'Atlético-MG', 'Flamengo', 'São Paulo', 'Fluminense', 'Palmeiras', \
        'Santos', 'Grêmio', 'Sport', 'Corinthians', 'Fortaleza', 'Ceará', 'Atlético-GO', 'Bahia', \
        'Coritiba', 'Bragantino', 'Botafogo', 'Vasco', 'Athletico', 'Goiás'

for posi, c in enumerate(times):
    print(f'o {posi+1}º colocado é {c}')

# Primeiros cinco colocados
print(times[:5])
# Quatro ultims times
print(times[-4:])
# Deixando em Ordem alfabetica
print(sorted(times))
# Mostrando a posição do valor referido
b = 'Bahia'
print(times.index(b)+1)'''

# ----------------------------------------------------------

'''import random

n1 = random.randint(0,20)
n2 = random.randint(0,20)
n3 = random.randint(0,20)
n4 = random.randint(0,20)
n5 = random.randint(0,20)

valores = n1, n2, n3, n4, n5

print(valores)
# Maior Valor
print(max(valores))
# Menor
print(min(valores))'''

# ----------------------------------------------------------

'''tupla = (int(input('Valor 1: ')),
         int(input('Valor 2: ')),
         int(input('Valor 3: ')),
         int(input('Valor 4: ')))

print(f'vc digitou {tupla}')
# Quantas vezes apareceram o valor em parametro
print(tupla.count(9))
if 3 in tupla:
    print(f'o primeiro valor 3, esta na posição {tupla.index(3)}')
else:
    print('Não tem 3')
for n in tupla:
    if n % 2 == 0:
        print(f'os valores pares são: {n}')'''

# ----------------------------------------------------------

'''lista = 'Arroz', 25.90, 'Feijao', 10.50, 'Farinha', 5.80, 'Suco', 1.99


# for iniciando da posicao zero ate o final da lista
for item in range(0, len(lista)):
    # se o valor for divisivel por dois, imprima
    if item % 2 == 0:
        print(f'{lista[item]:.<30}', end= '')
    else:
        print(f'R${lista[item]:>7.2f}')'''

# ----------------------------------------------------------

'''tupla = (str(input('palavra 1: ')),
         str(input('palavra 2: ')),
         str(input('palavra 3: ')),
         str(input('palavra 4: ')))

for p in tupla:
    print(f'\n na palavra {p} temos ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')'''
