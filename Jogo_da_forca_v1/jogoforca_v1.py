# -*- coding: utf-8 -*-

"""
Jogo da Forca 1.0
24/05/2020

Desenvolvido por: Daniel Lopes
E-mail: ddanielssoares@gmail.com

"""

import random

# Board (tabuleiro)
forca_img = ['''

+---+
|   |
    |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
|   |
    |
    |
=========''', '''

 +---+
 |   |
 O   |
/|   |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/    |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/ \  |
     |
=========''']

versao = '1.0'


# Classe
class Boneco:
    palavra = str()
    palavraOrigem = str()
    # Método Construtor
    def __init__(self, palavr):
        palavraOrigem = palavr[0]
        self.palavra = palavr[0]
        tamanho = len(self.palavra)
        statusGame = False

    # Método para adivinhar a letra
    def advinha(self, letra):
        if letra.lower() in self.palavra.lower():
            self.palavra.replace(letra.lower(), " ")
            return True
        else:
            return False
    # Método para verificar se o jogo terminou
    def fim_jogo(self, acertos, erros):
        if (erros == 5) or (acertos == len(self.palavra)):
            return True
        else:
            return False


    # Método para verificar se o jogador venceu
    def vitoria(self):
        if self.statusGame:
            return True
        else:
            return False

    # Método para não mostrar a letra no board
    def esconder_palavra(self, controle):
        if controle:
            print('show')
        else:
            espaco = '_' * len(self.palavra)
            print('Palavra: '+'_' * len(self.palavra))

    # Método para checar o status do game e imprimir o board na tela
    def status_jogo(self, acertos, erros):
        if acertos == len(self.palavra):
            self.statusGame = True
        elif erros == 5:
            self.statusGame = False





# Função para ler uma palavra de forma aleatória do banco de palavras
def rand_palavra():
    with open("palavras.txt", "rt") as bancoPalavras:
        banco = bancoPalavras.readlines()
    return banco[random.randint(0, len(banco) - 1)].split()


# Função Main - Execução do Programa
def main():
    # Boas Vindas ao jogo:
    print('Bem vindo ao Jogo da Forca v{}\n'.format(versao) +
          'Desenvolvido por Daniel Lopes\n')

    # Objeto do tipo Boneco
    game = Boneco(rand_palavra())

    # Variáveis de controle
    acertos = 0
    erros = 0

    acertoBin = False

    # Enquanto o jogo não tiver terminado, print do status, solicita uma letra e faz a leitura do caracter
    while True:

        # Verifica se o jogo acabou, se não imprime o placar atual
        if game.fim_jogo(acertos,erros):
            break
        else:
            print(forca_img[erros])
            print('Acertos: {0} Erros: {1}\n'.format(acertos, erros) + '='*10)
            if acertoBin:
                game.esconder_palavra(True)
            else:
                game.esconder_palavra(False)

        # Solicita a letra para o jogador
        letraInput = input('\nDigite uma letra: ')

        # Debug
        if letraInput == 'adm_resposta':
            print(game.palavra)
            continue

        # Verifica se a letra está correta
        if game.advinha(letraInput):
            acertos += 1
            game.palavra = game.palavra.replace(letraInput, "0")
        else:
            erros += 1


    # Verifica o status do jogo
    game.status_jogo(acertos, erros)

    # De acordo com o status, imprime mensagem na tela para o usuário
    if game.vitoria():
        print('\nParabéns! Você venceu!!')
    else:
        print('\nGame over! Você perdeu.')
        print('A palavra era {}.'.format(game.palavraOrigem))

    print('\nFoi bom jogar com você! Agora vá estudar!\n')


# Executa o programa
if __name__ == "__main__":
    main()

