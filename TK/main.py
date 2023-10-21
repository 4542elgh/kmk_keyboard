# Thanks for using this PianoPad, made with ♥ by Evan Liu
# This main.py contain most basic macropad functionalities, if you want to get familarize with all the features please make a back up of main.py and modify according to the official doc:
# http://kmkfw.io/docs/Getting_Started/

# This is from CircuitPython, foundation of KMK
import board

# This is standard GPIO mapping for all matrix-like boards
from kmk.kmk_keyboard import KMKKeyboard

# Define diode orientation, we can leave vaule as default
from kmk.scanners import DiodeOrientation

# Key Code are in this builtin class
# http://kmkfw.io/docs/keycodes
from kmk.keys import KC

# Add Media key support
# http://kmkfw.io/docs/media_keys
from kmk.extensions.media_keys import MediaKeys

# Macro
# http://kmkfw.io/docs/sequences
from kmk.handlers.sequences import simple_key_sequence

# Unicode support
# http://kmkfw.io/docs/sequences#unicode
from kmk.handlers.sequences import unicode_string_sequence

# Rotary Encoder EC11 (Knob)
# http://kmkfw.io/docs/encoder
from kmk.modules.encoder import EncoderHandler

# Hold modifier with timeout (eg. Hold alt, and switch to Layer one for knob clicking tab tab tab)
# Use KC.HM(Modifier) to place a modifier on hold until timeout
from kmk.modules.holdmod import HoldMod

# Initialize Keyboard class
keyboard = KMKKeyboard()
# I dont know what this means but use this value
keyboard.diode_orientation = DiodeOrientation.COL2ROW
# Define GPIO mapping
keyboard.col_pins = (board.D3, board.D2, board.D1, board.D0)
keyboard.row_pins = (board.D10, board.D6, board.D5, board.D4)

# Initialize Encoder class
encoder_handler = EncoderHandler()
encoder_handler.pins = (
    # EC11 encoder, button click is omitted (part of the keymap matrix)
    (board.D9, board.D8, None,), # encoder #1 GPIO PINS
)
encoder_handler.map = [((KC.AUDIO_VOL_DOWN, KC.AUDIO_VOL_UP)), # Layer 1
                       ((KC.LSFT(KC.TAB), KC.TAB))] # Layer 2

# Holding Mod key while do something else
hold_mod = HoldMod()
hold_mod.tap_time = 5000

# Enable modules 
keyboard.modules = [encoder_handler, hold_mod, MediaKeys()]

COPY = simple_key_sequence(
    (
        KC.LCTL(no_release=True),
        KC.C
    )
)

PASTE = simple_key_sequence(
    (
        KC.LCTL(no_release=True),
        KC.V
    )
)

EGG_PLANT = unicode_string_sequence('🍆')

DESKTOP = simple_key_sequence(
    (
        KC.LGUI(no_release=True),
        KC.D
    )
)

# Your keymap
keyboard.keymap = [
    [COPY, PASTE, EGG_PLANT, KC.HM(KC.LALT), KC.HOME, DESKTOP], # Layer 1
]

if __name__ == '__main__':
    keyboard.go()
