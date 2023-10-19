# Thanks for using this MacroPad
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
# from kmk.handlers.sequences import unicode_string_sequence

# Rotary Encoder EC11 (Knob)
# http://kmkfw.io/docs/encoder
from kmk.modules.encoder import EncoderHandler

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
    (board.D9, board.D8, None,), # Encoder #1 GPIO PINS
)
encoder_handler.map = [((KC.AUDIO_VOL_DOWN, KC.AUDIO_VOL_UP))] # Layer 1

# Enable modules 
keyboard.modules = [encoder_handler, MediaKeys()]

COPY = simple_key_sequence(
    (
        KC.LCTL(no_release=True),
        KC.C
    )
)

CUT = simple_key_sequence(
    (
        KC.LCTL(no_release=True),
        KC.X
    )
)

PASTE = simple_key_sequence(
    (
        KC.LCTL(no_release=True),
        KC.V
    )
)

SELECT_ALL = simple_key_sequence(
    (
        KC.LCTL(no_release=True),
        KC.A
    )
)

STEAM = simple_key_sequence(
    (
        KC.LGUI,
        KC.MACRO_SLEEP_MS(1000),
        KC.S,
        KC.T,
        KC.E,
        KC.A,
        KC.M,
        KC.MACRO_SLEEP_MS(500),
        KC.ENT
    )
)

SETTING = simple_key_sequence(
    (
        KC.LGUI(no_release=True),
        KC.I
    )
)

DESKTOP = simple_key_sequence(
    (
        KC.LGUI(no_release=True),
        KC.D
    )
)

CHROME = simple_key_sequence(
    (
        KC.LGUI,
        KC.MACRO_SLEEP_MS(1000),
        KC.C,
        KC.H,
        KC.R,
        KC.O,
        KC.M,
        KC.E,
        KC.MACRO_SLEEP_MS(500),
        KC.ENT
    )
)

YOUTUBE = simple_key_sequence(
    (
        KC.LGUI,
        KC.MACRO_SLEEP_MS(1000),
        KC.C,
        KC.H,
        KC.R,
        KC.O,
        KC.M,
        KC.E,
        KC.MACRO_SLEEP_MS(500),
        KC.ENT,
        KC.MACRO_SLEEP_MS(500),
        KC.H,
        KC.T,
        KC.T,
        KC.P,
        KC.S,
        KC.COLN,
        KC.SLASH,
        KC.SLASH,
        KC.Y,
        KC.O,
        KC.U,
        KC.T,
        KC.U,
        KC.B,
        KC.E,
        KC.DOT,
        KC.C,
        KC.O,
        KC.M,
        KC.ENT,
    )
)

TASK_MANAGER = simple_key_sequence(
    (
        KC.LCTL(no_release=True),
        KC.LSFT(no_release=True),
        KC.ESC
    )
)

# Your keymap
keyboard.keymap = [
    [
        KC.NO, KC.MEDIA_PREV_TRACK, KC.MEDIA_NEXT_TRACK, KC.MUTE,
        COPY, CUT, PASTE, KC.MEDIA_PLAY_PAUSE,
        SELECT_ALL, STEAM, YOUTUBE, SETTING,
        DESKTOP, CHROME, TASK_MANAGER, KC.F5
    ], # Layer 1
]

if __name__ == '__main__':
    keyboard.go()
