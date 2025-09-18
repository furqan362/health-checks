import random
name=input("Enter your name: ")
print("Good luck !",name)
words=["book", "phone", "computer", "chair", "table", "bed", "car", "bike", "train", "bus"]
word=random.choice(words)
print("Guess the characters")
guesses=""
turns=12
while turns>0:
    failed=0
    for char in word:
        if char in guesses:
            print(char,end="")
        else:
            print("_")
            failed+=1
    if failed==0:
        print("You win! ")
        print("The character is ",word)
        break
    guess=input("Guess a character: ").lower()
    guesses+=guess
    if guess not in word:
        turns-=1
        print("Wrong")
        print("you have ",turns," more guesses")    
    if turns==0:
        print("You loose")
