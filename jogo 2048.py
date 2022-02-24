from random import randint
import sys
import os


class Menu:
    def __str__(self):
        return "Os comandos são os seguintes:\n \
        'W' ou 'w': Mover para cima\n \
        'S' ou 's': Mover para baixo\n \
        'A' ou 'a': mover para a esquerda\n \
        'D' ou 'd': Mover para a direita\n \
        \t[0,0,0,0]\n \
        \t[0,0,0,0]\n \
        \t[0,0,0,0]\n \
        \t[0,0,0,0]\n"

class Game:
    def __init__(self):
        self.matriz = [[0,0,0,0], \
                       [0,0,0,0], \
                       [0,0,0,0], \
                       [0,0,0,0]]
        # self.matriz = [[2048,2048,2048,2048], \
        #                [2048,2048,2048,2048], \
        #                [2048,2048,2048,2048], \
        #                [2048,2048,2048,2048]]
        self.state = 0
    def new_number(self):
        rand_line = randint(0,3)
        rand_colum = randint(0,3)
        
        if self.matriz[rand_line][rand_colum] == 0:
            self.matriz[rand_line][rand_colum] = 2
        else:
            self.new_number()
    
    def print_matriz(self):
        maior = 0
        for line in range(4):
            for column in range(4):
                if self.matriz[line][column] > maior:
                    maior = self.matriz[line][column]
                    
        tamanho = "%" + str(len(str(maior))) + "d"
        for line in range(4):
            print("\t\t\t[", end="")
            for colum in range(4):
                print(tamanho%(self.matriz[line][colum]),end="")
                if colum != len(self.matriz)-1: print(",",end="")
            print("]\n",end="")
            
    def Moviment(self):
        move = input("Movimento:")
        hv_move = 0
        # Right
        if move == "d":
            # Iterar pelos elementos
            for line in range(4):
                for column in range(3,-1,-1):
                    element = self.matriz[line][column]
                    # Exlusao do elemento zero e elementos da coluna direita
                    if element != 0 and column != 3:
                        for colum2 in range(column+1,4):
                            space = self.matriz[line][colum2]
                            if space == 0:
                                self.matriz[line][column] = 0
                                self.matriz[line][colum2] = element
                                column = colum2
                                hv_move = 1
                            elif space == element:
                                self.matriz[line][column] = 0
                                self.matriz[line][colum2] = element + space
                                hv_move = 1
                                break
                            else:
                                break
            pass            
        # Left
        elif move == "a":
            for line in range(4):
                for column in range(4):
                    element = self.matriz[line][column]
                    # Exlusao do elemento zero e elementos da coluna direita
                    if element != 0 and column != 0:
                        for colum2 in range(column-1,-1,-1):
                            space = self.matriz[line][colum2]
                            if space == 0:
                                self.matriz[line][column] = 0
                                self.matriz[line][colum2] = element
                                column = colum2
                                hv_move = 1
                                continue
                            elif space == element:
                                self.matriz[line][colum2] = element + space
                                self.matriz[line][column] = 0
                                hv_move = 1
                                break
                            else:
                                break
            pass
        # Up
        elif move == "w":
            for column in range(4):
                for line in range(4):
                    element = self.matriz[line][column]
                    # Exlusao do elemento zero e elementos da coluna direita
                    if element != 0 and line != 0:
                        for line2 in range(line-1,-1,-1):
                            space = self.matriz[line2][column]
                            if space == 0:
                                self.matriz[line][column] = 0
                                self.matriz[line2][column] = element
                                line = line2
                                hv_move = 1
                            elif space == element:
                                self.matriz[line2][column] = element + space
                                self.matriz[line][column] = 0
                                hv_move = 1
                                break
                            else:
                                break
            pass
        # Down
        elif move == "s":
            for column in range(4):
                for line in range(3,-1,-1):
                    element = self.matriz[line][column]
                    # Exlusao do elemento zero e elementos da coluna direita
                    if element != 0 and line != 3:
                        for line2 in range(line+1,4):
                            space = self.matriz[line2][column]
                            if space == 0:
                                self.matriz[line][column] = 0
                                self.matriz[line2][column] = element
                                line = line2
                                hv_move = 1
                            elif space == element:
                                self.matriz[line2][column] = element + space
                                self.matriz[line][column] = 0
                                hv_move = 1
                                break
                            else:
                                break
            pass
        else:
            print("Invalid input!")
            self.Moviment()
        if hv_move == 1:    self.new_number()

    def end(self):
        for line in range(4):
            for column in range(4):
                elemento = self.matriz[line][column]
                for i in range(-1,+2,2):
                    if (not((line == 0 and i == -1) or (line == 3 and i == 1))):
                        adjacente = self.matriz[line+i][column]
                        if adjacente == elemento or adjacente == 0:
                            break
                for i in range(-1,+2,2):
                    if (not((column == 0 and i == -1) or (column == 3 and i == 1))):
                        adjacente = self.matriz[line][column+i]
                        if adjacente == elemento or adjacente == 0:
                            break
                if adjacente == elemento or adjacente == 0:
                    break
            if adjacente == elemento or adjacente == 0:
                self.state = 1
                break
            else:
                self.state = -1
        
        for line in range(4):
            for column in range(4):
                if(self.matriz[line][column] == 2048):
                    self.state = 2
        
    def start(self): 
        print(Menu())
        if input("Start the game? (y/n)") == "y":
            self.new_number()
            self.state = 1
        else:
            return print("Jogo finalizado!")
        os.system('cls' if os.name == 'nt' else 'clear')
        while (self.state == 1):
            self.print_matriz()
            self.Moviment()
            os.system('cls' if os.name == 'nt' else 'clear')
            self.end()
        if (self.state == -1):
            self.print_matriz()
            print("Você Perdeu!")
        elif (self.state == 2):
            self.print_matriz()
            print("Você Ganhou!")

new_game = Game()
new_game.start()
