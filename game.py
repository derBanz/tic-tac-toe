"""
Set task: Creating a tic-tac-toe game.
Method:
* On __init__(), self.board (list) is generated with 9 empty cells in 3 rows and 3 columns and self.turn (in) is set to 0. self.gameover (dict) is also reset.
* game() randomly sets self.turn to 0 or 1. Even turns are considered player turns, odd turns are computer turns and the respective method is called.
* __playerTurn__() asks the player for input in form "x-y" and updates the corresponding cell in self.board.
* __computerTurn__() calls on __simulate()__ to do the heavy lifting. Here Greg Surma's "Unbeatable AI" algorithm is implemented, check https://gsurma.medium.com/tic-tac-toe-creating-unbeatable-ai-with-minimax-algorithm-8af9e52c1e7d#14e6 for the details.
* __gameOver__() checks all possible win conditions and updates self.gameover accordingly.
"""

from random import randint
from re import fullmatch
from copy import deepcopy
from time import sleep

class TicTacToe:

    def __init__(self):
        self.board = [
            ["","",""],
            ["","",""],
            ["","",""]
            ]
        self.turn = 0
        self.gameover = {"Gameover": False, "Winner": None}

    def __repr__(self):
        gameboard = list()
        for row in self.board:
            for cell in row:
                if not cell:
                    gameboard.append(" ")
                else:
                    gameboard.append(cell)
        
        return f"-------------\n| {gameboard[0]} | {gameboard[1]} | {gameboard[2]} |\n| {gameboard[3]} | {gameboard[4]} | {gameboard[5]} |\n| {gameboard[6]} | {gameboard[7]} | {gameboard[8]} |\n-------------"

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
                    if gameover["Gameover"] and gameover["Winner"] == "PC":
                        result.append(1)
                    elif gameover["Gameover"] and gameover["Winner"] == "Player":
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
        print(f"PC turn. This is the current board:\n{self}\nThinking...")
        sleep(randint(0,3))
        result = self.__simulate__(self.board,self.turn)
        self.board[result[0]][result[1]] = "O"

    def __playerTurn__(self):
        print(f"It's your turn. This is the current board:\n{self}")
        while True:
            choice = input("Please choose the position of your 'X' in the form 'x-y' with x = 1-3 defining the row, y = 1-3 defining the column.\n")
            if not fullmatch("[123]-[123]",choice):
                print("Incorrect input, please try again.")
                continue
            choice = choice.split("-")
            if self.board[int(choice[0])-1][int(choice[1])-1]:
                print("This position is already taken.")
                continue
            self.board[int(choice[0])-1][int(choice[1])-1] = "X"
            break
        return self.board

    def __gameOver__(self,board):
        gameover = False
        winner = None
        if ["X","X","X"] in board:
            gameover = True
            winner = "Player"
        elif ["O","O","O"] in board:
            gameover = True
            winner = "PC"
        else:
            for i in range(3):
                if [board[0][i],board[1][i],board[2][i]] == ["X","X","X"]:
                    gameover = True
                    winner = "Player"
                    break
                elif [board[0][i],board[1][i],board[2][i]] == ["O","O","O"]:
                    gameover = True
                    winner = "PC"
                    break
            if [board[0][0],board[1][1],board[2][2]] == ["X","X","X"] or [board[0][2],board[1][1],board[2][0]] == ["X","X","X"]:
                gameover = True
                winner = "Player"
            elif [board[0][0],board[1][1],board[2][2]] == ["O","O","O"] or [board[0][2],board[1][1],board[2][0]] == ["O","O","O"]:
                gameover = True
                winner = "PC"
            elif "" not in board[0] and "" not in board[1] and "" not in board[2]:
                gameover = True
        
        self.gameover = {"Gameover": gameover, "Winner": winner}
        return self.gameover

    def game(self):
        self.turn = randint(0,1)
        while True:
            if self.turn % 2:
                self.__playerTurn__()
            else:
                self.__computerTurn__()
            
            self.__gameOver__(self.board)
            if self.gameover["Gameover"]:
                break
            #print(self.board)
            self.turn += 1
        print(self)
        return self.gameover

T = TicTacToe()
print(T.game())