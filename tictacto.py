theBoard = {'top-L': ' ', 'top-M': ' ','top-R': ' ',
				'mid-L': ' ','mid-M': ' ','mid-R': ' ',
				'low-L': ' ','low-M': ' ','low-R': ' '
			}
			
def printBoard(board):
	print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
	print('-+-+-')
	print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
	print('-+-+-')
	print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])
	

def switchTurn(aTurn):
	if aTurn == 'x':
		return 'o'
	return 'x'

turn = 'x'

for i in range(9):
	print('Turn for ' + turn)
	move = input()
	if move == "exit":
		break
	theBoard[move] = turn
	printBoard(theBoard)
	turn = switchTurn(turn)




def highlight_word(sentence, word):
  formated_sentence = ""
  words = sentence.split()
  upper_word = word.upper()
  for idx,single_word in enumarate(words):
    if single_word.upper() == upper_word:
      single_word = single_word.upper()
      if idx == 0:
        formated_sentence = single_word
      else:
        formated_sentence = formated_sentence + " " + single_word
      
  
	return(formated_sentence)	
