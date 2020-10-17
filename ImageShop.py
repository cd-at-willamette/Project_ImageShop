# File: ImageShop.py

"""
This program is the starter file for the ImageShop application, which
implements the "Load" and "Flip Vertical" buttons.
"""

from filechooser import choose_input_file
from pgl import GWindow, GImage, GRect, GState
from button import GButton

# Constants

GWINDOW_WIDTH = 900
GWINDOW_HEIGHT = 500
BUTTON_WIDTH = 125
BUTTON_HEIGHT = 20
BUTTON_MARGIN = 10
BUTTON_BACKGROUND = "#CCCCCC"

# Derived constants

BUTTON_AREA_WIDTH = 2 * BUTTON_MARGIN + BUTTON_WIDTH
IMAGE_AREA_WIDTH = GWINDOW_WIDTH - BUTTON_AREA_WIDTH

# The image_shop application

def image_shop():
    def add_button(label, action):
        """
        Adds a button to the region on the left side of the window
        """
        x = BUTTON_MARGIN
        y = gs.next_button_y
        button = GButton(label, action)
        button.set_size(BUTTON_WIDTH, BUTTON_HEIGHT)
        gw.add(button, x, y)
        gs.next_button_y += BUTTON_HEIGHT + BUTTON_MARGIN

    def set_image(image):
        """
        Sets image as the current image after removing the old one.
        """
        if gs.current_image is not None:
            gw.remove(gs.current_image)
        gs.current_image = image
        x = BUTTON_AREA_WIDTH + (IMAGE_AREA_WIDTH - image.get_width()) / 2
        y = (gw.get_height() - image.get_height()) / 2
        gw.add(image, x, y)

    def load_button_action():
        """Callback function for the Load button"""
        filename = choose_input_file()
        if filename != "":
            set_image(GImage(filename))

    def flip_vertical_action():
        """Callback function for the Flip Vertical button"""
        if gs.current_image is not None:
            set_image(flip_vertical(gs.current_image))
        
    gw = GWindow(GWINDOW_WIDTH, GWINDOW_HEIGHT)
    gs = GState()
    button_area = GRect(0, 0, BUTTON_AREA_WIDTH, GWINDOW_HEIGHT)    
    button_area.set_filled(True)
    button_area.set_color(BUTTON_BACKGROUND)
    gw.add(button_area)
    gs.next_button_y = BUTTON_MARGIN
    gs.current_image = None
    add_button("Load", load_button_action)
    add_button("Flip Vertical", flip_vertical_action)

# Creates a new GImage from the original one by flipping it vertically.

def flip_vertical(image):
    array = image.get_pixel_array()
    return GImage(array[::-1])

# Startup code

if __name__ == "__main__":
    image_shop()
