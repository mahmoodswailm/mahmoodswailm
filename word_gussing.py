# c = lambda a : lambda b : a*b

# print(c(5)("5"))
from random import choice
"""
a project of guessing the a random word

"""


# name = input("what's your name")

print("good look mahmood")



words = """fruit apple orange pinapple
"""
words = words.split(" ")
word = choice(words)

print(word)

guesses = ""

tries = 12



def hi():
        
    while tries > 0 :
        failed = 0


        for char in word:
            
            if char in guesses:
                print(char,end=" ")
            
            else:
                print("_",end=" ")
                failed +=1

        if failed == 0:
            print("you won ")
            break


        
        guesse = input("input your guess")


        if guesse in word:
            guesses += guesse

        else :
            tries-=1
            print(tries," tries left")
                
            if tries == 0 :
                print("nice try the word is {}".format(word))





# someWords = '''apple banana mango strawberry  
# orange grape pineapple apricot lemon coconut watermelon 
# cherry papaya berry peach lychee muskmelon'''

# someWords = someWords.split(' ') 
# print(words)
# print(someWords)
def hi2():
    global tries,guesses
    word = choice(words)

    while tries > 0 :
        failed = 0


        for char in word:
            
            if char in guesses:
                print(char,end=" ")
            
            else:
                print("_",end=" ")
                failed +=1

        if failed == 0:
            print("you won ")
            break


        while True:
            guesse = input("input your guess")
            if not guesse.isalpha():
                print("please input  only letter ")
            elif len(guesse) > 1:
                print("please input only one letter")
            else:
                break
        
        if guesse in word:
            guesses += guesse

        else :
            tries-=1
            print(tries," tries left")
                
            if tries == 0 :
                print("nice try the word is {}".format(word))

hi2()