''' Ensinando a brecar um while
while True:
 if passo:

 if pula:

 # Finaliza a repetição
 break

print('FIM')'''

# ----------------------------------------------------------
'''cont = 1
while True:
    print(cont, '->', end='')
    cont += 1
print('ACABOU')'''

# ----------------------------------------------------------

'''n = cont = soma = 0
while True:
    n = int(input('Digite um numero: '))

    if n == 999:
        break
    soma += n
    cont += 1
print(f'soma {soma}, qtd {cont}')'''

# ----------------------------------------------------------

'''while True:
    tab = 0
    num = int(input('Digite um numero: '))
    if num < 0:
        break
    while tab < 10:
        tab += 1
        res = num * tab
        print(f' {num} X {tab} = {res}')

print('Acabou')'''

# ----------------------------------------------------------
'''import random

soma = result = cont = 0
pcvalue = random.randint(0, 5)

while True:
    user = int(input('--Par ou Impar?-- '
                     '\n [1] Impar'
                     '\n [2] Par '))

    if user > 2 or user < 1:
        print('Valores Invalidos!')
        break

    elif user == 1:
        pc = 2
    else:
        pc = 1

    valor = int(input('insira um valor até 5: '))

    if valor > 5 and valor < 0:
        print('Numero Não suportado!')
        break

    soma = pcvalue + valor
    result = soma % 2
    if user == 1 and result == 1:
        cont += 1
        print(f'valor da maquina {pcvalue}, Você Ganhou!')
    elif user == 1 and result == 0:
        print('Você perdeu!')
        break
    elif user == 2 and result == 0:
        cont += 1
        print(f'valor da maquina {pcvalue}, Você Ganhou!')
    elif user == 2 and result == 1:
        print('Você perdeu!')
        break
print(f'Vitórias {cont}, valor da maquina {pcvalue}')'''

# ----------------------------------------------------------

'''tot18 = totH = totM20 = 0
while True:
    idade = int(input('Insira a idade da pessoa: '))
    genero = ' '
    while genero not in 'MF':
        genero = str(input('Insira o genero da pessoa, sendo [M ou F]: ')).upper().strip()[0]
    if idade >= 18:
        tot18 += 1
    if genero == 'M':
        totH += 1
    if genero == 'F' and idade < 20:
        totM20 += 1

    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if resp == 'N':
        break
print(f'Total de pessoas com mais de 18 anos: {tot18}')
print(f'Ao todo temos {totH} homens cadastrados.')
print(f'Ao todo temos {totM20} mulheres com menos de 20 anos.')'''

# ----------------------------------------------------------

'''vCompra = pMMil = cont = menor = 0
nBarato = ' '
while True:
    nome = str(input('Nome do alimento: ')).strip()
    valor = float(input('Valor: '))

    while valor <= 0:
        valor = float(input('Valor invalido!: '
                            '\n Insira um novo valor: '))

    if valor > 1000:
        pMMil += 1

    cont += 1
    vCompra += valor
    if cont == 1 or valor < menor:
        menor = valor
        nBarato = nome
   
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if resp == 'N':
        break
print(f'Total gasto na compra:  {vCompra:2.2f}')
print(f'Ao todo temos {pMMil} produtos maior que mil reais')
print(f'o produto mais barato foi {nBarato} que custa  {menor:.2f}')'''

# ----------------------------------------------------------

'''totalced = total = 0
ced = 50

valor = int(input('Insira o valor a ser sacado: '))
total = valor

while True:

    if valor < 0:
        print('Valor Invalido, insira um numero acima de 0.')
        break
    if total >= ced:
        total -= ced
        totalced += 1
    else:
        if totalced > 0:
            print(f'total de {totalced} cedulas de R${ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totalced = 0
        if total == 0:
            break
print('Até a proxima!')'''
