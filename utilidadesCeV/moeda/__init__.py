def aumentar(n, por):
    n = (n / 100) * (por + 100)
    return n


def diminuir(n, por):
    n = (n / 100) * (100 - por)
    return n


def dobro(n):
    n *= 2
    return n


def metade(n):
    n /= 2
    return n


def moeda(n, sit=False):
    met = n / 2
    print(f'R${n:.2f} e sua metade é ', end='')
    if sit:
        print(f'R${met:.2f}')
    else:
        print(f'{met:.2f}')


def resumo(n, aum=0, red=0):
    print('-' * 25)
    print(f'{"RESUMO DO VALOR":^25}')
    print('-' * 25)
    print('Preço Analisado: ', end='')
    print(f'R${n:.2f}')
    print('Dobro do preço: : ', end='')
    print(f'R${dobro(n):.2f}')
    print('Metade do preço: ', end='')
    print(f'R${metade(n):.2f}')
    print(f'{aum}% de aumento: ', end='')
    print(f'R${aumentar(n, aum):.2f}')
    print(f'{red}% de redução: ', end='')
    print(f'{diminuir(n, red):.2f}')
