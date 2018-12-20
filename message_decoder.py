#Functions

#Code Shifter
def caesar(code,shift): #Function that cylces through 26 possible shifts and passes over non-lowercase-alphas
    text_list = list(code)
    result = ''
    for i in text_list:
        if ord(i) < 65 or ord(i) > 90: #Don't shift non-lowercase-alphas
            result += i
        elif ord(i) + shift > 90:
            new_shift = (ord(i) + shift - 91)
            result += chr(65 + new_shift)
        else:
            result += chr(ord(i) + shift)
    return result

#Letter goodness score adder for shift
def add_score(result,letterGoodness):
    total_score = 0
    for i in result:
        if i.isalpha():
            letter_score = float(letterGoodness[ord(i)-65])
            total_score += letter_score
    return total_score

def create_dyct(message,letterGoodness):
    score_shift = {}
    for i in range(1,27):
        result = caesar(message,i)
        total_score = add_score(result,letterGoodness)
        score_shift[i] = total_score
    return score_shift

#Master
letterGoodness = [0.0817, 0.0149, 0.0278, 0.0425, 0.127, 0.0223, 0.0202, 0.0609, 0.0697, 0.0015, 0.0077, 0.0402, 0.0241, 0.0675, 0.0751, 0.0193, 0.0009, 0.0599, 0.0633, 0.0906, 0.0276, 0.0098, 0.0236, 0.0015, 0.0197, 0.0007]
message = input()
score_dyct = create_dyct(message,letterGoodness)
best_shift = max(score_dyct, key=score_dyct.get)
decrypted = caesar(message,best_shift)
print(decrypted)
