# Thanks for using this MacroPad
# This main.py contain most basic macropad functionalities, if you want to get familarize with all the features please make a back up of main.py and modify according to the official doc:
# http://kmkfw.io/docs/Getting_Started/
# My blog have some extra explanation on some features
# https://obsidian.evanmingliu.com/Projects/Keyboard/KMK/kmk_setup

# This is from CircuitPython, interacting with GPIO pins, also foundation of KMK
import board

# This is standard GPIO mapping for all matrix-like boards
from kmk.kmk_keyboard import KMKKeyboard

# Key Code are in this builtin class
# http://kmkfw.io/docs/keycodes
from kmk.keys import KC

# Add Media key support
# http://kmkfw.io/docs/media_keys
from kmk.extensions.media_keys import MediaKeys

# Define diode orientation, we can leave vaule as default
from kmk.scanners import DiodeOrientation

# This is an extension from CircuitPython, Disable LED light
# https://learn.adafruit.com/circuitpython-essentials/circuitpython-internal-rgb-led
from kmk.extensions.statusled_neopixel import statusLED
led = statusLED()
led.breath_mode = True # Breathing LED
# led.breath_mode = False # Disable LED
led.colors = [
    (255, 0, 0),
    (0, 255, 0),
    (0, 0, 255)
]

# Rotary Encoder EC11 (Knob)
# http://kmkfw.io/docs/encoder
from kmk.modules.encoder import EncoderHandler
encoder_handler = EncoderHandler()
encoder_handler.pins = (
    (board.D9, board.D10, None),
) # encoder #1 GPIO

# Instantiate a KMKKeyboard class
keyboard = KMKKeyboard()
keyboard.modules = [led, encoder_handler, MediaKeys()]

# https://wiki.seeedstudio.com/XIAO-RP2040/
#                ___
#         ------|   |------
# COL2/D0 |               | 5V
# COL1/D1 |               | GND
# COL0/D2 |     XIAO      | 3V3
# ROW3/D3 |    RP2040     | RSW2/D10
# ROW2/D4 |               | RSW1/D9
# ROW1/D5 |               | D8
# ROW0/D6 |               | D7
#         -----------------

# I dont know what this means but use this value
keyboard.diode_orientation = DiodeOrientation.COL2ROW

# Define Row and Column pins
keyboard.col_pins = (board.D2, board.D1, board.D0)
keyboard.row_pins = (board.D6, board.D5, board.D4, board.D3)

# Media KC need to be defined AFTER MediaKeys() is in keyboard.modules
encoder_handler.map = [(
    (KC.AUDIO_VOL_DOWN, KC.AUDIO_VOL_UP, None),
)] # Layer 1

# Your Keymaps, a new list is a new layer
keyboard.keymap = [
    (KC.NO, KC.N0, KC.MUTE,
    KC.N7, KC.N8, KC.N9,
    KC.N4, KC.N5, KC.N6,
    KC.N1, KC.N2, KC.N3)
]

if __name__ == '__main__':
    # Debug mode
    # keyboard.debug_enabled = True
    keyboard.go()