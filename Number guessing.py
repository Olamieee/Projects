import random, sys
num = []
guess = None
for num in range(5):
    print('****Welcome to number guessing game****')
    guess = int(input('Please enter a number: '))
    num= random.randint(0,20)
    print(num)
    if guess == num:
        print(guess)
        print('correct')
        print('***WELLDONE!***')
    else:
        print('try again')
print(sys.getsizeof(guess))
sys.exit
# import pywhatkit as pwk
 
# # using Exception Handling to avoid unexpected errors
# try:
#      # sending message in Whatsapp in India so using Indian dial code (+91)
#      pwk.sendwhatmsg("+2348104388704", 'urghh \n pelee ti e', 23, 48) * 4
#      print("Message Sent!") #Prints success message in console
 
#      # error message
# except: 
#      print("Error in sending the message")
