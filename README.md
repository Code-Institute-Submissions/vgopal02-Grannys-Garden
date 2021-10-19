<h1 align="center">Granny's Garden</h1>

[View the live project here.](https://grannys-garden.herokuapp.com/)
<h2 align="center"><img src="readme/images/screenshot.png" alt="Mock Terminal Screen Shot" width="850" height="550"></h2>

<p style="justify">Granny's Garden is a Python terminal game that runs in a mock terminal on Heroku. Users need to try and save Granny, who the wicked witch has kidnapped.</p>

### Origin of the game

Granny's Garden is a logic game based on the educational adventure game created for the British BBC Microcomputer, released in 1983. You can read more about it on [Wikipedia](https://en.wikipedia.org/wiki/Granny%27s_Garden). 

# How to play

<p style="justify">The user is presented with an introduction storyline, which speaks of how the wicked witch kidnapped Granny from her garden.</p> 

<p style="justify">The player is then asked if they wish to rescue granny. If they agree, the game proceeds further. It takes the player through a myriad of paths through the game.</p> 

<p style="justify">Eventually, the player will complete the game by either losing as the incorrect path was chosen or winning after following the correct route and rescuing granny.</p> 

<p style="justify">At every stage, the player is presented with two routes. Typing an incorrect answer will alert the player with a response of  'Incorrect answer'. At that point, it also becomes a checkpoint to see if the player wants to continue playing or exit the game. This allows the player to leave the game at any stage without feeling trapped. 

If the user continues to type an incorrect answer, it will take them
to the play_again() function to check if they still want to play.
</p> 

# Data Model
The flowchart created on 
[Lucid Charts](https://www.lucidchart.com/pages/) gives the logic of the game.

<h2 align="center"><img src="readme/images/flowchart.png" alt="Website Screen Shots" width="850" height="700"></h2>
    
   
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

### Remaining Bugs
- No bugs remaining.

### Validator Testing
 - PEP8 

    - No errors were returned from PEP8online.com.

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

### Content

-   All content was written by the developer.
-   Language and Grammar for the Readme file was corrected using [Grammarly](https://www.grammarly.com).


### Media

- Mock Terminal Screen Shot was sourced from [AmIresponsive](ami.responsivedesign).


### Acknowledgement(s)

-  I would like to thank my mentor Adegbenga Adeye. His guidance in giving constructive feedback through all stages of site design and development has been most valuable.