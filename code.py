#!/usr/bin/env python3
# Created by: Joseph Kwon
# Created on: Jan 09, 2022
# This program is the final CPT video game

import constants
import stage
import ugame
import time
import random
import supervisor


def splash_scene():
    # this function is the splash scene

    # "bing chilling" for splash screen
    start_sound = open("bing.wav", "rb")
    sound = ugame.audio
    sound.stop()
    sound.mute(False)
    sound.play(start_sound)

    # imported an image and put it into a variable
    image_bank_mt_background = stage.Bank.from_bmp16("mt_game_studio.bmp")

    # sets the background image to
    background = stage.Grid(
        image_bank_mt_background, constants.SCREEN_GRID_X, constants.SCREEN_GRID_Y
    )
    background.tile(2, 2, 1)  # blank white

    background.tile(3, 2, 1)

    background.tile(4, 2, 2)

    background.tile(5, 2, 3)

    background.tile(6, 2, 4)

    background.tile(7, 2, 1)  # blank white

    background.tile(2, 3, 1)  # blank white

    background.tile(3, 3, 5)

    background.tile(4, 3, 6)

    background.tile(5, 3, 7)

    background.tile(6, 3, 8)

    background.tile(7, 3, 1)  # blank white

    background.tile(2, 4, 1)  # blank white

    background.tile(3, 4, 9)

    background.tile(4, 4, 10)

    background.tile(5, 4, 11)

    background.tile(6, 4, 12)

    background.tile(7, 4, 1)  # blank white

    background.tile(2, 5, 1)  # blank white

    background.tile(3, 5, 0)

    background.tile(4, 5, 13)

    background.tile(5, 5, 14)

    background.tile(6, 5, 0)

    background.tile(7, 5, 1)  # blank white

    # The display that will show up and refreshing it with 60 hertz
    game = stage.Stage(ugame.display, constants.FPS)
    game.layers = [background]
    game.render_block()

    # game loop to repeat forever
    while True:
        # Wait 2 seconds
        time.sleep(2.0)
        # Go to the menu scene
        menu_scene()


def menu_scene():
    # this function is the menu scene

    # set time to 0, this is used to later re-play the background music in menu
    time = 0

    # background music
    back_music = open("song.wav", "rb")
    sound = ugame.audio
    sound.stop()
    sound.mute(False)

    sound.play(back_music)

    # imported an image and put it into a variable
    image_bank_mt_background = stage.Bank.from_bmp16("mt_game_studio.bmp")

    # The Text Objects
    # Text for menu scene
    text = []
    text1 = stage.Text(
        width=29, height=12, font=None, palette=constants.RED_PALETTE, buffer=None
    )
    text1.move(20, 10)
    text1.text("United Nations")
    text.append(text1)

    text2 = stage.Text(
        width=29, height=12, font=None, palette=constants.RED_PALETTE, buffer=None
    )
    text2.move(40, 110)
    text2.text("Press Start")
    text.append(text2)

    text3 = stage.Text(
        width=29, height=12, font=None, palette=constants.RED_PALETTE, buffer=None
    )
    text3.move(10, 50)
    text3.text("Press Select for ")
    text.append(text3)

    text4 = stage.Text(
        width=29, height=12, font=None, palette=constants.RED_PALETTE, buffer=None
    )
    text4.move(10, 70)
    text4.text("Tutorial")
    text.append(text4)

    # grid of an image background
    background = stage.Grid(
        image_bank_mt_background, constants.SCREEN_GRID_X, constants.SCREEN_GRID_Y
    )

    # The display that will show up and refreshing it with 60 hertz
    game = stage.Stage(ugame.display, constants.FPS)
    game.layers = text + [background]
    game.render_block()

    # repeat forever, game loop
    # get user's button selection
    while True:
        # get user input
        keys = ugame.buttons.get_pressed()

        if keys & ugame.K_START != 0:
            game_scene()

        # start button selected
        if keys & ugame.K_SELECT != 0:
            tutorial_scene()

        # update game logic
        game.tick()  # wait until refresh rate finishes

        # makes sure the music replays if it ends
        if time >= 2457.06000098:
            sound.play(back_music)
            time = 0
        else:
            time += 1


def tutorial_scene():
    # this function is the tutorial scene

    # background music
    back_music = open("song.wav", "rb")
    sound = ugame.audio
    sound.stop()
    sound.mute(False)

    sound.play(back_music)

    # imported an image and put it into a variable
    image_bank_mt_background = stage.Bank.from_bmp16("mt_game_studio.bmp")

    # The Text Objects
    # the instructions / tutorial page
    text = []
    text1 = stage.Text(
        width=29, height=12, font=None, palette=constants.RED_PALETTE, buffer=None
    )
    text1.move(20, 10)
    text1.text("Press B to fire")
    text.append(text1)

    text2 = stage.Text(
        width=29, height=12, font=None, palette=constants.RED_PALETTE, buffer=None
    )
    text2.move(20, 100)
    text2.text("Press Select ")
    text.append(text2)

    text5 = stage.Text(
        width=29, height=12, font=None, palette=constants.RED_PALETTE, buffer=None
    )
    text5.move(20, 120)
    text5.text("to Return")
    text.append(text5)

    text3 = stage.Text(
        width=29, height=12, font=None, palette=constants.RED_PALETTE, buffer=None
    )
    text3.move(10, 50)
    text3.text("Don't get hit by ")
    text.append(text3)

    text4 = stage.Text(
        width=29, height=12, font=None, palette=constants.RED_PALETTE, buffer=None
    )
    text4.move(10, 70)
    text4.text("crusaders")
    text.append(text4)

    # grid of an image background
    background = stage.Grid(
        image_bank_mt_background, constants.SCREEN_GRID_X, constants.SCREEN_GRID_Y
    )

    # The display that will show up and refreshing it with 60 hertz
    game = stage.Stage(ugame.display, constants.FPS)
    game.layers = text + [background]
    game.render_block()

    while True:
        # get user input
        keys = ugame.buttons.get_pressed()

        # start button selected
        if keys & ugame.K_SELECT != 0:
            menu_scene()

        # update game logic
        game.tick()  # wait until refresh rate finishes


def game_scene():
    # this function is the main game scene

    # for score
    score = 0

    # outputs white text with no background since unspecified
    # height and width for scoreboard text
    score_text = stage.Text(width=29, height=14)
    score_text.clear()
    # top left corner, location
    score_text.cursor(0, 0)
    score_text.move(1, 1)
    score_text.text("Score: {0}".format(score))

    def show_alien():
        # this function takes an alien from off screen and moves it on screen
        # loops through all of the aliens
        for alien_number in range(len(aliens)):
            # checks to see if an alien has an x value less than 0
            if aliens[alien_number].x < 0:
                # if there is, take the alien and put it in a random position
                aliens[alien_number].move(
                    random.randint(
                        0 + constants.SPRITE_SIZE,
                        constants.SCREEN_X - constants.SPRITE_SIZE,
                    ),
                    constants.OFF_TOP_SCREEN,
                )
                break

    # import an image
    image_bank_background = stage.Bank.from_bmp16("space_aliens_background.bmp")
    # make sure the name within quotation matches the image file name inside Pybadge
    image_bank_sprites = stage.Bank.from_bmp16("space_aliens.bmp")

    # buttons you want to keep information on
    a_button = constants.button_state["button_up"]
    b_button = constants.button_state["button_up"]
    start_button = constants.button_state["button_up"]
    select_button = constants.button_state["button_up"]

    # get sound ready
    pew_sound = open("taco.wav", "rb")
    sound = ugame.audio
    sound.stop()
    sound.mute(False)

    # boom sound fx
    boom_sound = open("boom_sound.wav", "rb")
    sound = ugame.audio
    sound.stop()
    sound.mute(False)

    # crash sound fx
    crash_sound = open("boom.wav", "rb")
    sound = ugame.audio
    sound.stop()
    sound.mute(False)

    # create a grid of this image background
    background = stage.Grid(
        image_bank_background, constants.SCREEN_GRID_X, constants.SCREEN_GRID_Y
    )

    # picking off the fifth image from that long image, start counting from 0
    ship = stage.Sprite(
        image_bank_sprites, 5, 75, constants.SCREEN_Y - (2 * constants.SPRITE_SIZE)
    )

    # alien sprite
    # create a list of aliens
    aliens = []
    for alien_number in range(constants.TOTAL_NUMBER_OF_ALIENS):
        a_single_alien = stage.Sprite(
            image_bank_sprites, 9, constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y
        )
        # add to the list of aliens
        aliens.append(a_single_alien)

    # place 1 alien on the screen
    show_alien()

    # create a list of lasers for when we shoot
    lasers = []
    for laser_number in range(constants.TOTAL_NUMBER_OF_LASERS):
        # retrieving image #10
        a_single_laser = stage.Sprite(
            image_bank_sprites, 10, constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y
        )

        # add single laser to laser list
        lasers.append(a_single_laser)

    # variable game that is a display, with 60 hertz refresh
    game = stage.Stage(ugame.display, constants.FPS)
    # take images and add them to a list
    game.layers = [score_text] + lasers + [ship] + aliens + [background]
    game.render_block()

    # gaming loop
    while True:
        # get user input
        keys = ugame.buttons.get_pressed()

        # A button to fire
        # if this is true, a button has been pressed
        if keys & ugame.K_X != 0:
            if a_button == constants.button_state["button_up"]:
                a_button = constants.button_state["button_just_pressed"]
            elif a_button == constants.button_state["button_just_pressed"]:
                # make sure it does not repeat, if the button is pressed once and it is still held down
                a_button = constants.button_state["button_still_pressed"]
        else:
            if a_button == constants.button_state["button_still_pressed"]:
                a_button = constants.button_state["button_released"]
            else:
                a_button = constants.button_state["button_up"]
        if keys & ugame.K_O:
            pass
        if keys & ugame.K_START:
            pass
        if keys & ugame.K_SELECT:
            pass
        if keys & ugame.K_RIGHT:
            # if statement to check if its at the right side of the screen
            if ship.x <= constants.SCREEN_X - constants.SPRITE_SIZE:
                ship.move(ship.x + 3, ship.y)
            else:
                ship.move(0, ship.y)
        # If they press the left key
        if keys & ugame.K_LEFT:
            # if statement to check if its at the left side of the screen
            if ship.x >= 0:
                ship.move(ship.x - 3, ship.y)
            else:
                ship.move(constants.SCREEN_X - constants.SPRITE_SIZE, ship.y)
        # Can't leave it blank, replace it with pass
        if keys & ugame.K_UP:
            pass
        if keys & ugame.K_DOWN:
            pass

        # update game logic character moves
        # play sound if A was just button_just_pressed
        if a_button == constants.button_state["button_just_pressed"]:
            # fire a laser, if we have enough power (have not used up all the lasers)
            for laser_number in range(len(lasers)):
                if lasers[laser_number].x < 0:
                    lasers[laser_number].move(ship.x, ship.y)
                    sound.play(pew_sound)
                    break

        # each frame move the lasers, that have been fired up
        for laser_number in range(len(lasers)):
            if lasers[laser_number].x > 0:
                lasers[laser_number].move(
                    lasers[laser_number].x,
                    lasers[laser_number].y - constants.LASER_SPEED,
                )

                # check laser's y position
                if lasers[laser_number].y < constants.OFF_TOP_SCREEN:
                    lasers[laser_number].move(
                        constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y
                    )

                    show_alien()

        # each frame move the aliens down, that are on the screen
        for alien_number in range(len(aliens)):
            if aliens[alien_number].x > 0:
                aliens[alien_number].move(
                    aliens[alien_number].x,
                    aliens[alien_number].y + constants.ALIEN_SPEED,
                )

                if aliens[alien_number].y > constants.SCREEN_Y:
                    aliens[alien_number].move(
                        constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y
                    )

                    show_alien()
                    # subtract 1 for score each time an alien passes by without getting shot
                    score -= 1
                    if score < 0:
                        # if the score is already 0, don't subtract any
                        score = 0
                    score_text.clear()
                    score_text.cursor(0, 0)
                    score_text.move(1, 1)
                    score_text.text("Score: {0}".format(score))

        # each frame check if any of the lasers are touching any of the aliens
        for laser_number in range(len(lasers)):
            if lasers[laser_number].x > 0:
                # check all aliens that are on screen
                for alien_number in range(len(aliens)):
                    if aliens[alien_number].x > 0:
                        if stage.collide(
                            lasers[laser_number].x + 6,
                            lasers[laser_number].y + 2,
                            lasers[laser_number].x + 11,
                            lasers[laser_number].y + 12,
                            aliens[alien_number].x + 1,
                            aliens[alien_number].y,
                            aliens[alien_number].x + 15,
                            aliens[alien_number].y + 15,
                        ):

                            # if you hit an alien
                            # move alien off screen
                            aliens[alien_number].move(
                                constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y
                            )
                            lasers[laser_number].move(
                                constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y
                            )
                            sound.stop()
                            # make death sound fx
                            sound.play(boom_sound)
                            show_alien()
                            show_alien()
                            score = score + 1
                            score_text.clear()
                            score_text.cursor(0, 0)
                            score_text.move(1, 1)
                            score_text.text("Score: {0}".format(score))

        # each frame check if any aliens are touching the space ship
        for alien_number in range(len(aliens)):
            if aliens[alien_number].x > 0:
                if stage.collide(
                    aliens[alien_number].x + 1,
                    aliens[alien_number].y,
                    aliens[alien_number].x + 15,
                    aliens[alien_number].y + 15,
                    ship.x,
                    ship.y,
                    ship.x + 15,
                    ship.y + 15,
                ):
                    # alien hit the ship
                    sound.stop()
                    sound.play(crash_sound)
                    time.sleep(3.0)
                    game_over_scene(score)

        # redraw sprite/ship/alien not background
        game.render_sprites(lasers + [ship] + aliens)
        game.tick()  # wait until refresh rate finishes


def game_over_scene(final_score):
    # this function is the game over scene

    # image banks for CircuitPython
    image_bank_2 = stage.Bank.from_bmp16("mt_game_studio.bmp")

    # sets the background to image 0 in the image bank
    background = stage.Grid(
        image_bank_2, constants.SCREEN_GRID_X, constants.SCREEN_GRID_Y
    )

    # add text objects
    # text for scoreboard
    text = []
    text1 = stage.Text(
        width=29, height=14, font=None, palette=constants.RED_PALETTE, buffer=None
    )
    text1.move(22, 20)
    text1.text("Final Score: {:0>2d}".format(final_score))
    text.append(text1)

    text2 = stage.Text(
        width=29, height=14, font=None, palette=constants.RED_PALETTE, buffer=None
    )
    text2.move(43, 60)
    text2.text("GAME OVER")
    text.append(text2)

    text3 = stage.Text(
        width=29, height=14, font=None, palette=constants.RED_PALETTE, buffer=None
    )
    text3.move(32, 110)
    text3.text("PRESS SELECT")
    text.append(text3)

    # create a stage for the background to show up on
    # and set the frame rate to 60 fps
    game = stage.Stage(ugame.display, constants.FPS)
    # set the layers, items show up in order
    game.layers = text + [background]
    # render the background and initial location of sprite list
    # most likely you will only render background once per scene
    game.render_block()

    # repeat forever, game loop
    # get user's button selection
    while True:
        # get user input
        keys = ugame.buttons.get_pressed()

        # start button selected
        if keys & ugame.K_SELECT != 0:
            supervisor.reload()

        # update game logic
        game.tick()  # wait until refresh rate finishes


if __name__ == "__main__":
    # make sure to have the scene the FIRST scene you want to display
    splash_scene()
