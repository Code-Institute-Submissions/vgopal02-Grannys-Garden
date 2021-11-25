import time

a = 2


def start():
    # Storyline prompts
    print("\n WELCOME TO GRANNY'S GARDEN\n")
    print("\n Granny was in the garden picking apples....")
    time.sleep(a)
    print("\n when the wicked witch from across the mountain kidnapped her!")
    time.sleep(a)
    print("\n Granny needs to be rescued...")
    time.sleep(a)
    start_main()


def start_main():
    # Main function allowing user to proceed
    print("\n DO YOU WANT TO SAVE GRANNY? (y or n) ")
    # convert the player's input to lower_case
    answer = input(">").lower().strip()
    if answer == "y":
        # if input "y" take player to cross_roads
        cross_roads()
    elif answer == "n":
        # if input "n" take player to play_again()
        print("\n ------------------------------------------ ")
        print("\n ***** SORRY TO SEE YOU GO ***** ")
        print("\n ***** GRANNY HOPES YOU WILL BE BACK SOON *****")
        print("\n ***** GOODBYE *****")
        print("\n ------------------------------------------ ")
        play_again()
    elif answer == "":
        # if input blank back to start_main() indicatiing invalid entry
        print("\n ------------------------------------------ ")
        print("\n ***** INVALID ENTRY *****")
        print("\n ***** PLEASE ENTER A VALID ANSWER *****")
        print("\n ------------------------------------------ ")
        start_main()
    else:
        # if input wrong back to start_main() indicating incorrect entry
        print("\n ------------------------------------------ ")
        print("\n ***** INCORRECT ANSWER ***** ")
        print("\n ***** PLEASE ENTER A CORRECT ANSWER ***** ")
        print("\n ------------------------------------------ ")
        start_main()


def cross_roads():
    # Storyline prompts
    print("\n Thank you for coming to Granny's rescue.")
    time.sleep(a)
    print("\n You are at a crossroad with 2 doors.")
    time.sleep(a)
    cross_roads_main()


def cross_roads_main():
    # Main function allowing user to proceed
    print("\n WILL YOU TAKE THE DOOR ON THE LEFT OR RIGHT? (L or R)")
    # convert the player's input() to lower_case
    answer = input(">").lower().strip()
    # if player typed "left" or "l" lead him to bear_den()
    if answer == "l":
        bear_den()
    # else if player typed "right" or "r" lead him to monster_den()
    elif answer == "r":
        monster_den()
    elif answer == "":
        # if input blank back to cross_roads_main() indicating invalid entry
        print("\n ------------------------------------------ ")
        print("\n ***** INVALID ENTRY *****")
        print("\n ***** PLEASE ENTER A VALID ANSWER *****")
        print("\n ------------------------------------------ ")
        cross_roads_main()
    else:
        # if input wrong back to cross_roads_main()indicating incorrect entry
        print("\n ------------------------------------------ ")
        print("\n ***** INCORRECT ANSWER ***** ")
        print("\n ***** PLEASE ENTER A CORRECT ANSWER ***** ")
        print("\n ------------------------------------------ ")
        cross_roads_main()


def bear_den():
    # Storyline prompts
    print("\n You have entered the bear's den")
    time.sleep(a)
    print("\n You see two doors.")
    time.sleep(a)
    print("\n Door 1 is guarded by a pot of honey")
    time.sleep(a)
    print("\n Door 2 is guarded by the sleeping bear")
    time.sleep(a)
    bear_den_main()


def bear_den_main():
    # Main function allowing user to proceed
    print("\n WHICH DOOR WILL YOU CHOOSE TO TAKE? (1 or 2) ?")
    print("\n 1. Door guarded by the honey jar.")
    print("\n 2. Door guarded by the sleeping bear")
    # convert the player's input() to lower_case
    answer = input(">").lower().strip()
    # if player typed "1" game over()
    if answer == "1":
        game_over()
    # else if player typed "2" lead him to dungeon_den()
    elif answer == "2":
        dungeon_den()
    elif answer == "":
        # if input blank back to bear_den_main() indicating invalid entry
        print("\n ------------------------------------------ ")
        print("\n ***** INVALID ENTRY *****")
        print("\n ***** PLEASE ENTER A VALID ANSWER *****")
        print("\n ------------------------------------------ ")
        bear_den_main()
    else:
        # if input wrong back to bear_den_main()indicating incorrect entry
        print("\n ------------------------------------------ ")
        print("\n ***** INCORRECT ANSWER ***** ")
        print("\n ***** PLEASE ENTER A CORRECT ANSWER ***** ")
        print("\n ------------------------------------------ ")
        bear_den_main()


def monster_den():
    # Storyline prompts
    print("\n You have entered the monster den")
    time.sleep(a)
    print("\n The monster is eating lunch...")
    time.sleep(a)
    print("\n you just have a few seconds to get through..")
    time.sleep(a)
    print("\n You see two windows.")
    time.sleep(a)
    print("\n Window 1 is open but very small")
    time.sleep(a)
    print("\n Window 2 is closed but big enough for you to fit through")
    time.sleep(a)
    monster_den_main()


def monster_den_main():
    # Main function allowing user to proceed
    print("\n WHICH DOOR WILL YOU CHOOSE TO TAKE (1 or 2) ?")
    print("\n 1. Squeeze through the small window")
    print("\n 2. Open the bigger window and comfortably slide through")
    # convert the player's input() to lower_case
    answer = input(">").lower().strip()
    # if player typed "1" dungeon_den()
    if answer == "1":
        dungeon_den()
    # else if player typed "2" lead him to game_over()
    elif answer == "2":
        game_over()
    elif answer == "":
        # if input blank back to monster_den_main() indicating invalid entry
        print("\n ------------------------------------------ ")
        print("\n ***** INVALID ENTRY *****")
        print("\n ***** PLEASE ENTER A VALID ANSWER *****")
        print("\n ------------------------------------------ ")
        monster_den_main()
    else:
        # if input wrong back to monster_den_main()indicating incorrect entry
        print("\n ------------------------------------------ ")
        print("\n ***** INCORRECT ANSWER ***** ")
        print("\n ***** PLEASE ENTER A CORRECT ANSWER ***** ")
        print("\n ------------------------------------------ ")
        monster_den_main()


def dungeon_den():
    # Storyline prompts.
    print("\n Well done! ")
    time.sleep(a)
    print("\n You have now entered the witch's dungeon den.")
    time.sleep(a)
    print("\n Again you see two doors")
    time.sleep(a)
    print("\n Door 1 will lead you through a room with a sleeping snake")
    time.sleep(a)
    print("\n Door 2 will lead you through a room with a starving tiger")
    time.sleep(a)
    dungeon_den_main()


def dungeon_den_main():
    # Main function allowing user to proceed
    print("\n WHICH DOOR WILL YOU CHOOSE TO TAKE (1 or 2) ?")
    print("\n 1. Door leading to room with a sleeping snake.")
    print("\n 2. Door leading to room with starving tiger")
    # convert the player's input() to lower_case
    answer = input(">").lower().strip()
    # if player typed "1" game over()
    if answer == "1":
        game_over_1()
    # else if player typed "2" game_win()
    elif answer == "2":
        game_win()
    elif answer == "":
        # if input blank back to dungeon_den_main() indicating invalid entry
        print("\n ------------------------------------------ ")
        print("\n ***** INVALID ENTRY *****")
        print("\n ***** PLEASE ENTER A VALID ANSWER *****")
        print("\n ------------------------------------------ ")
        dungeon_den_main()
    else:
        # if input wrong back to dungeon_den_main()indicating incorrect entry
        print("\n ------------------------------------------ ")
        print("\n ***** INCORRECT ANSWER ***** ")
        print("\n ***** PLEASE ENTER A CORRECT ANSWER ***** ")
        print("\n ------------------------------------------ ")
        dungeon_den_main()

def game_over():
    # print "reason" for game over
    print("\n Sorry there was nothing beyond ...")
    time.sleep(a)
    print("\n and you fell down the cliff!")
    time.sleep(a)
    print("\n ------------------------------------------ ")
    print("\n ***** GAME OVER! *****")
    print("\n ------------------------------------------ ")
    time.sleep(a)
    # ask player to play again or not by activating play_again() function
    play_again()


def game_over_1():
    # print "reason" for game over
    print("\n The sleeping snake could feel the vibrations")
    time.sleep(a)
    print("\n as you entered the room and woke....")
    time.sleep(a)
    print("\n ------------------------------------------ ")
    print("\n ***** GAME OVER! *****")
    print("\n ------------------------------------------ ")
    time.sleep(a)
    # ask player to play again or not by activating play_again() function
    play_again()


def game_win():
    # print the "reason" in a new line (\n)
    print("\n By the time you came into the room ..")
    time.sleep(a)
    print("\n ...the tiger had been starving for 2 years and died!")
    time.sleep(a)
    print("\n You could walk through the door..")
    time.sleep(a)
    print("\n And exit out into the garden where Granny was kept")
    time.sleep(a)
    print("\n WELL DONE ON RESCUING GRANNY!")
    # ask player to play again or not by activating play_again() function
    play_again()


def play_again():
    print("\n DO YOU WANT TO PLAY AGAIN ?(y or n)")
    # convert the player's input to lower_case
    answer = input(">").lower().strip()
    if answer == "y":
        # take player to start()
        start()
    elif answer == "n":
        # exit() the program
        print("\n Sorry to see you go")
        print("\n Granny hopes you will return")
        exit()
    else:
        # return to start()
        start()


# start the game
start()
