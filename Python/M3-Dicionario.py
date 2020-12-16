''' Declaração de um dicionario'''
# dicionario = {}
# dicionario = dict()

''' Substituindo valores numericos por literais'''
# dados = {'nome': 'Pedro', 'idade': 20}

'''Inserindo dados no dicionario'''
# dados['Sexo'}='M'

''' removendo dados de um dicionario'''
# del dados['idade']


'''retornando todos os valores'''
# print(filme.values())

'''retornando todos as chaves(valores numerico alterados por lietarias)'''
# print(filme.keys())

'''retornando todos os valores e chaves'''
# print(filme.items())

'''Copiando um lista '''
# a = {'Uf': 'PR','Estado': ' Parana'}
# b = a.copy()

# ----------------------------------------------------------

'''nome = str(input('Insira um nome: ')).strip().upper()
media = int(input('Insira a media: '))

if  media >= 0 and media  <= 6 :
    dicionario = {'Nome': nome, 'Media': media, 'Situação': 'Reprovado'}
elif  media >= 7 and media <= 10:
    dicionario = {'Nome': nome, 'Media': media, 'Situação': 'Aprovado'}

print(f'Nome é igual a v')
print(f'A média é igual a {dicionario["Media"]}')
print(f'A Situação é {dicionario["Situação"]}')'''

# ----------------------------------------------------------

'''from random import randint
from operator import itemgetter

listvalor = list()

valores = {'Jogador 1': randint(1, 6),
           'Jogador 2': randint(1, 6),
           'Jogador 3': randint(1, 6),
           'Jogador 4': randint(1, 6),
           'Jogador 5': randint(1, 6),
           'Jogador 6': randint(1, 6), }

listvalor = sorted(valores.items(), key=itemgetter(1), reverse=True)

for c, n in enumerate(listvalor):
    print(f'o {c+1}º foi o {n[0]} com o numero: {n[1]} ')'''

# ----------------------------------------------------------

'''nome = str(input('Insira seu nome: ')).strip().upper()
anonasci = int(input('Seu ano de nascimento: '))
ctps = int(input('Sua CTPS: '))

if ctps == 0:
    dicionario = {'Nome': nome, 'Idade': 2020 - anonasci, 'CTPS': ctps}
    print(f'-=' * 30)
    print(f'\nO nome tem o valor de {dicionario["Nome"]}')
    print(f'A idade tem o valor de {dicionario["Idade"]}')
    print(f'A CTPS tem o valor de {dicionario["CTPS"]}')
else:
    anoCont = int(input('Insira seu ano de contratação: '))
    salario = int(input('Seu salario: '))

    idade = 2020 - anonasci
    aposent =  (anoCont + 65) - 2020
    dicionario = {'Nome': nome, 'Idade': idade, 'CTPS': ctps, 'Ano de Contratação': anoCont,
                  'Salario': salario}

    print(f'-='*30)
    print(f'\nO Nome tem o valor de {dicionario["Nome"]}')
    print(f'O Idade tem o valor de {dicionario["Idade"]}')
    print(f'A CTPS tem o valor de {dicionario["CTPS"]}')
    print(f'A Ano de Contratação tem o valor de {dicionario["Ano de Contratação"]}')
    print(f'Tem o valor de R${dicionario["Salario"]},00')
    print(f'Aposentadoria tem o valor de {aposent}')'''

# ----------------------------------------------------------

'''cont = 1
somaGols = 0
lista = list()

nome = str(input('Insira seu nome: ')).strip().upper()
qtdPartidas = int(input('Quantas Partidas ele fez: '))

for n in range(1, qtdPartidas + 1):
    qtdGols = int(input(f'Quantos Gols ele fez na {cont}º partida? '))
    cont += 1
    lista.append(qtdGols)
    somaGols = somaGols + qtdGols

dicionario = {'Nome': nome, 'Quantidade de Partidas': qtdPartidas, 'Quantidade de Gols': lista, 'Soma': somaGols}

print(f'\nO campo Nome tem o valor de {dicionario["Nome"]}')
print(f'O campo Quantidade de Partidas tem o valor de {dicionario["Quantidade de Partidas"]}')
print(f'O campo Quantidade de Gols tem o valor de {dicionario["Quantidade de Gols"]}')
print(f'\nO campo Soma tem o valor de {dicionario["Soma"]}')
for c, n in enumerate(lista):
    print(f'Na {c+1}º partida ele fez {n}')'''

# ----------------------------------------------------------

'''lista = []
soma = 0
while True:
    dicio = dict()
    dicio['Nome'] = str(input('Digite o Nome: ')).strip().upper()
    dicio['Idade'] = int(input('Digite a idade: '))
    soma += dicio['Idade']
    dicio['Genero'] = str(input('Digite o Genero [M/F]: ')).strip()[0].upper()
    lista.append(dicio)
    del dicio
    resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if resp == 'N':
        break
print(lista)
print(f'O Grupo tem {len(lista)} pessoas')
print(f'A media de idade é {soma / len(lista):.1f} ')
media = soma / len(lista)
for p in lista:
    if p["Genero"] == 'F':
        print(f'A mulheres cadastradas, foram {p["Nome"]}')
print(f'As pessoas acima da média foram: ')
for p in lista:
    if p["Idade"] >= media:
        print('   ', end='')
        for k, v in p.items():
            print(f' {k} = {v} :',  end='')
        print()'''

# ----------------------------------------------------------

'''listaAtlet = list()
while True:
    cont = 1
    lista = list()
    somaGols = 0
    nome = str(input('Insira o nome do jogador: ')).strip().capitalize()
    qtdPartidas = int(input(f'Quantas Partidas {nome} fez: '))

    for n in range(1, qtdPartidas + 1):
        qtdGols = int(input(f'Quantos Gols ele fez na {cont}º partida? '))
        cont += 1
        lista.append(qtdGols)
        somaGols = somaGols + qtdGols

    dicionario = {'Cod': len(listaAtlet), 'Nome': nome, 'Quantidade de Partidas': qtdPartidas,
                  'Quantidade de Gols': lista, 'Soma': somaGols}
    del lista
    listaAtlet.append(dicionario)
    resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if resp == 'N':
        break

print('-=' * 32)
print('Cod' + ' ' * 2 + 'Nome' + ' ' * 2 + 'Partidas' + ' ' * 2 + 'Gols' + ' ' * 2 + 'Total')
print('-' * 30)

for c, n in enumerate(listaAtlet):
    for v, k in n.items():
        print(f'{k} ' + ' ' * 3, end='')
    print()
while True:
    jgd = int(input('Você gostaria de ver os dados de qual jogador? '))
    if jgd >= len(listaAtlet)  :
        print('Erro, esse jogador não existe!')
        continue
    else:
        for c, n in enumerate(listaAtlet):
            if jgd == c:
                print(f'O campo Nome tem o valor de {listaAtlet[jgd]["Nome"]}')
                print(f'O campo Quantidade de Partidas tem o valor de {listaAtlet[jgd]["Quantidade de Partidas"]}')
                print(f'O campo Quantidade de Gols tem o valor de {listaAtlet[jgd]["Quantidade de Gols"]}')
                print(f'O campo Soma tem o valor de {listaAtlet[jgd]["Soma"]}')
                for c, n in enumerate(listaAtlet[jgd]["Quantidade de Gols"]):
                    print(f'Na {c + 1}º partida ele fez {n}')
                print()'''