import random
import time


def print_pause(input_text):
    # Function to print a message with a pause of 2 seconds
    print(input_text)
    time.sleep(2)


def play_game():
    # Main function that drives the game
    total_score = 0
    game_over = False

    player_name = input("Enter your name: ")  # Ask for the player's name
    print_pause(f"Welcome, {player_name}! You find yourself in front of the greatest school of magic ever, Hogwarts.")
    print_pause("Where the magic greats were born.")
    print_pause("You have just two houses to choose from, and each house has a mission to complete.")
    print_pause("What would you choose?")

    while True:
        choice = input("Enter 1 to enter Gryffindor house. Enter 2 to enter Slytherin house: ")
        if choice == "1":
            # Gryffindor house chosen, call spell_Gryffindor function
            enemy = random.choice(["dragon", "hippogriff", "basilisk"])
            print_pause(f"Your mission is to get the treasure. You saw a {enemy} protecting the treasure.")
            spell_Gryffindor(total_score, enemy, player_name)  # Pass player_name to the function
            break
        elif choice == "2":
            # Slytherin house chosen, call slytherin_check function
            enemy = random.choice(["snake", "giant spider", "dementor"])
            print_pause(f"Your mission is to protect a child from a {enemy}. The {enemy} was about to attack the child.")
            slytherin_check(total_score, enemy, player_name)  # Pass player_name to the function
            break
        else:
            print_pause("Please enter 1 or 2.")

    play_again()


def spell_Gryffindor(total_score, enemy, player_name):
    # Function to handle choices and consequences for Gryffindor house
    magic_wands = ["Elder Wand", "Phoenix Feather Wand", "Dragon Heartstring Wand"]
    wand = random.choice(magic_wands)
    print_pause(f"You have the {wand}, {player_name}.")  # Include player_name in the message
    while True:
        choice = input("Enter 1 to say the Expelliarmus spell. Enter 2 to say the Wingardium Leviosa spell: ")
        if choice == "1":
            # Expelliarmus spell chosen, handle consequences
            print_pause(f"The {enemy} is not affected by the spell.")
            total_score -= 5
            print_pause("You lost 5 points for not affecting the enemy!")
            print("Your current score is:", total_score)
            expelliarmus_choice(total_score, enemy, player_name)  # Pass player_name to the function
            break
        elif choice == "2":
            # Wingardium Leviosa spell chosen, handle consequences
            print_pause(f"The {enemy} will be affected and sleep for 5 seconds.")
            total_score += 10
            print_pause("You gained 10 points for affecting the enemy!")
            print("Your current score is:", total_score)
            wingardium_leviosa_choice(total_score, enemy, wand, player_name)  # Pass player_name to the function
            break
        else:
            print_pause("Please enter 1 or 2.")


def slytherin_check(total_score, enemy, player_name):
    # Function to handle choices and consequences for Slytherin house
    magic_wands = ["Elder Wand", "Phoenix Feather Wand", "Dragon Heartstring Wand"]
    wand = random.choice(magic_wands)
    print_pause(f"You have the {wand}, {player_name}.")  # Include player_name in the message
    while True:
        choice = input("Enter 1 to say the Avada Kedavra spell. Enter 2 to say the Muffliato spell: ")
        if choice == "1":
            # Avada Kedavra spell chosen, handle consequences
            print_pause(f"The {enemy} will die, the child will escape, and you will be judged by the Magic Court.")
            avada_kedavra_choice(total_score, enemy, wand, player_name)  # Pass player_name to the function
            break
        elif choice == "2":
            # Muffliato spell chosen, handle consequences
            print_pause(f"The {enemy} will be affected and confused as it cannot hear anything and cannot move correctly. You will save the child.")
            muffliato_choice(total_score, player_name)  # Pass player_name to the function
            break
        else:
            print_pause("Please enter 1 or 2.")


def expelliarmus_choice(total_score, enemy, player_name):
    # Function to handle choices and consequences for choosing Expelliarmus spell in Gryffindor house
    while True:
        choice = input("Enter 1 to run away. Enter 2 to say the conjunctivitis curse spell: ")
        if choice == "1":
            # Player chooses to run away, handle consequences
            print_pause(f"The {enemy} catches you.")
            total_score -= 5
            print_pause("You lost 5 points for running away!")
            print("Your current score is:", total_score)
            print_pause("Sorry, you lost!")
            break
        elif choice == "2":
            # Player chooses the conjunctivitis curse spell, handle consequences
            print_pause(f"The eyes of the {enemy} will be affected and you can defeat it.")
            total_score += 20
            print_pause("You gained 20 points for successfully defeating the enemy and getting the treasure!")
            print("Your current score is:", total_score)
            print_pause("Congratulations, you won!")
            break
        else:
            print_pause("Please enter 1 or 2.")


def wingardium_leviosa_choice(total_score, enemy, wand, player_name):
    # Function to handle choices and consequences for choosing Wingardium Leviosa spell in Gryffindor house
    while True:
        choice = input("Enter 1 to get the treasure and hide behind the chair. Enter 2 to escape while the enemy is sleeping and not get the treasure: ")
        if choice == "1":
            # Player chooses to get the treasure and hide, handle consequences
            print_pause(f"The {enemy} will look for you in another place, and you escape with the treasure successfully.")
            total_score += 10
            print_pause("You gained 10 points for getting the treasure!")
            print("Your current score is:", total_score)
            print_pause("Congratulations, you won!")
            break
        elif choice == "2":
            # Player chooses to escape without getting the treasure, handle consequences
            print_pause("You will be punished because you did not get the treasure.")
            total_score -= 10
            print_pause("You lost 10 points for not getting the treasure!")
            print("Your current score is:", total_score)
            print_pause("Sorry, you lost!")
            break
        else:
            print_pause("Please enter 1 or 2.")


def avada_kedavra_choice(total_score, enemy, wand, player_name):
    # Function to handle choices and consequences for choosing Avada Kedavra spell in Slytherin house
    while True:
        choice = input("Enter 1 to obey the ruling and go to Azkaban prison. Enter 2 to Escape and join The dark side: ")
        if choice == "1":
            # Player chooses to obey the ruling, handle consequences
            print_pause("After two years, you will come back to Hogwarts and finish your learning.")
            total_score += 10
            print_pause("You gained 10 points for obeying the ruling!")
            print("Your current score is:", total_score)
            print_pause("Congratulations, you won!")
            break
        elif choice == "2":
            # Player chooses to escape and join the dark side, handle consequences
            print_pause("You will be forbidden from using magic forever.")
            total_score -= 10
            print_pause("You lost 10 points because you did not obey the ruling!")
            print("Your current score is:", total_score)
            print_pause("Sorry, you lost!")
            break
        else:
            print_pause("Please enter 1 or 2.")


def muffliato_choice(total_score, player_name):
    # Function to handle consequences for choosing Muffliato spell in Slytherin house
    total_score += 20
    print_pause("You gained 20 points for saving the child!")
    print("Your current score is:", total_score)
    print_pause("Congratulations, you won!")


def play_again():
    # Function to ask the player if they want to play again
    while True:
        choice = input("Would you like to play again? (y/n): ")
        if choice.lower() == "y":
            play_game()
            break
        elif choice.lower() == "n":
            print_pause("Game Over. Thank you for playing!")
            break
        else:
            print_pause("Please enter 'y' or 'n'.")


play_game()
