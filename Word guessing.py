import random
correct_words = ['A', 'B', 'C', "D", 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X, Y', 'Z'] 
#these are suggested words to be guessed stored in a list 
guess = None 
word = None
for i in range(10):
    guess = input('Make a guess: ')   #try by guessing a word from the given list.
    word = random.choices(correct_words)  #word variable take a word from the lists and assume it as the correct word.
    if guess == word: 
        print(word) 
        print('**************\n'
              '***Well done!**\n'
              '****************')
    else:
         print('**************\n'
              '***Try again.**\n'
              '****************')

# print(random.choices(words))

    