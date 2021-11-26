<h1 align="center">Granny's Garden</h1>

[View the live project here.](https://grannys-garden.herokuapp.com/)
<h2 align="center"><img src="readme/images/screenshot.png" alt="Mock Terminal Screen Shot" width="850" height="550"></h2>

<p style="justify">Granny's Garden is a Python terminal game that runs in a mock terminal on Heroku. Users need to try and save Granny, who the wicked witch has kidnapped.</p>

### Origin of the game

Granny's Garden is a logic game based on the educational adventure game created for the British BBC Microcomputer, released in 1983. You can read more about it on [Wikipedia](https://en.wikipedia.org/wiki/Granny%27s_Garden). 

# How to play

<p style="justify">There is an introduction storyline, which speaks of how the wicked witch kidnapped Granny from her garden.</p> 

<p style="justify">The player may proceed further if they wish to rescue granny.  It takes the player through a myriad of paths through the game.</p> 

<p style="justify">Eventually, the player will complete the game by either losing as the incorrect path was chosen or winning after following the correct route and rescuing granny.</p> 

<p style="justify">At every stage, there are two routes. Typing a wrong answer will return a response of an incorrect answer. It also becomes a checkpoint to see if the player wants to continue playing or exit the game, allowing the player to leave the game at any stage without feeling trapped. 

If the user continues to type an incorrect answer, it will take them
to the play_again() function to check if they still want to play.
</p> 

# Data Model
The flowchart created on 
[Lucid Charts](https://www.lucidchart.com/pages/) gives the logic of the game.

<h2 align="center"><img src="readme/images/flowchart.png" alt="Website Screen Shots" width="850" height="700"></h2>

# Features

- Introduction
    - The wicked witch has kidnapped granny.
    - The player is given the option to rescue granny.
    - If the play agrees, the game proceeds.
    - If the player does not wish to, the game will end.
    - If the player types an incorrect option, they return to start().
    - For example, (y or n) can be typed in either case, but it has to be "y" or "n". 
    - If a player enters a blank response it will be flagged up with "INVALID ENTRY".
    - If a player enters an incorrect response it will be flagged up with "INCORRECT ENTRY".
    - A blank or incorrect response after highlightling it to the player will return to the question to continue playing.
    - Each function has been divided into two parts . 
    - The first part is the storyline.
    - The second part allows the user to take decisions.
    
   <h2 align="center"><img src="readme/images/f_start.png" alt="Mock screenshot" width="500" height="200"></h2>
   <h2 align="center"><img src="readme/images/f_start_main.png" alt="Mock screenshot" width="500" height="450"></h2>
   <h2 align="center"><img src="readme/images/p_start.png" alt="Mock screenshot" width="500" height="150"></h2>
   
   <h2 align="center"><img src="readme/images/p_start_main.png" alt="Mock screenshot" width="500" height="50"></h2>

- Crossroads
    - This is the first point of decision if the player proceeds to rescue granny
    - The player is given the option to turn left or right.
    - Left will take the player to the bear's den
    - Right will take the player to the monster's den
    - If a player enters a blank response it will be flagged up with "INVALID ENTRY".
    - If a player enters an incorrect response it will be flagged up with "INCORRECT ENTRY".
    - A blank or incorrect response after highlightling it to the player will return to the question to continue playing.
    <h2 align="center"><img src="readme/images/f_crossroads.png" alt="Mock screenshot" width="500" height="150"></h2>
    <h2 align="center"><img src="readme/images/f_crossroads_main.png" alt="Mock screenshot" width="500" height="350"></h2>

- Bear and Monster Den

    - At the next level, the player will need to proceed through either the Bear or Monster den.
    - Both den's will lead the player to either the witch's dungeon or lose the game.
    - Through both options if a player enters a blank response it will be flagged up with "INVALID ENTRY".
    - Through both options if a player enters an incorrect response it will be flagged up with "INCORRECT ENTRY".
    - A blank or incorrect response after highlightling it to the player will return to the question to continue playing.
<h2 align="center"><img src="readme/images/f_bear.png" alt="Mock screenshot" width="500" height="150"></h2>
<h2 align="center"><img src="readme/images/f_bear_main.png" alt="Mock screenshot" width="500" height="350"></h2>
<h2 align="center"><img src="readme/images/f_monster.png" alt="Mock screenshot" width="500" height="200"></h2>
<h2 align="center"><img src="readme/images/f_monster_main.png" alt="Mock screenshot" width="500" height="350"></h2>
<h2 align="center"><img src="readme/images/p_bear.png" alt="Mock screenshot" width="500" height="200"></h2>
<h2 align="center"><img src="readme/images/p_monster.png" alt="Mock screenshot" width="500" height="200"></h2>

- Dungeon Den

    - If the player is successful from the previous level, they will enter the dungeon den.
    - Here, the player will have two options leading to a win or loss.
    - If a player enters a blank response it will be flagged up with "INVALID ENTRY".
    - If a player enters an incorrect response it will be flagged up with "INCORRECT ENTRY".
    - A blank or incorrect response after highlightling it to the player will return to the question to continue playing.
<h2 align="center"><img src="readme/images/f_dungeon.png" alt="Mock screenshot" width="500" height="200"></h2>
<h2 align="center"><img src="readme/images/p_dungeon.png" alt="Mock screenshot" width="500" height="250"></h2>

- Choices

    - At all levels the player is presented with two choices.
    - If a player enters a blank response it will be flagged up with "INVALID ENTRY".
    - If a player enters an incorrect response it will be flagged up with "INCORRECT ENTRY".
    - A blank or incorrect response after highlightling it to the player will return to the question to continue playing.
<h2 align="center"><img src="readme/images/p_invalid.png" alt="Mock screenshot" width="500" height="200"></h2>
<h2 align="center"><img src="readme/images/p_incorrect.png" alt="Mock screenshot" width="500" height="250"></h2>
    


- Conclusion 
    - The game concludes with the player choosing the correct path and winning by rescuing granny.
    - By choosing the wrong path , the player loses and the game is over.

<h2 align="center"><img src="readme/images/f_win.png" alt="Mock screenshot" width="500" height="200"></h2>
<h2 align="center"><img src="readme/images/p_gamewin.png" alt="Mock screenshot" width="500" height="250"></h2>
<h2 align="center"><img src="readme/images/f_over.png" alt="Mock screenshot" width="500" height="150"></h2>
<h2 align="center"><img src="readme/images/p_gameover.png" alt="Mock screenshot" width="500" height="200"></h2>


- Play again
    
<h2 align="center"><img src="readme/images/f_play.png" alt="Mock screenshot" width="500" height="300"></h2>
<h2 align="center"><img src="readme/images/p_playagain.png" alt="Mock screenshot" width="500" height="50"></h2>

# Testing

I have manually tested this project by doing the following:

- Passed the code through PEP8 linter and confirmed there are no problems.
- Given invalid options to ensure the function will check if the user wanted to continue playing or quit the game.
- Tested in my local terminal and Heroku terminal.
-  Tested by peers and my mentor.

# Bugs
### Solved Bugs

When I wrote the project, notable errors included:

- Unwanted white spaces.
- Incorrect indentation, resulting in the program not functioning correctly.
- Incorrect line spaces between functions.
- Within each function, the nested "if" statement within the "else" statement did not work properly as the structure was incorrect.
- It was found that if the player added an extra blank space before entering a correct option, it was considered incorrect. And the incorrect option loop was followed. It has been resolved by using .strip(). 
- Incorrect validation : Another error which was found when entering a BLANK entry or an INCORRECT entry , the game simply looped in both cases to the beginning of the function without giving any reason to the user. This was corrected , so the user is informed of their mistake and the question is asked to them again.
- Occasionally, the terminal in Heroku hangs while playing the game. It is perhaps a connectivity issue between git and the Heroku terminal. In such a case pressing "Run program" restarts and then functions properly. 

### Remaining Bugs
- No bugs remaining.

### Validator Testing
 - PEP8 

    - No errors have been returned from PEP8online.com.

    <h2 align="center"><img src="readme/images/pep8.png" alt="Website Screen Shots" width="750" height="400"></h2>

# Creation and Deployment

The project has been created on gitpod and deployed to GitHub Pages. 

It was then deployed using a mock terminal for Heroku.

- Steps for deployment to Heroku Mock Terminal
    - Fork or clone this repository.
    - Create a new Heroku app.
    - Set the buildbacks to Python and NodeJS , in that order.
    - Link the Heroku app to the repository.
    - Click on deploy.

# Credits
### Code & Creation

-   [The Coding pie](https://thecodingpie.com/post/make-your-own-text-based-adventure-game-in-python3) 

-   [Lucid Charts](https://www.lucidchart.com/pages/) 

### Inspiration

-  [Granny's Garden](https://en.wikipedia.org/wiki/Granny%27s_Garden)

### Content & Deployment

- All content for the game is written by the developer.
- Language and Grammar for the Readme.md corrected using [Grammarly](https://www.grammarly.com).
- Code Institute for the deployment terminal.


### Media

- Mock Terminal Screen Shot was sourced from [AmIresponsive](http://ami.responsivedesign.is/) and desktop screenshots.


### Acknowledgement(s)

-  I would like to thank my mentor Adegbenga Adeye. His guidance in giving constructive feedback through all stages of site design and development has been most valuable.