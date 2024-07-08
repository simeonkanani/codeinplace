import random

def main():
    print("Khansole Academy")
    # generate two random numbers btn 10 and 99
    Rand1 = random.randint(10,99)
    Rand2 = random.randint(10,99)
    
    print("What is " + str(Rand1) + " + " + str(Rand2) + "?")

    # ask the user to input answer 
    your_answer = int(input(''))
    print("Your answer: " + str(your_answer))
    # add Rand1 and Rand 2 
    answer = Rand1 + Rand2
    # check if answer entered is correct or incorrect
    if your_answer == answer:
        print("Correct!")
    else:
        print("Incorrect.")
    print("The expected answer is " + str(answer))
    # Return the correct answer

    
    
if __name__ == '__main__':
    main()