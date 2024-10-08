# Função Interactive Helping System in Python
from time import sleep
def menuInicial():
    frase = 'Python Helping System'
    print('\033[1;30;43m')
    print('♥' * len(frase))
    print(f'  {frase}')
    print('♥' * len(frase))
    print('\033[m')


def acessandoMenu():
    frase = 'Looking for Help ☺'
    print('\033[1;30;46m')
    print('♥' * len(frase))
    print(f'  {frase}')
    print('♥' * len(frase))
    print('\033[m')


while True:
    menuInicial()
    opc = str(input('Função ou Biblioteca? ')).strip().lower()
    if opc in 'fim':
        break
    acessandoMenu()
    sleep(1)
    print(f'\033[1;30;44m')
    help(opc)
