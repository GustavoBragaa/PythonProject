from time import sleep


def leiaInt(msg):
    while True:
        try:
            i = int(input(msg))
        except (ValueError, TypeError):
            print(f'\033[0;31mERRO: Digite um valor Inteiro!\033[m')
            continue
        except KeyboardInterrupt:
            print(f'\033[0;31mUsuario preferiu não informar o numero!\033[m')
            return 0
        else:
            return i


while True:
    print('-' * 29)
    print(f'{"MENU PRINCIPAL":^29}')
    print('-' * 29)
    print('\033[0;33m 1 -\033[m\033[0;34m Ver Pessoas cadastradas\n\033[m'
          '\033[0;33m 2 -\033[m\033[0;34m Cadastrar Nova Pessoa\n\033[m'
          '\033[0;33m 3 -\033[m\033[0;34m Sair do Sistema \033[m')
    print('-' * 29)
    resp = int(leiaInt('\033[0;33mSua opção: \033[m'))
    print('-' * 29)

    if resp > 3 or resp < 1:
        print('\033[0;31mOpção invalida, digite entre 1 e 3.\033[m')
        sleep(2)
        print()

    elif resp == 1:
        arquivo = open('Texto/arquivo.txt', 'r')

        for d in arquivo:
            try:
                s = d[:-1]
                i = int(s)

                if i:
                    print(f'{i:>} Anos')

            except (ValueError, AttributeError):
                print(f'{s:.<22}', end='')
                continue
        arquivo.close()
    elif resp == 2:

        arquivo = open('Texto/arquivo.txt', 'r')
        conteudo = arquivo.readlines()

        nome = str(input('Digite o nome da pessoa: '))
        conteudo.append(nome + '\n')
        idade = str(leiaInt('Digite a idade da pessoa: '))
        conteudo.append(idade + '\n')

        arquivo = open('Texto/arquivo.txt', 'w')
        arquivo.writelines(conteudo)

        arquivo.close()

    elif resp == 3:
        sleep(0.5)
        break
print('\033[0;35mAté Logo\033[m')
