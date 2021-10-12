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
    print("\n DO YOU WANT TO SAVE GRANNY? (yes or no)")
    # convert the player's input to lower_case
    answer = input(">").lower()
    if answer == "yes":
        # take player to cross_roads
        cross_roads()
    elif answer == "no":
        # exit() the program
        exit("\n Sorry to see you go.")
    else:
        # return to start()
        start()