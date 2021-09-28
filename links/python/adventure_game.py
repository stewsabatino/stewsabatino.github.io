import words
import random
import time


def print_pause(message, seconds):
    print(message)
    time.sleep(seconds)


def intro(noun1, noun2, adjective, noun3, items):
    monster = random.choice(noun1)
    name_place_1 = random.choice(noun2)
    name_place_2 = random.choice(adjective) + " " + random.choice(noun3)
    print_pause("You find yourself standing in an open "
                "field, filled with grass and yellow "
                "wildflowers.", 2)
    print_pause("Rumor has it that a wicked " + monster + " is "
                "somewhere around here, and has been "
                "terrifying the nearby village.", 2)
    print_pause("In front of you is a " + name_place_1 + ".", 2)
    print_pause("To your right is a " + name_place_2 + ".", 2)
    print_pause("In your hand you hold your trusty (but not very "
                "effective) dagger", 2)
    in_field(name_place_1, name_place_2, monster, items)


def play_again():
    answer = input("Would you like to play again? (y/n)\n")
    if answer == 'y':
        print_pause("Excellent! Restarting the game...", 2)
        play_game()
    elif answer == 'n':
        print_pause("Thank you for playing! See you next time.", 2)
    else:
        print_pause("Please try again.", 2)
        play_again()


def run(name_place_1, name_place_2, monster, items):
    # run away from monster
    print_pause("you run back into the field. Luckily, you don't "
                "seem to have been followed.", 2)
    in_field(name_place_1, name_place_2, monster, items)


def wrong_answer():
    print_pause("Please try again.", 2)


def place_1_intro(name_place_1, name_place_2, monster, items):
    print_pause("You approach the door of the house.", 2)
    print_pause("You are about to knock when the door opens "
                "and out steps a wicked " + monster + ".", 2)
    print_pause("Eep! this is the wicked " + monster + "'s "
                + name_place_1 + "!", 2)
    print_pause("The wicked " + monster + " attacks you!", 2)


def place_1_sword_battle(name_place_1, name_place_2, monster, items):
    response = input("Would you like to (1) fight or (2) run "
                     "away?\n")
    if "1" in response:
        print_pause("As the wicked " + monster + " moves to attack"
                    ", you unsheath your new sword.", 2)
        print_pause("The sword of Ogorath shines brightly in your "
                    "hand as you brace yourself for the attack.", 2)
        print_pause("But the wicked " + monster + " takes one look"
                    " at your shiny new toy and runs away!", 2)
        print_pause("You have rid the town of the wicked " +
                    monster + ". You are vicotrious!", 2)
        play_again()
    elif "2" in response:
        run(name_place_1, name_place_2, monster, items)
    else:
        wrong_answer()
        place_1_sword_battle(name_place_1, name_place_2, monster, items)


def place_1_dagger_battle(name_place_1, name_place_2, monster, items):
    print_pause("You feel a bit under-prepared for this, what with "
                "only having a tiny dagger.", 2)
    response = input("Would you like to (1) fight or (2) run "
                     "away?\n")
    if "1" in response:
        print_pause("You do your best....", 2)
        print_pause("but your dagger is no match for the wicked "
                    + monster, 2)
        print_pause("You are eaten by the " + monster + "!", 2)
        play_again()
    elif "2" in response:
        run(name_place_1, name_place_2, monster, items)
    else:
        wrong_answer()
        place_1_dagger_battle(name_place_1, name_place_2, monster, items)


def place_1(name_place_1, name_place_2, monster, items):
    place_1_intro(name_place_1, name_place_2, monster, items)
    if "sword" in items:
        place_1_sword_battle(name_place_1, name_place_2, monster, items)
    else:
        place_1_dagger_battle(name_place_1, name_place_2, monster, items)


def place_2_again(name_place_1, name_place_2, monster, items):
    print_pause("You've been here before, and gotten all the "
                "good stuff. It's just an empty " + name_place_2 +
                " now.", 2)
    print_pause("You walk back out to the field", 2)
    in_field(name_place_1, name_place_2, monster, items)


def place_2_gain_sword(name_place_1, name_place_2, monster, items):
    print_pause("It turns out to be only a small " + name_place_2 + ".", 2)
    print_pause("Your eye catches a glint of metal behind a rock.", 2)
    print_pause("You have found the magical Sword of Ogoroth!", 2)
    print_pause("You discard your silly old dagger and take the "
                "sword with you.", 2)
    print_pause("You walk back out to the field.", 2)
    items.append("sword")
    in_field(name_place_1, name_place_2, monster, items)


def place_2(name_place_1, name_place_2, monster, items):
    print_pause("You peer cautiously into the " + name_place_2 + ".", 2)
    if "sword" in items:
        place_2_again(name_place_1, name_place_2, monster, items)
    else:
        place_2_gain_sword(name_place_1, name_place_2, monster, items)


def in_field(name_place_1, name_place_2, monster, items):
    print_pause("Enter 1 to knock on the door of the " + name_place_1 +
                ".\nEnter 2 to peer into the " + name_place_2 + ".", 2)
    print_pause("What would you like to do?", 2)
    response = input("(Please enter 1 or 2.)\n")
    if response == '1':
        place_1(name_place_1, name_place_2, monster, items)
    elif response == '2':
        place_2(name_place_1, name_place_2, monster, items)
    else:
        print_pause("Please choose one of the following:", 2)
        in_field(name_place_1, name_place_2, monster, items)


def play_game():
    items = []
    intro(words.noun1, words.noun2, words.adjective, words.noun3, items)


play_game()
