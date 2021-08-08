class Board :
    def __init__(self) :
        self.board = [["a","b","c","d"],["e","f","g","h"],["i","j","k"," "]]
    
    def display_board(self,position) :
        print(position[0][0] + '|' + position[0][1] + '|' + position[0][2] + '|' + position[0][3])
        print('-------')
        print(position[1][0] + '|' + position[1][1] + '|' + position[1][2] + '|' + position[1][3])
        print('-------')
        print(position[2][0] + '|' + position[2][1] + '|' + position[2][2] + '|' + position[2][3])
    
    def start_game(self) :
        print("welcome to Sort Game")
        self.display_board(self.board)
        #new_position = Input_Processer.get_input() 

    def switch(self,board,new_input) : #อันนี้ไว้สำหรับเช็คว่า input กะ ตรงที่ว่างอยู่ติดกันหรือเปล่า ละก็สลับที่กัน
        space = " " 
        for i in range(3) :
            for j in range(4) :
                if board[i][j] == " " :
                    row_space = i
                    column_space = j 
        for a in range(3) :
            for b in range(4) :
                if board[a][b] == new_input :
                    row_input = a
                    column_input = b  
        if i - a == 0 or i - a == -1 or i - a == 1 :
            if j - b == 0 or j - b == -1 or j - b == 1 :
                temp = board[i][j]
                board[i][j] = board[a][b]
                board[a][b] = temp




class Input_Processer :
    def get_input(self) :
        position = input("which one do you want to play ---> ")

SortGame_game = Board()
SortGame_game.start_game()