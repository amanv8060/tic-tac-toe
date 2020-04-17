#Made by
#
# Aman Verma
# verma1090aman@gmail.com
from os import system,name
board=["-","-","-",
       "-","-","-",
       "-","-","-"]
game_on =True
win=None
player="X"

def clear(): 
  
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
  
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear') 

def play():
    
    board_disp()
    while game_on:
        print("\n"+player + "'s turn")
        turn(player)
        check_game(player)
        change_player()
    if win=="X" or win == "O":
        print("\n"+win + " won")
    elif win==None:
        print("\nTie")

def check_game(player):
    global game_on
    global win
    r1=board[0]==board[1]==board[2]==player
    r2=board[3]==board[4]==board[5]==player
    r3=board[6]==board[7]==board[8]==player
    c1=board[0]==board[3]==board[6]==player
    c2=board[1]==board[4]==board[7]==player
    c3=board[2]==board[5]==board[8]==player
    d1=board[0]==board[1]==board[2]==player
    d2=board[3]==board[4]==board[5]==player
    if r1==True or r2==True or r3==True or c1==True or c2==True or c3 ==True or d1==True or d2==True :
        game_on = False
        win = player
    if "-" not in board:
        game_on =False
        win =None

def board_disp():
    clear()
    print(" "+board[0] +  " |",board[1]  + " |",board[2]+"       1 | 2 | 3 ")
    print("-----------     -----------")
    print(" "+board[3] +  " |",board[4]  + " |",board[5]+"       4 | 5 | 6 ")
    print("-----------     -----------")
    print(" "+board[6] +  " |",board[7]  + " |",board[8]+"       7 | 8 | 9 ")

def change_player():
  global player
  if player == "X":
    player = "O"
  elif player == "O":
    player = "X"

def turn(player):
    valid = False
    pos=int(input("Enter postion 1 to 9 : "))
    while not valid:
        while pos not in [1, 2, 3, 4, 5, 6, 7,8,9]:
            pos = int(input("Please enter position 1 to 9: "))
        pos=pos-1
        if board[pos] == "-":
            valid = True
        else:
            print("Occupied, Enter again.")
    
    board[pos]=player
    board_disp()

play()
