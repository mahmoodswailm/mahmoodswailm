from random import choice
words = """fruit apple orange pinapple
"""
words = words.split(" ")
word = choice(words)

print(word)

guesses = ""

tries = 12




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

# hi2()