# Enquanto não chegar a tal ponto, faça
'''while not value:'''

'''c = 1
while c < 10:
    print(c)
    c = c + 1
print('FIM')'''

# ----------------------------------------------------------

# Põe em maiusculo, tira os espaçõs e pega so a primeira letra se digitarem palavras
# genero = str(input(' Digite seu Genero: ')).upper().strip()[0]

# Enquanto genero não tiver esses valores, faça tal
'''while genero not in 'MmFf':
    genero = str(input(' Digite seu Genero: ')).upper().strip()[0]
print('Ok')'''

# ----------------------------------------------------------

import random

# Verifique se os numero são iguais e contabilize as tentativas
'''numero = int(input(' Digite seu numero até 10: '))

numPc = random.randint(0, 10)
c = 1
while numero != numPc:
    numero = int(input(' Não Deu boa, digite DNV:  '))

    c = c + 1

print('Boa MLK! Foram {} tentativas'.format(c))'''

# ----------------------------------------------------------
'''
num1 = int(input(' Digite seu numero: '))
num2 = int(input(' Digite seu outro numero: '))

opcao = int(input(' Digite seu outro numero: '
                  '\n [1] Somar'
                  '\n [2] multiplicar'
                  '\n [3] maior'
                  '\n [4] novos numeros'
                  '\n [5] Sair do programa '))

while opcao > 5:
    opcao = int(input(' Errado, Digite dentre essas opções:  '
                      '\n [1] Somar'
                      '\n [2] multiplicar'
                      '\n [3] maior'
                      '\n [4] novos numeros'
                      '\n [5] Sair do programa '))
if opcao == 1:
    soma = 0
    soma = num1 + num2
    print(soma)
elif opcao == 2:
    multi = 0
    multi = num1 * num2
    print(multi)
elif opcao == 3:
    if num1 > num2:
        print(num1)
    else:
        print(num2)
elif opcao == 4:
    num1 = int(input(' Digite um novo numero: '))
    num2 = int(input(' Digite outro novo numero: '))
    print('{}, {}'.format(num1, num2))
elif opcao == 5:
    print('Você saiu do programa!')
    exit()
print('Você saiu do programa!')'''

# ----------------------------------------------------------

'''num1 = int(input(' Digite seu numero: '))
c = num1
mult = num1

while c != 1:
    if c == mult:
        mult = (c * (c - 1))
    else:
        mult = mult * (c - 1)
    c = c - 1
print(mult)'''

# ----------------------------------------------------------

'''primeiro = int(input('Insira o valor primeiro: '))

razao = int(input( 'valor da razao: '))

decimo = primeiro+(10-1) * razao

for c in range(primeiro, decimo + razao, razao ):
    print('{}'.format(c), end='=>')
print('FIM')'''

# ----------------------------------------------------------

'''menu = int(input('---MENU---'
                 '\n [0] Para sair'
                 '\n [1] Para informar os valores '))

while menu != 1 and menu != 0:
    menu = int(input('Insira valores de 0 ou 1'
                     '\n---MENU---'
                     '\n [0] Para sair'
                     '\n [1] Para informar os valores '))

if menu == 1:
    primeiro = int(input('Insira o valor primeiro: '))
    razao = int(input('valor da razao: '))
    cont = int(input(' Informe o valor dos argumentos: '))
    c = 0
    while cont != 0:
        c = primeiro + (cont - 1) * razao
        print('{}'.format(c), end='<=')
        cont = cont - 1
    print('FIM')
elif menu == 0:
    print('Você Saiu')
    exit()'''

# ----------------------------------------------------------

'''numero = int(input(' Digite seu numero: '))
c = 0
soma = 0

while numero != 999:
    soma += numero
    c += 1
    numero = int(input(' Não Deu boa, digite DNV:  '))
print(f'Boa MLK! Foram {c} tentativas, soma {soma}')'''

# ----------------------------------------------------------

'''n = int(input(' Quantos termos vc quer mostrar?: '))
t1 = 0
t2 = 1
print(' {}, {} '.format(t1, t2), end='')
cont = 3
while cont <= n:
    t3 = t1 + t2
    print(' -> {} '.format(t3), end='')
    t1 = t2
    t2 = t3

    cont += 1
print('FIM')'''

# ----------------------------------------------------------

'''resp = 'S'
soma = quant = media = 0
while resp in 'Ss':
    num = int(input('Digite um numero: '))
    soma += num
    quant += 1
    if quant == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num

    resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
media = soma / quant
print('Você digitou {} numeros, e a média foi {} '.format(quant, media))
print('o maior valor foi {}, e o menor foi {}'.format(maior, menor))'''

# ----------------------------------------------------------

