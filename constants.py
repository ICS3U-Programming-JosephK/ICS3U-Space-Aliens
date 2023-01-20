#!/usr/bin/env python3
# Created by: Joseph Kwon
# Created on: Jan 09, 2022
# Constants for space alien game

# Screen size is 160 x 128
SCREEN_X = 160
SCREEN_Y = 128

SCREEN_GRID_X = 10
SCREEN_GRID_Y = 8

# Sprites are 16 x 16
SPRITE_SIZE = 16

SHIP_SPEED = 1
ALIEN_SPEED = 1
LASER_SPEED = 1

TOTAL_NUMBER_OF_ALIENS = 5
TOTAL_NUMBER_OF_LASERS = 5

OFF_SCREEN_X = -100
OFF_SCREEN_Y = -100
OFF_TOP_SCREEN = -1 * SPRITE_SIZE

OFF_BOTTOM_SCREEN = SCREEN_Y + SPRITE_SIZE

FPS = 60
SPRITE_MOVEMENT_SPEED = 1

# States of the Button
button_state = {
    "button_up": "up",
    "button_just_pressed": "just pressed",
    "button_still_pressed": "still pressed",
    "button_released": "released",
}

# New palette for filled Text
RED_PALETTE = (
    b"\xff\xff\x00\x22\xcey\x22\xff\xff\xff\xff\xff\xff\xff\xff\xff"
    b"\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff"
)

# Same as the palette above but in blue
BLUE_PALETTE = (
    b"\xf8\x1f\x00\x00\xcey\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff"
    b"\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff"
)
