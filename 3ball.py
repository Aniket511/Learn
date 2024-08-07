from random import shuffle

my_list = ["O"," "," "]

def shuffle_list():
    shuffle(my_list)
    return my_list

new_list = shuffle_list()

def take_guess():
    guess=""
    while True:
        guess = int(input("Enter your guess between 1 to 3:"))
        
    return guess

guess=take_guess()

def check_guess(new_list,guess):
    for i in new_list:
        if new_list[guess] == "O":
            print("Congratulations")
        else:
            print("Sorry")
            print(new_list)