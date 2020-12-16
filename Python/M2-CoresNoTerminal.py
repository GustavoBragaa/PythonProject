#  sintaxe
# \codigo padrao no terminal{style;texto;cor de fundo m
# \033[0;33;44m
# \033[m padrão sem estilo

# códigos de Estilo
# 0 Sem Estilo
# 1 Negrito
# 4 Sublinhado
# 7 Cor Negativo

# Cor De Texto
# 30 White
# 31 Red
# 32 Green
# 33 Yelow
# 34 Blue
# 35 Purple
# 36 Cyan(Ciano)
# 37 Gray

# BackGround
# 40 White
# 41 Red
# 42 Green
# 43 Yelow
# 44 Blue
# 45 Purple
# 46 Cyan(Ciano)
# 47 Gray

# a = 1
# b = 5
# print('\033[4;37;40m Ola Mundo\033[m')
# print('Os Valores São \033[34m{}\033[m e \033[31m{}\033[m'.format(a, b))
# print('Os Valores São {}{}{}'.format('\033[4;32;40m', b, '\033[m'))

# cores = {'limpa': '\033[m',
#         'azul': '\033[34m',
#         'amarelo': '\033[33m',
#         'pretoebranco': '\033[7;30m'}
# print('algo {}{}{}'.format(cores['azul'], b, cores['limpa']))
