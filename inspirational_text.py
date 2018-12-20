'''Solomon Brenneman
   Project 3 (Inspirational Text)
   November 9, 2018

   This program asks the user for a textfile and then allows them to choose from 6 different options for
   interacting with the text. Option 1 asks for a word or phrase and then searches for the text for the first occurence.
   Option 2 asks for a word or phrase and finds it and then prints it in context. Option 3 searches for a word and replaces
   every instance of that word with a new one saved to a new string. Option 4 encodes the text in a new file. Option 5 finds the
   longest word in the file and option 6 sends the user an email containing either a random chunk of the text or uses option 2 to
   send the user a chunk of text containing a specific keyword.'''


#Imports
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import random

#Functions
#Get the textfile
def get_text():
    text_file = input("Input the name of your textfile (including '.txt'):")
    with open(text_file, 'r+') as f:
        text = f.read()
    return text,text_file

#Menu
def show_menu(text,text_file):#Shows the user the menu
    print("\nWhat would you like to do with the text?\n")
    print("1 Find the number of occurences of a word or phrase")
    print("2 Find a word or phrase in context")
    print("3 Search and replace")
    print("4 Encode the text in a new textfile")
    print("5 Find the longest word")
    print("6 Email a chunk of random text or text containing a keyword\n")
    user = input("Enter the number of the option you would like to choose, 'q' to quit.")
    if user == "1": #This next section checks the user input and runs the chosen function, returns q
        word_occurence(text)
    elif user == "2":
        word = input("Input the word or phrase you would like to find in context:")
        word_context(text,word)
    elif user == "3":
        search_replace(text)
    elif user == "4":
        encoded_text = encoder(text,text_file)
        print("Your text has been encoded in the file %s" % encoded_text)
    elif user == "5":
        longest_word(text)
    elif user == "6":
        user_email = input("Enter your email address:") #Asks for email address
        choice = input("Enter '1' to be sent a random chunk of text, type a word to be sent a chunk of text with that word in it.")
        if choice == "1": #This option is for random chunk
            random_place = random.randint(0,len(text)-100)
            text_chunk = text[random_place:random_place + 100]
            sendEmail("python.inspirational@gmail.com",user_email,text_file[:-3],text_chunk,"Project3")
        else:
            place = word_context(text,choice) #This option is for sending a chunk of text with a keyword
            text_chunk = (text[(place-100):place] + text[place:(place+100)])
            sendEmail("python.inspirational@gmail.com",user_email,text_file[:-3],text_chunk,"Project3")
        print("Check your email!")
    return user

#Find occurences of a word
def word_occurence(text):
    word = input("Input the word or phrase you would like to count:")
    occurences = text.lower().count(word.lower())
    print("\n'%s', occurs %i times in your text" % (word,occurences))
    return text

#Find a word in context
def word_context(text,word):
    if word in text:
        place = text.find(word)#If you have time go back and make this so that it cylces through all occurences
        print(text[(place-100):place] + text[place:(place+100)])
    else:
        print("\nSorry, that word cannot be found in the text.")
    return place

#Search and replace a word with a new word and saved to a new string
def search_replace(text):
    word = input("Input the word or phrase you would like to replace:")
    new_word = input("Input the new word you would like to replace the old word with:")
    new_text = text.replace(word,new_word) #If I have time to look at this make it so that it accounts for upper and lower case
    print("\n'%s' has been replaced with '%s'" % (word, new_word))
    return text

#Encodes the text (shift 10) and creates a new file
def encoder(text,text_file):
    text_list = list(text)
    result = ''
    for i in text_list:
        result += chr(ord(i) + 10)
    new_text_file = text_file[:-4]+"_encoded.txt"
    with open(new_text_file, "w+") as f:
        f.write(result)
    return new_text_file

#Searches for the longest word in the textfile
def longest_word(text):
    unwanted = [',','.','?','!',':',';','\'','-','"']
    for char in unwanted:
        text = text.replace(char,' ')
    text_list = text.split()
    long_word = max(text_list, key=len)
    num_char = len(long_word)
    print("\nThe longest word in your text is '%s' which is %i letters long." % (long_word,num_char))
    return text

#Sends the user an email
def sendEmail(sender, sendee, header, body, password):
    s = smtplib.SMTP('smtp.gmail.com:587')
    s.starttls()
    s.login(sender, password)
    msg = MIMEMultipart()
    msg['From']= sender
    msg['To']= sendee
    msg['Subject']= header
    msg.attach(MIMEText(body, 'plain'))
    s.send_message(msg)
    del msg
    s.quit()

#Master
user = ''
user2 = ''
text_file = ''

try:
    text,text_file = get_text() #Gets the textfile and assigns the text to a variable
    while user != "q": #Quits if the user enters q
        try:
            user = show_menu(text,text_file)
        except:
            print("Invalid input.")
except FileNotFoundError:
    print("The File does not exist.") #Breaks if the input is invalid or if the file does not exist
except:
    print('Invalid input')
print("Goodbye!")
