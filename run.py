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
    # if player typed "left" or "l" lead him to bear_den()
    if answer == "l":
        bear_den()
    # else if player typed "right" or "r" lead him to monster_den()
    elif answer == "r":
        monster_den()
    # else return to start()
    else:
        print("\n Incorrect Answer")
        print("\n To continue playing press 1 or press 2 to quit the game")
        # convert the player's input() to lower_case
        answer = input(">").lower()
        if answer == "1":
            cross_roads()
        elif answer == "2":
            print("\n Sorry to see you go!")
            print("\n Granny hopes you will return to rescue her")
            exit()
        else:
            exit()


def bear_den():
    # give some prompts.
    print("\nYou have entered the bear's den")
    time.sleep(a)
    print("\nYou see two doors.")
    time.sleep(a)
    print("Door 1 is guarded by a pot of honey")
    time.sleep(a)
    print("Door 2 is guarded by the sleeping bear")
    time.sleep(a)
    print("Which door will you choose to take (1 or 2)")
    print("1). Door guarded by the honey jar.")
    print("2). Door guarded by the sleeping bear")
    # convert the player's input() to lower_case
    answer = input(">").lower()
    # if player typed "1" game over()
    if answer == "1":
        game_over()
    # else if player typed "2" lead him to dungeon_den()
    elif answer == "2":
        dungeon_den()
    # else return to start()
    else:
        print("\n Incorrect Answer")
        print("\n To continue playing press 1 or press 2 to quit the game")
        # convert the player's input() to lower_case
        answer = input(">").lower()
        if answer == "1":
            bear_den()
        elif answer == "2":
            print("\n Sorry to see you go!")
            print("\n Granny hopes you will return to rescue her")
            exit()
        else:
            exit()


def monster_den():
    # give some prompts.
    print("\nYou have entered the monster den")
    time.sleep(a)
    print("\n The monster is eating lunch...")
    time.sleep(a)
    print("\n you just have a few seconds to get through..")
    time.sleep(a)
    print("\nYou see two windows.")
    time.sleep(a)
    print("window 1 is open but very small")
    time.sleep(a)
    print("Door 2 is closed but big enough for you to fit through")
    time.sleep(a)
    print("Which door will you choose to take (1 or 2)")
    print("1. Squeeze through the small window")
    print("2. Open the bigger window and comfortably slide through")
    # convert the player's input() to lower_case
    answer = input(">").lower()
    # if player typed "1" dungeon_den()
    if answer == "1":
        dungeon_den()
    # else if player typed "2" lead him to game_over()
    elif answer == "2":
        game_over()
    # else return to start()
    else:
        print("\n Incorrect Answer")
        print("\n To continue playing press 1 or press 2 to quit the game")
        # convert the player's input() to lower_case
        answer = input(">").lower()
        if answer == "1":
            bear_den()
        elif answer == "2":
            print("\n Sorry to see you go!")
            print("\n Granny hopes you will return to rescue her")
            exit()
        else:
            exit()


def dungeon_den():
    # give some prompts.
    print("\nWell done! You escaped the sleeping bear.")
    time.sleep(a)
    print("\nYou have entered the witch's dungeon den.")
    time.sleep(a)
    print("\nAgain you see two doors")
    time.sleep(a)
    print("Door 1 will lead you through a room with a sleeping snake")
    time.sleep(a)
    print("Door 2 will lead you through a room with a starving tiger")
    time.sleep(a)
    print("Which door will you choose to take (1 or 2)")
    print("1). Door leading to room with a sleeping snake.")
    print("2). Door leading to room with starving tiger")
    # convert the player's input() to lower_case
    answer = input(">").lower()
    # if player typed "1" game over()
    if answer == "1":
        game_over()
    # else if player typed "2" game_win()
    elif answer == "2":
        game_win()
    # else return to start()
    else:
        start()
    

# start the game
start()
