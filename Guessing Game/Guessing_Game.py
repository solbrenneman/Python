#Guessing Game - Solomon Brenneman

#Define functions

def high_score(entry): #Create highscore file and write highscores
    with open("guessing_game_scores.txt", "a+") as f:
        f.seek(29)
        score_list = f.readlines()
        score_list.append(entry + "\n")
        score_list.sort(reverse=True)
        #print(score_list)

    with open("guessing_game_scores.txt","w+") as f:
        f.write("Guessing Game Highscore List\n")
        f.writelines(score_list)
        #print(score_list)

def guess_calc(guess): #Calculate whether or not the user's guess is correct
    global answer
    if guess == my_num:
        answer = True
    elif guess < my_num:
        answer = False
        print("\nHigher than %i." % (guess))
    elif guess > my_num:
        answer = False
        print("\nLower than %i." % (guess))

def random_num():  #Get a random number
    import random
    my_num = random.randint(1,100)
    #print(my_num)
    return my_num

def guessing_game(number): #Give the user 3 attempts to guess the number and then ask if they would like to play again
            global guess
            global user
            guess_calc(int(input("Enter your guess:"))) #Take the users guess
            if answer == True:
                print("Correct! You got: 500 points.") #Tell them how many points they got
                user = input("Type any key and press enter to play again, 'q' to quit:") #Allow them to quit or play again
                return 500 #Return score

            guess_calc(int(input("Enter your guess:")))
            if answer == True:
                print("Correct! You got: 250 points.")
                user = input("Type any key and press enter to play again, 'q' to quit:")
                return 250

            guess_calc(int(input("Last chance!\nEnter your guess:")))
            if answer == True:
                print("Correct! You got: 100 points.")
                user = input("Type any key and press enter to play again, 'q' to quit:")
                return 100
            elif answer == False: # If they get it wrong on the last try they get 0 points
                print("Good try! The number was %i." %(my_num))
                user = input("\nType any key and press enter to play again, 'q' to quit:")
                return 0

#Master
#Variables needed
guess = 0
user = ""
scores = []
initials = input("\nInput your initials:") #Get the users initials

while user != "q": #Allow them to quit if they do not want to play again
    try:
        my_num = random_num() #Get a random number
        print("\nI've got my number!")
        score = guessing_game(my_num) #Allow the user 3 guess and give them points if they get it right
        scores.append(score) #Keep a list of their scores
        highscore = max(scores) #Collect the highscore out of their list of scores
        entry = (str(highscore) + " " + initials) #Create an entry for the highscore list
    except:
        print("Error. Try again with a new number.")

if highscore > 0: #If they guessed at least one number correctly they are put on the highscore list
    high_score(entry)
    print("%s, your highscore of: %i, has been posted to the highscore list!\n" % (initials,highscore))
    exit()
else: #If they don't get any points on any try they do not make it to the highscore list
    print("\nSorry %s, you didn't make it to the Highscore list. Better luck next time!\n" % (initials))
    exit()
