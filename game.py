from random import randint
from re import fullmatch
from copy import deepcopy

class Tictactoe:

    def __init__(self):
        self.board = [["","",""],["","",""],["","",""]]
        self.turn = 0
        self.gameover = {"Gameover": False, "Winner": None}
            
    def __computerTurn__(self):
        result = self.__simulate__(self.board,self.turn)
        self.board[result[0]][result[1]] = "O"
    
    def __playerTurn__(self):
        while True:
            choice = input("Please choose the position of your '' in the form '(x,y)' with x = 1-3 defining the column, y = 1-3 defining the row.\n")
            if not fullmatch("[123]-[123]",choice):
                print("Incorrect input, please try again.")
                continue
            choice = choice.split("-")
            if self.board[int(choice[1])-1][int(choice[0])-1]:
                print("This position is already taken.")
                continue
            self.board[int(choice[1])-1][int(choice[0])-1] = "X"
            break

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

    def game(self):
        self.start = randint(0,1)
        for self.turn in range(self.start,9+self.start):
            if self.turn % 2:
                self.__playerTurn__()
            else:
                print("PC Turn\n",self.board)
                self.__computerTurn__()
                print("After PC Turn",self.board)
            self.__gameOver__(self.board)
            if self.gameover["Gameover"]:
                break
            print(self.board)

        return self.gameover
                
T = Tictactoe()
print(T.game())