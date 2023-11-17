from random import randint
def main():
    player_guess()

def player_guess():
    guess =  input("Enter a number 1-100.")
    while(not guess.isdigit()):
        guess = input("Enter a number")

    return(guess)

def play_game():
    randomnum = generate_random_number()
    numguesses = 3
    print("3 Guesses to get the number correct")
    x = 1
    x += 1
    while x < 4:
        print(x)
    guess = player_guess()
    give_feedback()
 
   

if __name__ == "__main__":
    main()
