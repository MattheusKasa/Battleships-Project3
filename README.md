# BATTLESHIPS

## Battleships is a python terminal game, which runs in the mock terminal on Heroku
<p>&nbsp;</p>
  
### Users can try to beat the computer by finding all of the computers battleships within a limited number of turns. Each battleship occupies one square on the board.
<p>&nbsp;</p>

## The live website can be found here: [Battleships](https://battleships-project-3.herokuapp.com/)

![Site on different screens](/Mockup-Battleships.jpg)
<p>&nbsp;</p>

## How to play
---
Battleship is based on the classic pen and paper game. You can read more about it on [Wikipedia](https://en.wikipedia.org/wiki/Battleship_(game))

In this version a board is randomly generated, the player cannot see the ships.

Guesses are marked on the board with an **-** and hits are indicated by an **X**.

The player has a total of 15 turns to make guesses and try and sink all the ships.

If all ships are hit within 15 turns, the player wins.

If any of the ships are not hit within 15 turns, the player loses.

<p>&nbsp;</p>

## Features
---
### Random board generator
- Ships are randomly placed on the board.
- The player cannot see where the ships are.

![image](/battleships%20image1.png)

- Accepts user input
- Keeps score of remaining turns

![image](/battleships%20hit.png)

- Input validation and error-checking
    - You cannot enter coordinates outside of the grid
    - You must enter a number or a letter, correctly.
    - You cannot give an empty input.
    - You cannot enter the same guess twice

![image](/battleships%20error.png)

<p>&nbsp;</p>

## Data Model
---
I decided to use a Board class as my model. The game creates an instance of the Board class to hold the board.

The Board class stores the board size, the number of ships, the position of the ships, the guesses and details such as turns left.

The class also has methods to help play the game, such as a **print** method to print out the current board.
<p>&nbsp;</p>

## Testing
---
I have manually tested this project by doing the following:

- Passed the code through PEP8 and confirmed that there are no issues.
- Given invalid inputs: strings when numbers are expected, same input twice and out of bounds inputs.
- Tested in my local terminal and the Heroku terminal.

### Validator Testing
- CI Python Linter
    - No errors were returned from the CI python Linter
    ![image](/CI%20python%20linter%20no%20errors.png)

<p>&nbsp;</p>

## Technologies Utilized
---
- Programs Used for this project
    - Python
    - Gitpod
    - Heroku

<p>&nbsp;</p>

## Issues and Errors
---
- Had an issue where the program would crash if a empty input was given. I fixed this by raising an error if a user gives an empty input, redirecting them to giving an acceptable input instead.

![image](/battleships%20no%20input.png)

<p>&nbsp;</p>

## Deployment
---
This project was deployed using Heroku
- Steps for deployment:
    - Fork or clone this repository
    - Create a new Heroku app
    - Set the buildbacks to **Python** and **NodeJS** in that order
    - Link the Heroku app to the repository
    - Click on **Deploy**

<p>&nbsp;</p>

## Credits
---

### [Dylan Israel - Youtube](https://www.youtube.com/watch?v=7Ki_2gr0rsE) - The video i watched for inspiration.

### [Austin - Montgomery](https://bigmonty12.github.io/battleship) - Website i visited for additional inspiration.


<p>&nbsp;</p>

# Mattheus Kasa, 2023

