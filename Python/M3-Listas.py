''' Cria e Adiciona um item no final da lista, insere mais um'''
# .append('')

'''adiciona um item na posição informada'''
# .insert(0,'')

# ----------------------------------------------------------

'''Deleta o intem na posição desejada '''
# del lanche[3]

'''Pode apagar tambem usando pop passando a posição'''
# lanche.pop(3)

'''Tambem usado para  apagar o primeiro valor passando por paremetro'''
# lanche.remove('')

'''Deleta o ultimo item'''
# lanche.pop()

# ----------------------------------------------------------

'''Organizando em ordem a lista'''
# valores.sort()

'''Organizando a lista em ordem reversa'''
# valores.sort(reverse=True)

# ----------------------------------------------------------

'''Saber o tamanho da lista'''
# len(valores)

'''Criando uma lista com valores numericos iniciando em 4 e terminando em 10'''
# valores = list(range(4,11)

'''Inserindo valores numerico em uma lista'''
# valores = [8,5,4,6,3]

'''Copiando um lista '''
# a = [2, 3, 4, 7]
# b = a[:]

# ----------------------------------------------------------

'''num = [2, 5, 9, 1]
num[2] = 10
num.insert(0, 'Dois')
print(num)'''

'''valores = []
for cont in range(0, 5):
    valores.append(int(input('Digite um valor: ')))

for c, v in enumerate(valores):
    print(f'na posição {c}, encontrei oo valor {v}...')
print('Final')'''

# ----------------------------------------------------------

'''Copiando um lista '''
# a = [2, 3, 4, 7]
# b = a[:]

# ----------------------------------------------------------

'''mai = men = 0

valores = []
for c in range(0, 5):
    valores.append(int(input(f'Digite um valor para a posição {c}: ')))
    if c == 0:
        mai = men = valores[c]
    else:
        if valores[c] > mai:
            mai = valores[c]
        if valores[c] < men:
            men = valores[c]

for c, v in enumerate(valores):
    if v == mai:
        print(f'maior valor {mai} na posição {c}')

for c, v in enumerate(valores):
    if v == men:
        print(f'menor valor {men} na posição {c}')

print('Final')'''

# ----------------------------------------------------------

'''valores = []
while True:
    valor = int(input(f'Digite um valor: '))
    if valor in valores:
        print('Não é possivel inserir este valor')
        break

    else:
        valores.append(valor)
valores.sort()
print(f'Sua lista é {valores}')'''

# ----------------------------------------------------------

'''valores = []
for c in range(0, 5):
    n = int(input(f'Digite um valor: '))
# se o contador foi igual a zero ou o valor menor que o ultimo valor da lista 
    if c == 0 or n > valores[-1]:
        valores.append(n)
        print(f'Adicionado ao final da lista.')
    else:
        pos = 0
        while pos < len(valores):
            if n <= valores[pos]:
                valores.insert(pos,n)
                print(f'Adicionado na posição {pos}')
                break
            pos += 1
print(f'os valores digitados foram {valores}')'''

# ----------------------------------------------------------

'''valores = []
cont = 0
resp = ''
while resp in 'Ss':
    valor = int(input(f'Digite um valor: '))
    if valor in valores:
        print('Não é possivel inserir este valor')
        break
    else:
        valores.append(valor)
        cont += 1
    resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]

if 5 in valores:
    print('o numero 5 existe')
else:
    print('o numero 5 não existe')
    
print(f'{cont} numeros digitados')
valores.sort(reverse=True)
print(f'ordem decrescente {valores}')'''

# ----------------------------------------------------------

'''lista1 = []
lista2 = []
lista3 = []
for c in range(0, 10):
    valor = int(input(f'Digite um valor: '))
    if valor in lista1:
        print('Não é possivel inserir este valor')
        break
    else:
        lista1.append(valor)

    if valor % 2 == 0:
            lista2.append(valor)
    else:
            lista3.append(valor)

print(f'Lista normal {lista1}')
print(f'Lista de numeros pares {lista2}')
print(f'Lista de mumeros impares {lista3}')'''

# ----------------------------------------------------------

'''expre = str(input('Digite a expressão: '))
pilha = []
for simb in expre:
    if simb == '(':
        pilha.append('(')

    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Sua Expressão esta valida')
else:
    print('Sua Expressão esta invalida')'''

# ----------------------------------------------------------

'''lista dentro de listas'''
'''pessoas = [['Gustavo', 23], ['Kenny', 26], ['Guilherme', 19]]

for p in pessoas:
    print(p)

galera = list()

for c in range(0,3):
    galera.append(str(input('Digite o nome: ')))
    galera.append(int(input('Digite a idade: ')))
print(galera)'''

# ----------------------------------------------------------

'''temp = []
princ = []
cont = 0
max = min = 0

while True:
    temp.append(str(input('Digite um nome: ')).strip())
    temp.append(float(input('Digite o peso: ')))

    if len(princ) == 0:
        max = min = temp[1]
    else:
        if temp[1] > max:
            max = temp[1]
        if temp[1] < min:
            min = temp[1]
    princ.append(temp[:])
    temp.clear()
    cont += 1

    resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if resp == 'N':
        break
print(f'o total de pessoas cadastradas são: {cont}')
print(f'o maior peso foi {max}, peso de ', end='')
for p in princ:
    if p[1] == max:
        print(f'{p[0]}, ', end='')

print()
print(f'o menor peso foi {min},  peso de ', end='')
for p in princ:
    if p[1] == min:
        print(f'{p[0]}, ', end='')'''

# ----------------------------------------------------------

'''numeros = [[],[]]
num = 0

for n in range(1, 8):
    numero = int(input(f'Insira o {num+1}º numero: '))
    num += 1
    if numero % 2 == 0:
        numeros[0].append(numero)
    else:
        numeros[1].append(numero)
numeros[0].sort()
numeros[1].sort()
print(f'Numeros pares {numeros[0]}')
print(f'Numeros impares {numeros[1]}')'''

# ----------------------------------------------------------

'''matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
cont = 0

for l in range(0, 3):
    for c in range(0, 3):
        matrix[l][c] = int(input(f'Digite um valor para {l}, {c}: '))

print('-=' * 30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matrix[l][c]:^5}]', end='')
    print()'''

# ----------------------------------------------------------

'''matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
somapar = somaterce = maior = 0

for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para {l}, {c}: '))

print('-=' * 30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
        if matriz[l][c] % 2 == 0:
            somapar += matriz[l][c]
    print()
print('-=' * 30)
print(f'A soma dos valores pares são:  {somapar}')
for l in range(0, 3):
    somaterce += matriz[l][2]
print(f'A soma da terceira coluna é {somaterce}')
for c in range(0, 3):
    if c == 0:
        maior = matriz[1][c]
    elif matriz[1][c] > maior:
        maior = matriz[1][c]
print(f'O maior elemento da segunda linha é {maior}')'''

# ----------------------------------------------------------

'''from random import randint

lista = list()
jogos = list()

qtd = int(input('Insira quantas apostas você quer fazer: '))
tot = 0
while tot <= qtd:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print(f'Os numeros sorteados foram: {jogos}')'''

# ----------------------------------------------------------

'''alunos = list()

while True:
    nomealuno = (str(input('Digite um nome: ')).upper().strip())
    n1 = (float(input('Digite a primeira nota: ')))
    n2 = (float(input('Digite a segunda nota: ')))
    media = (float((n1 + n2) / 2))
    alunos.append([nomealuno, [n1, n2], media])

    resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if resp == 'N':
        break

nome = str(input('Qual o nome do Aluno? ')).upper().strip()
for c, n in enumerate(alunos):
    if nome in alunos[c][0]:
        print(f'Nome: {n[0]}')
        print(f'Notas: {n[1]}')
        print(f'Segunda Nota: {n[2]}')
    else:
        print(f'na posição {c} não foi encontrado esse nome.')
        continue
print()
print('Você Saiu')'''

