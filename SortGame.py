class Board :
    def __init__(self) :
        self.board = [["","","",""],["","","",""],["","","",""]]
        self.board1 = [["k","j","i","h"],["g","f","e","d"],["c","b","a"," "]]
        self.board2 = [["a","e","i","f"],["b","j","c","k"],["d","g","h"," "]]
        self.board3 = [["f","h","c","i"],["k","a","d","e"],["b","g","j"," "]]
        self.row_space = int
        self.row_input = int
        self.column_space = int
        self.column_input = int
        self.stillplay = True
  
    def display_board(self,position) :
        print(position[0][0] + '|' + position[0][1] + '|' + position[0][2] + '|' + position[0][3])
        print('-------')
        print(position[1][0] + '|' + position[1][1] + '|' + position[1][2] + '|' + position[1][3])
        print('-------')
        print(position[2][0] + '|' + position[2][1] + '|' + position[2][2] + '|' + position[2][3])
  
    def start_game(self) :
        print("welcome to Sort Game")
        print("select your pattern")
        patt = int(input("choose one (1 or 2 or 3)"))
        while self.stillplay == True :
            if patt == 1:
                self.board = self.board1
                self.display_board(self.board)
            elif patt == 2:
                self.board = self.board2
                self.display_board(self.board)
            elif patt == 3:
                self.board = self.board3
                self.display_board(self.board)
            new_position = Input_Processer.get_input(self)
            self.switch(self.board,new_position)
            self.check_result()
            
    def switch(self,board,new_input) : #อันนี้ไว้สำหรับเช็คว่า input กะ ตรงที่ว่างอยู่ติดกันหรือเปล่า ละก็สลับที่กัน
       for i in range(3) :
           for j in range(4) :
               if board[i][j] == " " :
                   
                   self.row_space = i
                   self.column_space = j
       for a in range(3) :
           for b in range(4) :
               if board[a][b] == new_input :
                   
                   self.row_input = a
                   self.column_input = b
       if self.row_space - self.row_input == 0 or self.row_space - self.row_input == -1 or self.row_space - self.row_input == 1 :
           if self.column_space - self.column_input == 0 or self.column_space - self.column_input == -1 or self.column_space - self.column_input == 1 :
               temp = board[self.row_space][self.column_space]
               board[self.row_space][self.column_space] = board[self.row_input][self.column_input]
               board[self.row_input][self.column_input] = temp
 
    def check_result(self):
        if self.board == [["a","b","c","d"],["e","f","g","h"],["i","j","k"," "]] :
            print("Sorted is Finish you Win")
            self.stillplay = False
 
        
 
 
 
class Input_Processer :
   def get_input(self) :
       position = input("which one do you want to switch ---> ")
       return position
 
 
 
 
SortGame_game = Board()
SortGame_game.start_game()
 
 
 
 
 

