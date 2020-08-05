import random 

print("Rules: You have to continue the word chain, Your word must start with the last word last character like - MAN your word must start with N like NUMBER, you have 3 heart in every round" )

class SmallNumber(Exception):
    pass

while True:
    try:
        gamers_number = int(input("How many players do we have? "))
        if gamers_number < 2:
            raise SmallNumber
        else:
            break
    except SmallNumber:
        print("2 or more player can only play")
    except ValueError:
        print("Oops not a number")

gamers_name = [input() for i in range(0, gamers_number)]


def welcome(gamers_name): #  greeting to the competitors
    for i in range(len(gamers_name)):
        print(i + 1, ". competitor is:", gamers_name[i])

def shuffle_competitors(gamers_name):
    random.shuffle(gamers_name) #  shuffle the names 

welcome(gamers_name)
shuffle_competitors(gamers_name)


random_first_word = ["man","goalkeeper","evaluate", "criticism","immune", "reliable", "abandon", "grand", "quaint"]
used_words = []
used_words.append(random_first_word [random.randint(0, len(random_first_word))].upper())
print("The first word is: ",used_words[0]) #  The first word


run = True
index = 0
count_bad_try = 0
while run:
    print("Write 'exit' for exit or write 'end' for give up or write your word.")
    is_good = True
    out_of_game = False
    print(gamers_name[index], " word is:")
    word = str(input())

    if word.upper() == "EXIT":
        print("Thanks for gaming")
        break 
    
    if word.upper() == "END" or count_bad_try == 2:
        print(gamers_name[index], " is out of game")
        gamers_name.pop(index)
        out_of_game = True
        if len(gamers_name) == 1:
            print("\nThe winner is:", gamers_name[0])
            break

    if word[0].upper() != used_words[-1][len(used_words[-1]) - 1] and not out_of_game:
        print("\nOopes the first letter doesn't match to the last word last character, try again left lives", 2 - count_bad_try)
        is_good = False
        count_bad_try += 1
        continue 

    if used_words.__contains__(word.upper()) and is_good and not out_of_game:
        print("\nOops someone earlier said this word, try again, left lives", 2 - count_bad_try)
        is_good = False
        count_bad_try += 1
        continue 

    if is_good:
        print("\nGood Word, Nice!")
        used_words.append(word.upper())
        index += 1
        if index >= len(gamers_name):
            index = 0
        
    
print("Used words: ",used_words)
    


