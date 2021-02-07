# Modularização
# Dividir um programa grande, aumentar a legibildade, facilitar manutenção.
# Técnicamente importar funções de outros arquivos

'''#Importandoo módulo Uteis
from Uteis import Numeros

num = int(input("Digite um valor: "))
fat = Numeros.fatorial(num)
print(f'o fatorial de {num} é {fat}')'''

# Vantagens:
# Organização
# Falicidade de manutenção
# Ocultação do código detalhado
# Reutilização em outros projetos


# Pacotes (Chamados de Bibliotecas)

# nome padrão de sintaxe dentro dos pacotes __init__.py

# ----------------------------------------------------------
import utilidadesCeV
from utilidadesCeV import dado, moeda

'''num = float(input('Insira um numero: '))

print(utilidadesCeV.aumentar(num))
print(utilidadesCeV.diminuir(num))
print(utilidadesCeV.dobro(num))
print(utilidadesCeV.metade(num))

num = dado.leiaDinheiro('Insira um numero: ')
print(num)
red = int(input('Quantos % de redução: '))
aum = int(input('Quantos % de aumento: '))

moeda.resumo(num, aum, red)'''
