from random import randint
def main():
    give_feedback()

def give_feedback():
    number = randint(1,5)
    guess = input("Pick a number between 1-5:")
        
    guess = int(guess)
    

    if guess > number:
        print("too high ")
    elif guess < number:
        print("too low ")
    elif guess == number:
        print("correct ")


if __name__ == "__main__":
    main()

