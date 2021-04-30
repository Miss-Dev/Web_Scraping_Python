from urllib.request import urlopen
from random import randint
from bs4 import BeautifulSoup
import os

print("**********Bem vindo! Esse código realiza coleta de dados-> elogios no site www.pensador.com************")

html = urlopen('https://www.pensador.com/lista_de_elogios_e_frases_para_elogiar_alguem/')
bs = BeautifulSoup(html.read(), 'html.parser')

# coletando elementos da tag 'blockquote'
elogios = bs.findAll('blockquote')
# imprimindo lista com as frases coletadas
'''
for i, palavra in enumerate(elogios):
    print("{} -> {}\n".format(palavra.get_text(), i))
'''
def menu():
    print("1 - Um elogio!\nAperte qualquer número - Sair")
    try:
        op = int(input())
    except:
        print("Entrada inválida, erro!")
        return 0
    return op


op = menu()
while op==1:
    x = randint(73, len(elogios))
    print(elogios[x].get_text())
    op = menu()
    os.system('cls')

print("O programa foi encerrado!")

