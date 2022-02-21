from random import randint
import sys


class Menu:
    def __str__(self):
        return "Os comandos são os seguintes:\n \
        'W' ou 'w': Mover para cima\n \
        'S' ou 's': Mover para baixo\n \
        'A' ou 'a': mover para a esquerda\n \
        'D' ou 'd': Mover para a direita\n \
        \t[0, 0, 0, 0]\n \
        \t[0, 0, 0, 0]\n \
        \t[0, 0, 0, 0]\n \
        \t[0, 0, 0, 0]\n"

class Game:
    def __init__(self):
        self.matriz = [[0,0,0,0], \
                       [0,0,0,0], \
                       [0,0,0,0], \
                       [0,0,0,0]]
        # self.matriz = [[1,2,3,4], \
        #                [5,6,7,8], \
        #                [9,10,11,12], \
        #                [13,14,15,16]]
        self.state = 0
    def new_number(self):
        rand_line = randint(0,3)
        rand_colum = randint(0,3)
        
        if self.matriz[rand_line][rand_colum] == 0:
            self.matriz[rand_line][rand_colum] = 2
        else:
            self.new_number()
    
    def print_matriz(self):
        for line in range(4):
            print("[", end="")
            for colum in range(4):
                print(str(self.matriz[line][colum]),end="")
                if colum != len(self.matriz)-1: print(",",end="")
            print("]\n",end="")
            
    def Moviment(self):
        move = input("Movimento:")
        hv_move = 0
        # Right
        if move == "d":
            # Iterar pelos elementos
            for line in range(4):
                for colum in range(3,-1,-1):
                    element = self.matriz[line][colum]
                    # Exlusao do elemento zero e elementos da coluna direita
                    if element != 0 and colum != 3:
                        for colum2 in range(colum+1,4):
                            space = self.matriz[line][colum2]
                            if space == 0:
                                self.matriz[line][colum] = 0
                                self.matriz[line][colum2] = element
                                colum = colum2
                                hv_move = 1
                            elif space == element:
                                self.matriz[line][colum] = 0
                                self.matriz[line][colum2] = element + space
                                hv_move = 1
                                break
                            else:
                                break
            pass            
        # Left
        elif move == "a":
            for line in range(4):
                for colum in range(4):
                    element = self.matriz[line][colum]
                    # Exlusao do elemento zero e elementos da coluna direita
                    if element != 0 and colum != 0:
                        for colum2 in range(colum-1,-1,-1):
                            space = self.matriz[line][colum2]
                            if space == 0:
                                self.matriz[line][colum] = 0
                                self.matriz[line][colum2] = element
                                colum = colum2
                                hv_move = 1
                                continue
                            elif space == element:
                                self.matriz[line][colum2] = element + space
                                self.matriz[line][colum] = 0
                                hv_move = 1
                                break
                            else:
                                break
            pass
        # Up
        elif move == "w":
            for colum in range(4):
                for line in range(4):
                    element = self.matriz[line][colum]
                    # Exlusao do elemento zero e elementos da coluna direita
                    if element != 0 and line != 0:
                        for line2 in range(line-1,-1,-1):
                            space = self.matriz[line2][colum]
                            if space == 0:
                                self.matriz[line][colum] = 0
                                self.matriz[line2][colum] = element
                                line = line2
                                hv_move = 1
                            elif space == element:
                                self.matriz[line2][colum] = element + space
                                self.matriz[line][colum] = 0
                                hv_move = 1
                                break
                            else:
                                break
            pass
        # Down
        elif move == "s":
            for colum in range(4):
                for line in range(3,-1,-1):
                    element = self.matriz[line][colum]
                    # Exlusao do elemento zero e elementos da coluna direita
                    if element != 0 and line != 3:
                        for line2 in range(line+1,4):
                            space = self.matriz[line2][colum]
                            if space == 0:
                                self.matriz[line][colum] = 0
                                self.matriz[line2][colum] = element
                                line = line2
                                hv_move = 1
                            elif space == element:
                                self.matriz[line2][colum] = element + space
                                self.matriz[line][colum] = 0
                                hv_move = 1
                                break
                            else:
                                break
            pass
        else:
            print("Invalid input!")
            self.Moviment()
        if hv_move == 1:    self.new_number()

    # def end(self):
    #   for line in range(4):
    #     for colum in range(4):
    #       element = self.matriz[line][colum]
    #       if element == 0:
    #         break
    #   if element != 0:
    #     self.state = 0
    #     return print("U lose!")
    #     # sys.exit("U lose!")
    #   else:
    #     pass
    
    # Para finalizar o jogo eu tenho que pegar todos os elementos e ver se seus adjacentes são 
        
    def start(self): 
        print(Menu())
        if input("Start the game? (y/n)") == "y":
            self.new_number()
            self.state = 1
        else:
            return print("Jogo finalizado!")
        while (self.state == 1):
            self.print_matriz()
            self.Moviment()

new_game = Game()
new_game.start()