from random import randint
from re import fullmatch
from copy import deepcopy
from time import sleep
import tkinter as tk

class Application(tk.Frame):
    def __init__(self,master=None):
        super().__init__(master)
        self.master = master
        self.title = tk.Label(text="Tic Tac Toe",font="Verdana 56")
        self.title.grid(row=0,columnspan=3,sticky="ew")
        self.board = [
            ["","",""],
            ["","",""],
            ["","",""]
            ]
        self.labelText = tk.StringVar()
        self.__createWidgets__()
        self.turn = 0
        self.playerTurn = tk.BooleanVar()
        self.playerTurn.set(False)
        self.gameover = {"Gameover": False, "Winner": None}

    def __createWidgets__(self):
        self.gameStatus = tk.Label(textvariable=self.labelText,font="Verdana 30")
        self.gameStatus.grid(row=1,columnspan=3,sticky="ew")
        self.buttons = [
            [
                tk.Button(text=self.board[0][0],font="Verdana 56",width=5,height=2,command=lambda: self.__playerchoice__((0,0))),
                tk.Button(text=self.board[0][1],font="Verdana 56",width=5,height=2,command=lambda: self.__playerchoice__((0,1))),
                tk.Button(text=self.board[0][2],font="Verdana 56",width=5,height=2,command=lambda: self.__playerchoice__((0,2)))
            ],
            [
                tk.Button(text=self.board[1][0],font="Verdana 56",width=5,height=2,command=lambda: self.__playerchoice__((1,0))),
                tk.Button(text=self.board[1][1],font="Verdana 56",width=5,height=2,command=lambda: self.__playerchoice__((1,1))),
                tk.Button(text=self.board[1][2],font="Verdana 56",width=5,height=2,command=lambda: self.__playerchoice__((1,2)))
            ],
            [
                tk.Button(text=self.board[2][0],font="Verdana 56",width=5,height=2,command=lambda: self.__playerchoice__((2,0))),
                tk.Button(text=self.board[2][1],font="Verdana 56",width=5,height=2,command=lambda: self.__playerchoice__((2,1))),
                tk.Button(text=self.board[2][2],font="Verdana 56",width=5,height=2,command=lambda: self.__playerchoice__((2,2)))
            ]
        ]
        # self.button11 = tk.Button(text=self.board[0][0],font="Verdana 56",width=5,height=2,command=lambda: self.__playerchoice__((0,0)))
        # self.button11.grid(row=2,column=0, sticky="ew")
        # self.button12 = tk.Button(text=self.board[0][1],font="Verdana 56",width=5,height=2,command=lambda: self.__playerchoice__((0,1)))
        # self.button12.grid(row=2,column=1, sticky="ew")
        # self.button13 = tk.Button(text=self.board[0][2],font="Verdana 56",width=5,height=2,command=lambda: self.__playerchoice__((0,2)))
        # self.button13.grid(row=2,column=2, sticky="ew")
        # self.button21 = tk.Button(text=self.board[1][0],font="Verdana 56",width=5,height=2,command=lambda: self.__playerchoice__((1,0)))
        # self.button21.grid(row=3,column=0, sticky="ew")
        # self.button22 = tk.Button(text=self.board[1][1],font="Verdana 56",width=5,height=2,command=lambda: self.__playerchoice__((1,1)))
        # self.button22.grid(row=3,column=1, sticky="ew")
        # self.button23 = tk.Button(text=self.board[1][2],font="Verdana 56",width=5,height=2,command=lambda: self.__playerchoice__((1,2)))
        # self.button23.grid(row=3,column=2, sticky="ew")
        # self.button31 = tk.Button(text=self.board[2][0],font="Verdana 56",width=5,height=2,command=lambda: self.__playerchoice__((2,0)))
        # self.button31.grid(row=4,column=0, sticky="ew")
        # self.button32 = tk.Button(text=self.board[2][1],font="Verdana 56",width=5,height=2,command=lambda: self.__playerchoice__((2,1)))
        # self.button32.grid(row=4,column=1, sticky="ew")
        # self.button33 = tk.Button(text=self.board[2][2],font="Verdana 56",width=5,height=2,command=lambda: self.__playerchoice__((2,2)))
        # self.button33.grid(row=4,column=2, sticky="ew")

        self.buttons[0][0].grid(row=2,column=0, sticky="ew")
        self.buttons[0][1].grid(row=2,column=1, sticky="ew")
        self.buttons[0][2].grid(row=2,column=2, sticky="ew")
        self.buttons[1][0].grid(row=3,column=0, sticky="ew")
        self.buttons[1][1].grid(row=3,column=1, sticky="ew")
        self.buttons[1][2].grid(row=3,column=2, sticky="ew")
        self.buttons[2][0].grid(row=4,column=0, sticky="ew")
        self.buttons[2][1].grid(row=4,column=1, sticky="ew")
        self.buttons[2][2].grid(row=4,column=2, sticky="ew")

        self.playbutton = tk.Button(text="Play", font="Verdana 12",command=self.game)
        self.playbutton.grid(row=5,column=0,sticky="ew")

        self.continuebutton = tk.Button(text="Continue", font="Verdana 12", command=lambda: self.playerTurn.set(True))
        self.continuebutton.grid(row=5,column=2,sticky="ew")

    def __simulate__(self,board,turn):
        boardClone = deepcopy(board)
        goodResults = []
        drawResults = []
        badResults = []
        result = list()
        #print(f"goodResults={goodResults}\ndrawResults={drawResults}\nbadResults={badResults}")
        for i in range(3):
            for j in range(3):
                #boardClone2 = deepcopy(board)
                #print(f"i,j={i,j}, board[i][j]={boardClone[i][j]}\nTurn={turn}\nResults={result}\nGoodResults={goodResults}\nDrawResults={drawResults}\nBadResults={badResults}")
                if not boardClone[i][j]:
                    if turn%2:
                        boardClone[i][j] = "X"
                    else:
                        boardClone[i][j] = "O"
                    gameover = self.__gameOver__(boardClone)
                    if gameover["Gameover"] and gameover["Winner"] == "O":
                        result.append(1)
                    elif gameover["Gameover"] and gameover["Winner"] == "X":
                        result.append(-1)
                    elif gameover["Gameover"]:
                        result.append(0)
                    else:
                        #print("calling simulate again",boardClone)
                        result.append(self.__simulate__(boardClone,turn+1))
                    if turn == self.turn and result[-1] == 1:
                        goodResults.append((i,j))
                    elif turn == self.turn and result[-1] == 0:
                        drawResults.append((i,j))
                    elif turn == self.turn and result[-1] == -1:
                        badResults.append((i,j))
                    boardClone[i][j] = ""
        #print(f"Turn={turn}\nResults={result}\nGoodResults={goodResults}\nDrawResults={drawResults}\nBadResults={badResults}")
        if len(goodResults) > 0:
            return goodResults[randint(0,len(goodResults)-1)]
        elif len(drawResults) > 0:
            return drawResults[randint(0,len(drawResults)-1)]
        elif len(badResults) > 0:
            return badResults[randint(0,len(badResults)-1)]
        elif turn % 2:
            return min(result)
        return max(result)

    def __computerTurn__(self):
        self.labelText.set("PC turn.")
        sleep(randint(0,3))
        result = self.__simulate__(self.board,self.turn)
        self.board[result[0]][result[1]] = "O"
        self.__updateButtons__()

    def __playerchoice__(self,button):
        self.choice = button
        # self.button11.configure(state="disabled")
        # self.button12.configure(state="disabled")
        # self.button13.configure(state="disabled")
        # self.button21.configure(state="disabled")
        # self.button22.configure(state="disabled")
        # self.button23.configure(state="disabled")
        # self.button31.configure(state="disabled")
        # self.button32.configure(state="disabled")
        # self.button33.configure(state="disabled")

    def __playerTurn__(self):
        self.labelText.set("Player turn.")
        # while True:
        #     choice = input("Please choose the position of your '' in the form '(x,y)' with x = 1-3 defining the column, y = 1-3 defining the row.\n")
        #     if not fullmatch("[123]-[123]",choice):
        #         print("Incorrect input, please try again.")
        #         continue
        #     choice = choice.split("-")
        #     if self.board[int(choice[1])-1][int(choice[0])-1]:
        #         print("This position is already taken.")
        #         continue
        #     self.board[int(choice[1])-1][int(choice[0])-1] = "X"
        #     break
        self.board[self.choice[0]][self.choice[1]] = "X"
        self.__updateButtons__()

    def __updateButtons__(self):
        self.buttons[0][0].configure(text=self.board[0][0])
        self.buttons[0][1].configure(text=self.board[0][1])
        self.buttons[0][2].configure(text=self.board[0][2])
        self.buttons[1][0].configure(text=self.board[1][0])
        self.buttons[1][1].configure(text=self.board[1][1])
        self.buttons[1][2].configure(text=self.board[1][2])
        self.buttons[2][0].configure(text=self.board[2][0])
        self.buttons[2][1].configure(text=self.board[2][1])
        self.buttons[2][2].configure(text=self.board[2][2])

    def __gameOver__(self,board):
        gameover = False
        winner = None
        if ["X","X","X"] in board:
            gameover = True
            winner = "X"
        elif ["O","O","O"] in board:
            gameover = True
            winner = "O"
        else:
            for i in range(3):
                if [board[0][i],board[1][i],board[2][i]] == ["X","X","X"]:
                    gameover = True
                    winner = "X"
                    break
                elif [board[0][i],board[1][i],board[2][i]] == ["O","O","O"]:
                    gameover = True
                    winner = "O"
                    break
            if [board[0][0],board[1][1],board[2][2]] == ["X","X","X"] or [board[0][2],board[1][1],board[2][0]] == ["X","X","X"]:
                gameover = True
                winner = "X"
            elif [board[0][0],board[1][1],board[2][2]] == ["O","O","O"] or [board[0][2],board[1][1],board[2][0]] == ["O","O","O"]:
                gameover = True
                winner = "O"
            elif "" not in board[0] and "" not in board[1] and "" not in board[2]:
                gameover = True
        
        self.gameover = {"Gameover": gameover, "Winner": winner}
        return self.gameover

    # def __refresh__(self):
    #     self.gameStatus.configure(text=)


    def game(self):
        self.start = randint(0,1)
        for self.turn in range(self.start,9+self.start):
            print("turn ",self.turn)
            self.makeTurn(self.turn)
            
            self.__gameOver__(self.board)
            if self.gameover["Gameover"]:
                break
            print(self.board)

        return self.gameover

    def makeTurn(self,turn):
        if turn % 2:
            print("Player turn")
            self.continuebutton.wait_variable(self.playerTurn)
            self.__playerTurn__()
        else:
            #print("PC Turn\n",self.board)
            self.__computerTurn__()
            #print("After PC Turn",self.board)

class Tictactoe:

    def __init__(self):
            pass
    

              
root = tk.Tk()
app = Application(master=root)
app.mainloop()