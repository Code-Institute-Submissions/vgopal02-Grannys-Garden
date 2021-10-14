import time

a = 2


def start():
    # Storyline prompts
    print("WELCOME TO GRANNY'S GARDEN\n")
    print("\n Granny was in the garden picking apples....")
    time.sleep(a)
    print("\n when the wicked witch from across the mountain kidnapped her!")
    time.sleep(a)
    print("\n Granny needs to be rescued...")
    time.sleep(a)
    print("\n DO YOU WANT TO SAVE GRANNY? (y or n)")
    # convert the player's input to lower_case
    answer = input(">").lower()
    if answer == "y":
        # take player to cross_roads
        cross_roads()
    elif answer == "n":
        # exit() the program
        exit("\n Sorry to see you go.")
    else:
        # return to start()
        start()


def cross_roads():
    # give some prompts.
    print("\nThank you for coming to Granny's rescue.")
    time.sleep(a)
    print("\nYou are at a crossroad with 2 doors.")
    time.sleep(a)
    print("\n Will you take the left or right door? (l or r)")
    # convert the player's input() to lower_case
    answer = input(">").lower()
    # if player typed "left" or "l" lead him to bear_room()
    if answer == "l":
        bear_den()
    # else if player typed "right" or "r" lead him to monster_room()
    elif answer == "r":
        monster_den()
    # else return to start()
    else:
        start()