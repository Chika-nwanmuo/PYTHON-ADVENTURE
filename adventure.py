import time
import random


def delayed_print(txt):
    print(txt)
    time.sleep(2)


def game_intro(attacker):
    delayed_print("You find yourself standing in an open field,"
                  " filled with grass and yellow wildflowers.")
    delayed_print(f"Rumor has it that a {attacker} is somewhere around"
                  " here, and has been terrifying the nearby village.")
    delayed_print("In front of you is a house.")
    delayed_print("To your right is a dark cave.")
    delayed_print("In your hand you hold your trusty "
                  "(but not very effective) dagger.")


def decide_door_cave(attacker, weapons):
    delayed_print("\nEnter 1 to knock on the door of the house.")
    delayed_print("Enter 2 to peer into the cave.")
    delayed_print("What would you like to do?")
    delayed_print("(Please enter 1 or 2.) ")
    choice_made(attacker, weapons)


def choice_made(attacker, weapons):
    door_or_cave = input()
    if door_or_cave == "1":
        door(attacker, weapons)
    elif door_or_cave == "2":
        cave(attacker, weapons)
    else:
        delayed_print("(Please enter 1 or 2.) ")
        choice_made(attacker, weapons)


def door(attacker, weapons):
    if "Ogoroth sword" in weapons:
        delayed_print("You approach the door of the house.")
        delayed_print(f"You are about to knock when the door"
                      f" opens and out steps a {attacker}.")
        delayed_print(f"Eep! This is the {attacker}’s house!")
        delayed_print(f"The {attacker} attacks you!")
        decision_fight_or_run(attacker, weapons)
    else:
        delayed_print("You approach the door of the house.")
        delayed_print(f"You are about to knock when the door"
                      f" opens and out steps a {attacker}.")
        delayed_print(f"Eep! This is the {attacker}’s house!")
        delayed_print(f"The {attacker} attacks you!")
        delayed_print("You feel a bit under-prepared for this,"
                      " what with only having a tiny dagger.")
        decision_fight_or_run(attacker, weapons)


def decision_fight_or_run(attacker, weapon):
    fight_or_run = input("Would you like to (1) fight or (2) run away?")
    if fight_or_run == '1':
        fight(attacker, weapon)
    elif fight_or_run == '2':
        run(attacker, weapon)
    else:
        delayed_print("Invalid input. Try again")
        decision_fight_or_run(attacker, weapon)


def play_again():
    decide = input("Would you like to play again? (y/n)")
    if decide == 'y':
        delayed_print("Excellent! Restarting the game ...")
        play_game()
    elif decide == 'n':
        delayed_print("Thanks for playing! see you next time.")
    else:
        play_again()


def fight(attacker, weapons):
    if "Ogoroth sword" in weapons:
        delayed_print("As the troll moves to attack, you "
                      "unsheathe you new sword.")
        delayed_print("The sword of Ogoroth shines "
                      "brightly in your hand as you "
                      "brace yourself for the attack.")
        delayed_print(f"But the {attacker} takes one look "
                      "at your shiny new toy and runs away!")
        delayed_print("You have rid the town of the "
                      "troll. You are victorious!")
        play_again()
    else:
        delayed_print("You do your best...")
        delayed_print(f"But your dagger is no match for the wicked {attacker}")
        delayed_print("You have been defeated!")
        play_again()


def run(attacker, weapons):
    delayed_print("You run back into the field. "
                  "Luckily, you don’t seem to have been followed.")
    decide_door_cave(attacker, weapons)


def cave(attacker, weapons):
    # Here is where you find the sword of Ogoroth
    if "Ogoroth sword" in weapons:
        delayed_print("You peer cautiously into the cave.")
        delayed_print("You’ve been here before, and gotten"
                      " all the good stuff. It’s just an empty cave now.")
        delayed_print("You walk back out to the field.")
        decide_door_cave(attacker, weapons)

    else:
        weapons.append("Ogoroth sword")
        delayed_print("You peer cautiously into the cave.")
        delayed_print("It turns out to be only a very small cave.")
        delayed_print("Your eyes catches a glint of metal behind a rock.")
        delayed_print("You have found the magical Sword of Ogoroth!")
        delayed_print("You discard your silly old dagger and"
                      " take the sword with you.")
        delayed_print("You walk back out to the field.")
        decide_door_cave(attacker, weapons)


def play_game():
    list = ["pirate", "troll", "wicked fairie", "dragon", "gorgon"]
    evil_agent = random.choice(list)
    ogoroth = []
    game_intro(evil_agent)
    decide_door_cave(evil_agent, ogoroth)


if __name__ == "__main__":
    play_game()
