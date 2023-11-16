import random

def main():
    game()

def game():
    rannum= random.randint(1,100)

    print('''        Guess a number between 1-100.
            You have 3 attempts.
            Good Luck!''')


    x=1
    while x<4:
        x+=1
        playerguess = input("Type your guess here: ")
    
        if not playerguess.isdigit():
            print("Type a number")
            return(game())
        

        playerguess = int(playerguess)


        if playerguess == rannum:
            print("correct")
                
            
        elif playerguess <1 and playerguess!= rannum:
            print("Please type a number greater than 1")
            print("Take another guess")
            
            continue

        elif playerguess > 100 and playerguess!= rannum:
            print("Please type a number less than 100")
            print("Take another guess")
            
            continue

        elif playerguess > rannum:
            print("Too high")

        elif playerguess < rannum:
            print("Too low")
        
    print("This was the correct number:",rannum)
    print("This took you", x-1 ,"attempts")

    restart = input("would you like to try again? 1 for yes, 2 for no: ")
    if restart == "1":
        return(game())
    elif restart =="2":
        quit()



if __name__ == "__main__":
        main()




        



