'''2. Create a second function, checker(text,shift) that will call the caesar function on the text,
using the given shift, and then print out a sample of the text for the user to see. If the user recognizes
the sample as valid English words, the checker function should return True. Else, it should return False.

3. Create a third function, decode(), that interacts with the user and asks them to input a textfile.
The function should then cycle through all possible 26 shifts, calling your checker function on each shift
until the function returns True.

Optional bonus: Call your letters function (cut and paste your letters function into this same file!) on
the textfile to figure out which letters are most frequently used in the textfile. Your decode program will
then try to match these frequently used letters with the shift needed to take them back to an "e". It will
test, in order, the best possible matches by using the checker function.

4. Call the decode() function and input each of the following encoded texts, one at a time
(you'll want to right click on each and save them into the same location as your python file).
Figure out what the texts say and then figure out where each of them are from. Once you figure them out,
email me your entire python file along with your answers for where these four messages are from
(that part can be in the body of the email).'''

#Define Functions
def open_code(): #Function to open the file and create the name of a the new decoded textfile
    global coded_contents
    global new_text_file
    text_file = input("Input your coded textfile name:")
    with open(text_file,"r+") as f:
        coded_contents = f.read()#read contents into variable coded_contents
    new_text_file = text_file[:-4] + "_decoded" + text_file[-4:]

def decode(): #Main function that calls function checker() and breaks when user returns 'y'
    global user
    global coded_contents
    global decoded_text
    open_code()
    for i in range(27):
        checker(i)
        if user == 'y':
            break
    decoded_text = (caesar(coded_contents,i))
    return decoded_text

def checker(shift):#Function that calls caesar and prints what it returns and asks the user if they can read it
    global user
    global coded_contents
    decode_attempt = caesar(coded_contents[:25],shift) #Sample only the first 25 characters
    print(decode_attempt)
    user = input("Can you read this? Press 'y' for yes, any other key for no.")
    return user

def caesar(code,shift): #Function that cylces through 26 possible shifts and passes over non-lowercase-alphas
    text_list = list(code)
    result = ''
    for i in text_list:
        if ord(i) < 97 or ord(i) > 122: #Don't shift non-lowercase-alphas
            result += i
        elif ord(i) + shift > 122:
            new_shift = (ord(i) + shift - 123)
            result += chr(97 + new_shift)
        else:
            result += chr(ord(i) + shift)
    return result

#Main body
#Variables
new_text_file = ''
text_file = ''
coded_contents = ''
decoded_text = ''
text = ''
user = ''

decode()
print("Here is your decoded text:")
print (decoded_text)
with open(new_text_file,"w+") as f: #Create new file with the decoded text
    f.write(decoded_text)
