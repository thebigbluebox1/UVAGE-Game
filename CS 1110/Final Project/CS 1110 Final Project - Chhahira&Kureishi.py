# Rohan Chhahira - fbt2gt
# Namai Kureishi - zap5dt

# Goal of the game is to catch as many sweets as you can (increasing your score), without catching veggies which
# decrease your score and cause you to lose and health and possibly the entire game.

# Basic features - We've already included user input via the a, d, left/right arrow to move the sprites to catch the sweets.
# We've also added game over screens that are caused by player health reaching zero or reaching the end of the game
# (the entire 60 seconds the game is live). We also incorporated images with the game's background, the sweets, veggies,
# players, etc. They are all local files not urls.

# Additional features - We've added a restart screen with more user inputs that allows the players to restart from any of the
# five stages in the game. Enemies have also been added in the form of veggies as they drop from the sky and cause the
# player to lose 10 hp. Sweets act as collectibles since they disappear when touched and add to the player's score. There
# is also a timer that counts down from 60. At every 12 second interval, the stage/level changes. These changes include
# faster dropping speeds, more items (sweets/veggies), etc. There is also a health bar for each of the two players.
# Whenever one of the players reaches 0 hp, they will no longer be able to move. If both players reach 0 hp, the game
# over screen will appear as both players have lost. If one or both players make it through the entire 60 seconds
# without getting to 0 hp, the game over screen will also appear, but it will show which player won by getting a higher score.

# To recap, we've included restarting when the game is over, enemies, collectibles, a timer, (two) health bars, two
# players simultaneously, and multiple levels.

# Originally, we were going to make it so that the players could not advance to the next level unless they'd
# acquired a certain amount of points, but we decided to remove that feature.

# Instructions:
# For player one, use the a and d keys to move your avatar. For player two, use the left and right arrow keys.
# Collect as many sweets as you can by touching them. When you get to stage 3, veggies will spawn. Avoid them as
# touching them will lower your score and cause you to lose hp. You can hit ten veggies before you run out of hp.
# When you do, you will no longer be able to move. If both players lose all their hp, the game will be over and you lose.
# If one or both players survive until the end of the game (a total of 60 seconds), then you will win. If both players
# make it to the end of the game, the one with the highest score will be declared the winner. If you win or lose, you can
# restart from any of the five stages.


# importing uvage, random, and setting variables for game start
import uvage
import random
camera = uvage.Camera(800, 600)
game_on = False
game_end = False
fb1score = 0
fb2score = 0
time = 60 # make sure to change to 60
healthp1 = 100
healthp2 = 100
coordp1 = 75
coordp2 = 725
health_bar_x_p1 = 100
health_bar_x_p2 = 700

#made baskets, food, and wood sprites
#sets food/wood at random locations before the game starts
fb1 = uvage.from_image(75, 520, "player 1 facing right.png")
fb2 = uvage.from_image(725, 520, "player 2 facing left.png")
background= uvage.from_image(400,300,"candybackground_1.jpeg")
darkchocolate = uvage.from_image(random.randint(50, 750),random.randint(-800, -75), "darkchocolate_1_1.png")
candycane= uvage.from_image(random.randint(50, 750),random.randint(-800, -75), "candycane_1.png")
melonbread = uvage.from_image(random.randint(50, 750),random.randint(-800, -75), "meloncake_1_1_1.gif")
cinnamonbun = uvage.from_image(random.randint(50, 750),random.randint(-800, -75), "cinnamon_3.png")
shortcake = uvage.from_image(random.randint(50, 750),random.randint(-800, -75), "strawberryshortcake_1.png")
cake = uvage.from_image(random.randint(50, 750),random.randint(-800, -75), "cakeeee_1.png")
pie = uvage.from_image(random.randint(50, 750),random.randint(-800, -75), "pie_1_1.png")
bread = uvage.from_image(random.randint(50, 750),random.randint(-800, -75), "bread_1.png")
toast = uvage.from_image(random.randint(50, 750),random.randint(-800, -75), "breadtoast_1.png")
blueberrycake = uvage.from_image(random.randint(50, 750),random.randint(-800, -75), "blueberrycheesecake_1.png")
tiramisu = uvage.from_image(random.randint(50, 750),random.randint(-800, -75), "tiramisu_1_2.png")
broccoli= uvage.from_image(random.randint(50, 750),random.randint(-800, -75), "broc_1.png")
cucumber= uvage.from_image(random.randint(50, 750),random.randint(-800, -75), "cucumber_1.png")
lettuce= uvage.from_image(random.randint(50, 750),random.randint(-800, -75), "lett_1.png")
#list to hold the food
foodlist = [darkchocolate, candycane, melonbread, cinnamonbun, shortcake, cake, pie, bread, toast, blueberrycake, tiramisu]
veggielist =[broccoli, cucumber, lettuce]

def tick():
   global game_on, fb1, fb2, foodlist, fb1score, fb2score, time, game_end, healthp1, healthp2, coordp1, coordp2, health_bar_x_p1, health_bar_x_p2
   camera.clear('light blue')
   camera.draw(background)
   health_bar_p1 = uvage.from_color(health_bar_x_p1, 85, "magenta", 200, 20)
   health_bar_p2 = uvage.from_color(health_bar_x_p2, 85, "magenta", 200, 20)
# draws health bar and background

   if not game_on and not game_end: # game start screen setup
       camera.draw(uvage.from_text(400, 200, 'Press the space bar to play!', 50, "magenta", italic = True))
       camera.draw(uvage.from_text(400, 250, 'Rules:', 50, "magenta", italic = True))
       camera.draw(uvage.from_text(400, 300, 'Catch as many food items as you can!', 45, "magenta", italic = True))
       camera.draw(uvage.from_text(400, 350, "Avoid veggies! They\'ll lower your score and health!", 45, "magenta", italic = True))
   # space starts game
       if uvage.is_pressing("space"):
            game_on = True
   if not game_on and game_end: #restart game feature
       for food in foodlist:
           food.y = (random.randint(40, 400))*-1
       for veggie in veggielist:
           veggie.y = (random.randint(40, 400))*-1
       camera.draw(uvage.from_text(400, 200, "Press 1 to play again from Stage 1!", 50, "magenta", italic = True))
       camera.draw(uvage.from_text(400, 250, "Press 2 to play again from Stage 2!", 50, "magenta", italic = True))
       camera.draw(uvage.from_text(400, 300, "Press 3 to play again from Stage 3!", 50, "magenta", italic = True))
       camera.draw(uvage.from_text(400, 350, "Press 4 to play again from Stage 4!", 50, "magenta", italic = True))
       camera.draw(uvage.from_text(400, 400, "Press 5 to play again from the Final Stage!", 50, "magenta", italic = True))
       if uvage.is_pressing("1"):
           game_on = True
           game_end = False
           time = 60 # make sure to change to 60
           fb1score = 0
           fb2score = 0
           healthp1 = 100
           healthp2 = 100
           health_bar_x_p1 = 100
           health_bar_x_p2 = 700
       if uvage.is_pressing("2"):
           game_on = True
           game_end = False
           time = 48 # make sure to change to 48
           fb1score = 0
           fb2score = 0
           healthp1 = 100
           healthp2 = 100
           health_bar_x_p1 = 100
           health_bar_x_p2 = 700
       if uvage.is_pressing("3"):
           game_on = True
           game_end = False
           time = 36 # make sure to change to 36
           fb1score = 0
           fb2score = 0
           healthp1 = 100
           healthp2 = 100
           health_bar_x_p1 = 100
           health_bar_x_p2 = 700
       if uvage.is_pressing("4"):
           game_on = True
           game_end = False
           time = 24 # make sure to change to 24
           fb1score = 0
           fb2score = 0
           healthp1 = 100
           healthp2 = 100
           health_bar_x_p1 = 100
           health_bar_x_p2 = 700
       if uvage.is_pressing("5"):
           game_on = True
           game_end = False
           time = 12 # make sure to change to 12
           fb1score = 0
           fb2score = 0
           healthp1 = 100
           healthp2 = 100
           health_bar_x_p1 = 100
           health_bar_x_p2 = 700
   # making the game start from each stage by changing the time


   if healthp1 == 0 and healthp2 == 0: # game over screen if both players' health reaches 0
       game_on = False
       game_end = True
       camera.draw(uvage.from_text(400, 100, "Game over!", 50, "magenta", italic = True))
       camera.draw(uvage.from_text(400, 150, "You caught too many veggies!", 50, "magenta", italic = True))




   # time only goes down if it is above 0
   if game_on and time > 0:
       time-=.03

   else: #uses final scores to announce winner if both scores are above 0
       if time <= 0 and healthp1 > 0 and healthp2 > 0:
           if fb1score > fb2score:
               game_end= True
               game_on = False
               camera.draw(uvage.from_text(400, 50, 'Game Over: Player 1 wins!', 50, "magenta", italic= True))

           if fb1score < fb2score:
               game_end= True
               game_on = False
               camera.draw(uvage.from_text(400, 50, 'Game Over: Player 2 wins!', 50, "magenta", italic = True))

           if time == 0 and fb1score == fb2score:
               game_end= True
               game_on = False
               camera.draw(uvage.from_text(400, 50, 'Tie!', 50, "magenta", italic = True))

   # setting up health bar visuals and controls which only work when the game is on and health is greater than 0
   if game_on:
       camera.draw(str(int(time)), 60, 'magenta', 400, 30) # displays time
       camera.draw(("Health: " + str(healthp1) + "/100"),30, "magenta", 80, 60)
       camera.draw(health_bar_p1)
       camera.draw(health_bar_p2)
       camera.draw(("Health: " + str(healthp2) + "/100"), 30, "magenta", 720, 60)
       if uvage.is_pressing("a") and healthp1 > 0:
           coordp1 -= 15
           fb1 = uvage.from_image(coordp1, 520, "player 1 facing left.png")

       if uvage.is_pressing("d") and healthp1 > 0:
           coordp1 += 15
           fb1 = uvage.from_image(coordp1, 520, "player 1 facing right.png")

       if uvage.is_pressing("left arrow") and healthp2 > 0:
           coordp2 -= 15
           fb2 = uvage.from_image(coordp2, 520, "player 2 facing left.png")

       if uvage.is_pressing("right arrow") and healthp2 > 0:
           coordp2 += 15
           fb2 = uvage.from_image(coordp2, 520, "player 2 facing right.png")


      #stops players from going past left/right of the screen
       if fb1.x < camera.x - 370:
           fb1.x = camera.x - 370

       if fb1.x > camera.x + 370:
           fb1.x = camera.x + 370

       if fb2.x < camera.x - 370:
           fb2.x = camera.x - 370

       if fb2.x > camera.x + 370:
           fb2.x = camera.x + 370

       for b in veggielist: # setting up the veggie mechanics (if touched, they lower player hp and score, resetting position)
           camera.draw(b)
           if game_on:
               b.y += 0
               if time <= 36 and time >= 24:
                   b.y += 6
               if time <= 24 and time >= 12:
                   b.y += 10
               if time <= 12 and time >= 0:
                   b.center = [random.randint(50, 750), -40]
                   b.y += 0
               if b.touches(fb1) and healthp1 > 0:
                   b.move_to_stop_overlapping(fb1)
                   b.center = [random.randint(50, 750), -40]
                   fb1score -= 3
                   healthp1 -= 10
                   health_bar_x_p1 -= 20
               if b.touches(fb2) and healthp2 > 0:
                   b.move_to_stop_overlapping(fb2)
                   b.center = [random.randint(50, 750), -40]
                   fb2score -= 3
                   healthp2 -= 10
                   health_bar_x_p2 += 20
               if b.y > camera.y + 300 and b.x < 400:
                   b.center = [random.randint(50, 750), -40]

               if b.y > camera.y + 300 and b.x > 0:
                   b.center = [random.randint(50, 750), -40]

       #draws food
       for food in foodlist:
           camera.draw(food)
          #makes food move if game is on
           #displays score and players' sides
           if game_on:
               food.y += 3
               camera.draw(str(int(fb1score)), 40, 'magenta', 200, 30)
               camera.draw(str(int(fb2score)), 40, 'magenta', 600, 30)
               camera.draw('Player 1', 30, 'magenta', 60, 30)
               camera.draw('Player 2', 30, 'magenta', 740, 30)

               #changes speed depending on how much time is left/what stage players are at

               if time <= 48 and time>=36:
                   food.y += 4

               if time <= 36 and time >=24:
                   food.y += 6

               if time <= 24 and time >=12:
                   food.y += 10

               if time <= 12 and time >= 0:
                   food.y += 25



               #announces the stage the players are at for one second
               if time <= 60 and time>=59:
                   camera.draw(uvage.from_text(400, 300, 'Stage 1: Catch the sweets!', 50, "magenta", italic =True))
               if time <= 48 and time>=47:
                   camera.draw(uvage.from_text(400, 300, 'Stage 2: Speed up!', 50, "magenta", italic = True))

               if time <= 36 and time >=35:
                   camera.draw(uvage.from_text(400, 300, 'Stage 3: Avoid the veggies!', 50, "magenta", italic = True))

               if time <= 24 and time >=23:
                   camera.draw(uvage.from_text(400, 300, 'Stage 4: Keep collecting sweets!!', 50, "magenta", italic = True))

               if time <= 12 and time >= 11:
                   camera.draw(uvage.from_text(400, 300, 'Final Stage: Sugar rush!', 50, "magenta", italic = True))



           #stops food/wood from going through the basket
           #resets food if it touches basket
           #adds 1 to score when food touches each basket
           if food.touches(fb1) and healthp1 > 0:
               food.move_to_stop_overlapping(fb1)
               food.center = [random.randint(50, 750),-40] #resets food
               fb1score += 1 #adds 1 to score

           if food.touches(fb2) and healthp2 > 0:
               food.move_to_stop_overlapping(fb2)
               food.center = [random.randint(50, 750),-40]
               fb2score += 1

           #resets food if it touches floor
           if food.y > camera.y + 300 and food.x < 400:
               food.center = [random.randint(50, 750), -40]

           if food.y > camera.y + 300 and food.x > 0:
               food.center = [random.randint(50, 750), -40]

   #draws paddles, displays game
   camera.draw(fb1)
   camera.draw(fb2)
   camera.display()


uvage.timer_loop(30, tick)