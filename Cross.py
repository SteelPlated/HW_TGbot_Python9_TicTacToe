import collections

from telegram.ext import Filters
from telegram import Bot
from telegram.ext import Updater, CommandHandler, MessageHandler, CallbackContext
bot = Bot(token='5572182114:AAEGaREq4XiSrXJdUjxRNteu2Bd0pBD4VUM')

def cross(update: Updater, context: CallbackContext):
    msg=update.message.text
    print(msg)
    #items=msg.split()
    

    
    board = list(range(1,10))

    def draw_board(board):
        #print ("-" * 13)
        #update.message.reply_text(f'"-", {13}')
        for i in range(3):
            #print ("|", board[0+i*3], "|", board[1+i*3], "|", board[2+i*3], "|")
            update.message.reply_text(f'"|", {board[0+i*3]}, "|", {board[1+i*3]}, "|", {board[2+i*3]}, "|"')
            #print ("-" * 13)
            #update.message.reply_text(f'"-", {13}')
    
    def take_input(player_token):
        valid = False
        
        while not valid:
            
            #player_answer = input("Куда поставим " + player_token+"? ")
                      
            player_answer = update(msg, 'Отправьте мне сообщение')
                        
            try:
                player_answer = int(player_answer)
            except:
                #print ("Некорректный ввод. Вы уверены, что ввели число?")
                update.message.reply_text(f"Некорректный ввод. Вы уверены, что ввели число?")
                continue
            if player_answer >= 1 and player_answer <= 9:
                if (str(board[player_answer-1]) not in "XO"):
                    board[player_answer-1] = player_token
                    valid = True
                else:
                    #print ("Эта клеточка уже занята")
                    update.message.reply_text(f"Эта клеточка уже занята?")
            else:
                #print ("Некорректный ввод. Введите число от 1 до 9 чтобы походить.")
                update.message.reply_text(f"Некорректный ввод. Введите число от 1 до 9 чтобы походить.")

    def check_win(board):
        win_coord = ((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))
        for each in win_coord:
            if board[each[0]] == board[each[1]] == board[each[2]]:
                return board[each[0]]
        return False

    def main(board):
        counter = 0
        win = False
        while not win:
            draw_board(board)
            if counter % 2 == 0:
                take_input("X")
            else:
                take_input("O")
            counter += 1
            if counter > 4:
                tmp = check_win(board)
                if tmp:
                    #print (tmp, "выиграл!")
                    update.message.reply_text(tmp, "выиграл!")
                    win = True
                    break
            if counter == 9:
                #print ("Ничья!")
                update.message.reply_text("Ничья!")
                break
        draw_board(board)

    main(board)
    