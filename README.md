# Extreme Brick Out

## Demo
Demo Video: https://youtu.be/Kq7JzU8bOaQ

## GitHub Repository
GitHub Repo: https://github.com/HydroShock1/ANGM2305-Project-Final-Brick-Out

## Description
My code is a simple game of Brick Out with my own twists to it. When you first start the game, 5 green blocks get randomly spawned in different locations each playthrough.
This randomness makes each game completely different and new from each other, but the goal is still simple. The goal is to use your paddle to bounce the ball away from the
bottom and break as many blocks as possible. There is a timer that goes down and whenever it hits zero, the game is over and whatever high score you get is your high score.

Each time you hit a green block, the high score goes up by 1 as well as make the timer go up by 2 seconds to make the game longer. The only way to really end the game is 
getting a game over once the timer runs out and the quickest way to do this is making the ball hit the bottom of the screen. Each time the ball hits the bottom of the game,
the score goes down by 1 and the timer goes down by 5 seconds, making each hit to the bottom a game ender if too many mistakes are made. 

I wanted to make this simple, just like how the original PONG game looked, as PONG was my original choice of game before I changed it to Brick Out. I had bigger ambitions however, my ideal outcome would be this same game but with other colored blocks spawning, decreasing the time as well as well as two randomly spawning power ups. However, my powerups were too confusing to implement and adding a randomly bad red block would make the game incredibly difficult for players as you can't really change the trajectory of the ball. Another area
I wish to improve upon is my timer, as the timer randomly glitches out when increasing or decreasing. I would like to make it stable and find a different way to order it around
in my code as well as I had to implement the code into the very end for the timer to work.