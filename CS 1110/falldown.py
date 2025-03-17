import uvage
import random

camera = uvage.Camera(600, 800)
camera.clear("white")
game_on = False
score = 0
player = uvage.from_color(300, 400, "red", 15, 15)
player_width = 20
player_height = 20
player_score = 0
game_end = False
time = 0

walls = [
    uvage.from_color(0, 400, "white", 10, 800),
    uvage.from_color(600, 400, "white", 10, 800),
    uvage.from_color(300, 0, "white", 600, 10),
    uvage.from_color(300, 800, "white", 600, 10)
]

def floor_dimensions():
    floor_width = 500
    gap_size = 100
    floor1_x = random.randint((0 - 250), 250)
    floor2_x = floor1_x + floor_width + gap_size
    return [floor1_x, floor2_x]



dimension_list = floor_dimensions()
floor1_1 = uvage.from_color(dimension_list[0], 800, "black", 500, 25)
floor1_2 = uvage.from_color(dimension_list[1], 800, "black", 500, 25)

dimension_list = floor_dimensions()
floor2_1 = uvage.from_color(dimension_list[0], 700, "black", 500, 25)
floor2_2 = uvage.from_color(dimension_list[1], 700, "black", 500, 25)

dimension_list = floor_dimensions()
floor3_1 = uvage.from_color(dimension_list[0], 600, "black", 500, 25)
floor3_2 = uvage.from_color(dimension_list[1], 600, "black", 500, 25)

dimension_list = floor_dimensions()
floor4_1 = uvage.from_color(dimension_list[0], 500, "black", 500, 25)
floor4_2 = uvage.from_color(dimension_list[1], 500, "black", 500, 25)

dimension_list = floor_dimensions()
floor5_1 = uvage.from_color(dimension_list[0], 400, "black", 500, 25)
floor5_2 = uvage.from_color(dimension_list[1], 400, "black", 500, 25)

dimension_list = floor_dimensions()
floor6_1 = uvage.from_color(dimension_list[0], 300, "black", 500, 25)
floor6_2 = uvage.from_color(dimension_list[1], 300, "black", 500, 25)

dimension_list = floor_dimensions()
floor7_1 = uvage.from_color(dimension_list[0], 200, "black", 500, 25)
floor7_2 = uvage.from_color(dimension_list[1], 200, "black", 500, 25)

dimension_list = floor_dimensions()
floor8_1 = uvage.from_color(dimension_list[0], 100, "black", 500, 25)
floor8_2 = uvage.from_color(dimension_list[1], 100, "black", 500, 25)

floors = [
    floor8_1, floor8_2, floor7_1, floor7_2, floor6_1, floor6_2, floor5_1, floor5_2, floor4_1, floor4_2, floor3_1,
    floor3_2, floor2_1, floor2_2, floor1_1, floor1_2
]

def make_new_floor():
    dimension_list = floor_dimensions()
    floors.append(uvage.from_color(dimension_list[0], 800, "black", 500, 25))
    floors.append(uvage.from_color(dimension_list[1], 800, "black", 500, 25))

def tick():
    global game_on
    global time
    global game_end
    global player_score
    if not game_on and (not game_end): # Start screen
        camera.draw("Press space to start", 50, "black", 300, 100)
    if uvage.is_pressing("space"):
        camera.clear("white")
        game_on = True
        camera.draw(player)

    if game_on: # Player movement plus side wall collision
        player.speedy = 7
        if uvage.is_pressing("left arrow"):
            player.x -= 2.5
        if uvage.is_pressing("right arrow"):
            player.x += 2.5
        camera.clear("white")
        camera.draw(player)
    if player.touches(walls[0]):
        player.move_to_stop_overlapping(walls[0])
    if player.touches(walls[1]):
        player.move_to_stop_overlapping(walls[1])



    for wall in walls: # Drawing walls + moving floors + removal/creation of floors
        camera.draw(wall)
    if game_on:
        for items in floors:
            camera.draw(items)
            items.speedy = -1
            items.move_speed()
        for item in floors:
            if item.y < 0:
                floors.remove(item)
                floors.remove(floors[0])
                make_new_floor()

    if game_on: # Collision with top + game over screen
        if player.touches(walls[2]):
            game_end = True
            game_on = False
            for item in floors:
                item.speedy = 0
            camera.draw("GAME OVER", 50, "red", 300, 100)


    if game_on: # floor collision
        for items in floors:
            if player.touches(items):
                player.move_to_stop_overlapping(items)
        if player.touches(walls[3]):
            player.move_to_stop_overlapping(walls[3])

    if game_on: # points
        time += .02
        player_score = int(time)
        camera.draw("Score: " + str(player_score), 50, "blue", 500, 50)

    player.move_speed()
    camera.display()

ticks_per_second = 60
uvage.timer_loop(ticks_per_second, tick)
