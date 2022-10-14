import random
words = ['game','lion','tiger','coder','techie','google','football','friends','university','hunter']
word = random.choice(words)
maskedword =[]
length = len(word)
while length>0:
    maskedword.append('*')
    length-=1
mask = len(word)*'*'   
wrongguess = len(word)
print("Word is ", mask , "its length is ", len(word))
turns = 0
index = 0
previous =''
correct =''
while(turns<wrongguess):
    print("\nyou have ", (wrongguess - turns), "attempts left")
    print("Enter a character(lowercase) : ", end='')
    guess=input()
    if(guess not in word):
        if(guess not in previous):
            turns+=1
        previous+=guess
        print("Previous guess : ", previous)
        if(turns<wrongguess):
             print("Try again...")
             print("word is ", end='')
             for i in maskedword:
                 print (i, end='')
    else:
        if(guess not in correct):
            
            print("correct..")
            index = 0
            for i in word:
                if(word[index]==guess):
                    maskedword[index]=guess
                index=index+1;
            if(turns<wrongguess):
                print("word is ", end='')
                for i in maskedword:
                    print (i, end='')
            correct+=guess
        else:
            print("you have already guessed this character")
            print("Try again...")
            print("word is ", end='')
            for i in maskedword:
                print (i, end='')
            
    if('*' not in maskedword):
        print("\nCongratulations you got the word")
        break;
if(turns==wrongguess):
    print("word is ", word)
    print("you lost")
                
        
        
