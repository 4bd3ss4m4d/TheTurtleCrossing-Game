# The Turtle Crossing Game

from turtle import Turtle, Screen, listen, onkey
import time
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

# Constants
WIDTH = 600
HEIGHT = 600
BGCOLOR = "white"
TITLE = "The Turtle Crossing Game"


def main():
    # Set screen:
    screen = Screen()
    screen.setup(width=WIDTH, height=HEIGHT)
    screen.bgcolor(BGCOLOR)
    screen.title(TITLE)
    # Deactivate Screen Tracer
    screen.tracer(0)

    # Create player
    player = Player()
    player.go_to_start()

    # Create car manager
    car_manager = CarManager()

    # Set scoreboard
    scoreboard = Scoreboard()
    scoreboard.update_scoreboard()

    # Listen to player's key strokes
    listen()
    # Control the player
    onkey(key="z", fun=player.up)
    onkey(key="s", fun=player.down)
    onkey(key="d", fun=player.go_right)
    onkey(key="q", fun=player.go_left)

    # Game control
    game_is_on = True

    while game_is_on:
        time.sleep(0.1)
        # Update screen to see changes made to the screen
        screen.update()

        # Make cars move
        car_manager.create_cars()
        car_manager.move_cars()

        # Detect collision with car
        for car in car_manager.all_cars:
            if car.distance(player) < 20:
                scoreboard.print_game_over()
                print("Game over!")
                game_is_on = False

        # Detect successful crossing
        if player.is_at_finish_line():
            scoreboard.increment_level()
            scoreboard.update_scoreboard()
            car_manager.level_up()
            player.go_to_start()

    # Exit screen on click
    screen.exitonclick()


main()
