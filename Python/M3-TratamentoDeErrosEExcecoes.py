# Sintexa

# try significa 'tente'
'''try:
  operação

except:
  falhou, trate

#else e finally são opcionais
else:
  se deu certo faça isso

finally:
  se der certo ou errado, faça algo'''

# ----------------------------------------------------------

'''try:
    a = int(input('Numero:'))
    b = int(input('Numero:'))
    r = a / b

except Exception as erro:
    print(f'Problema foi: {erro.__class__}')
except (ValueError, TypeError):
    print('problema no tipo.')
else:
    print(f'o resultado é {r}')'''

# ----------------------------------------------------------

'''def leiaInt(msg):
    while True:
        try:
            i = int(input(msg))
        except (ValueError, TypeError):
            print(f'\033[0;3mERRO: Digite um valor Inteiro!\033[m')
            continue
        except KeyboardInterrupt:
            print(f'\033[0;31mUsuario preferiu não informar o numero!\033[m')
            return 0
        else:
            return i'''


'''def leiaFloat(msg):
    while True:
        try:
            r = float(input(msg))
        except (ValueError, TypeError):
            print(f'\033[0;31mERRO:  Digite um valor Real!\033[m')
            continue
        except (KeyboardInterrupt):
            print(f'\033[0;31mUsuario preferiu não informar o numero!\033[m')
            return 0
        else:
            return r


i = int(leiaInt('Digite um numero inteiro: '))
r = float(leiaFloat('Digite um numero real: '))

print(i, r)'''

# ----------------------------------------------------------

'''import urllib.request

try:  # passando o valor da url para a variavel e verificando se ela é valida
    site = urllib.request.urlopen('http://www.pudim.com.br')
except:
    print('Deu erro.')
else:
    print('OK')
    # Este comando mostra todo o codigo do site
    print(site.read())'''
