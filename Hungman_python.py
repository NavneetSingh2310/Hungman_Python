#import time module
import time

#welcoming user
name = input("What is Your Name?")

print("Hello, "+ name + ", time to play hungman!")

#wait for 1 second
time.sleep(1)

print("start guessing...")
time.sleep(0.5)

#here we set the secret 
word = "secret"

#create an variable with an empty value

guesses=''

#determine the number of turns

turns=10

#create a while loop

#check if the turns are more than zero

while turns>0:
    
    #make a counter that starts with zero
    failed=0
    
    #for every character in secret_word
    for char in word:
        #see if the character is in the players guesses
        if char in guesses:
            #print out the character
            print(char)
        else:
            #if not found, print a dash
            print("_")
            #increment the failed counter by one 
            failed+=1
    #if failed is equals to zero 
    #print you won 
    if failed == 0:
        print("You Won")
        #exit the script
        break;
    
    #ask a user to go guess a character
    
    guess = input("guess a character:")
    
    #set the players guess to guesses
    guesses+=guess
    
    if guess not in word :
        #turn counter decrease by 1
        turn-=1
        print("Wrong")
        # how many turns left
        print("You have"+ turns + "more guesses")
        
        if turns==0:
            print("You Lose")
            
        
        
        
        
        