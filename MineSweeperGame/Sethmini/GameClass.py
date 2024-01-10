class Game:
    def start(self):
        while True:
            print("\nFIELD OPTIONS:") #field options for the user
            print("1 - 10x10 with 12 mines")
            print("2 - 15x15 with 18 mines")
            print("3 - 20*20 with 24 mines")

            field_option = input("\nEnter option field (1/2/3) or 'Exit' to quit:") #getting the user input

            if field_option.lower()== 'Exit':
                print("\nEXITING THE GAME!")
                break
            if field_option not in ['1','2','3']:
                print("\nINVALID OPTION! Try Again")
                continue

            size = 10 if field_option=='1' else (15 if field_option=='2' else 20)
            num_mines = 12 if field_option == '1' else (18 if field_option=='2' else 24)

            board=Board(size,num_mines)
            board.place_mines()
            board.calculate_neigh_mines()

            while True:
                board.show_board()
                user_input=input("\nENTER 3 letters in the format[<row letter><column letter><command>:").upper() #getting the user command

                if len(user_input)!=3:
                    print("\nINVALID INPUT! Try Again")
                    continue

                row = ord(user_input[0]) - ord('A')
                col = ord(user_input[1]) - ord('A')
                command = user_input[2]

                if not ('A' <= user_input[0] <= chr(ord('A') + size - 1)) or not ('A' <= user_input[1] <= chr(ord('A') + size - 1)):
                    print("\nINAVALID ROW OR COLUMN LETTER. Try again.") #Error
                    continue

                if command == 'R':
                    game_over = board.reveal(row,col)
                    if game_over:
                        break
                    elif command == 'F':
                        board.flag(row,col)
                    else:
                        print("\nINVALID COMMAND! Try again") #Error

            continue_option = input("\nGAME OVER! Do you want to continue playing(y/n)?:").lower() #ending the game
            if continue_option != 'y':
                print("\nEXITING THE GAME")
                break

if __name__ == "__main__":
    game = Game()
    game.start()

                
