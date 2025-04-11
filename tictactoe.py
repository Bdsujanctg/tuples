theboard={'7':' ','8':' ','9':' ',
          '4':' ','5':' ','6':' ',
          '1':' ','2':' ','3':' '}
board_keys= [ ]
for key in theboard:
    board_keys.append(key)

def printboard(board):
    print(board['7']+'|'+board['8']+'|'+board['9']+'|')
    print('--+-+--')
    print(board['4']+'|'+board['5']+'|'+board['6']+'|')
    print('--+-+--')
    print(board['1']+'|'+board['2']+'|'+board['3']+'|')
    print('--+-+--')
def game():
  turn='x'
  count=0
  for i in range(10):
      printboard(theboard)
      print('Its your turn to move'+ turn +'.Move to which place?')
      move=input( )

      if theboard[move]==" ":
        theboard[move]= turn
        count+=1
      else:
        print('The place is already filled', "\n Move to which place?")
        continue
      if count >=5:
        
          if theboard['7']==theboard['8']==theboard['9'] !='':
            printboard(theboard)
            print('\n Game over \n')
            print('***'+turn+' won the game ***')
            break
        
          elif theboard['4']==theboard['5']==theboard['6'] !='':
            printboard(theboard)
            print('\n Game over \n')
            print('***'+turn+' won the game ***')
            break

          elif theboard['1']==theboard['2']==theboard['3'] !='':
            printboard(theboard)
            print('\n Game over \n')
            print('***'+turn+' won the game ***')
            break

          elif theboard['7']==theboard['5']==theboard['3'] !='':
            printboard(theboard)
            print('\n Game over \n')
            print('***'+turn+' won the game ***')
            break
          elif theboard['9']==theboard['5']==theboard['1'] !='':
            printboard(theboard)
            print('\n Game over \n')
            print('***'+turn+' won the game ***')
            break
          elif theboard['1']==theboard['4']==theboard['7'] !='':
            printboard(theboard)
            print('\n Game over \n')
            print('***'+turn+' won the game ***')
            break
          elif theboard['2']==theboard['5']==theboard['8'] !='':
            printboard(theboard)
            print('\n Game over \n')
            print('***'+turn+' won the game ***')
            break
          elif theboard['3']==theboard['6']==theboard['9'] !='':
            printboard(theboard)
            print('\n Game over \n')
            print('***'+turn+' won the game ***')
            break
      if count==9:
        print("\n Game over! \n")
        print("Its a tie")

      if turn=='x':
        turn="O"
      else:
        turn="x"
restart=input("Do you want to play again? (y/n):").lower()
if restart=="y":
  for key in board_keys:
      theboard[key]=' '
  game()
if __name__=="__main__":
  game()
 