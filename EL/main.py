# Thanks for using this MacroPad
# This main.py contain most basic macropad functionalities, if you want to get familarize with all the features please make a back up of main.py and modify according to the official doc:
# http://kmkfw.io/docs/Getting_Started/

# This is from CircuitPython, interacting with GPIO pins, also foundation of KMK
import board

# This is standard GPIO mapping for all matrix-like boards
from kmk.kmk_keyboard import KMKKeyboard

# Key Code are in this builtin class
from kmk.keys import KC
# Add Media key support
# http://kmkfw.io/docs/media_keys
from kmk.extensions.media_keys import MediaKeys

# Macro
from kmk.handlers.sequences import simple_key_sequence

# Define diode orientation, we can leave vaule as default
from kmk.scanners import DiodeOrientation

# Turn NeoPixel LED into Layer indicator
from kmk.extensions.statusled_neopixel import statusLED
statusLED = statusLED(
    breath_mode=True,
    colors=(
    (255, 0, 0),
    (0, 255, 0),
    (0, 0, 255))
)

# Rotary Encoder EC11 (Knob)
from kmk.modules.encoder import EncoderHandler

from kmk.modules.layers import Layers

from kmk.modules.holdmod import HoldMod
hold_mod = HoldMod()
hold_mod.tap_time = 5000

# Add combo support
from kmk.modules.combos import Combos, Chord
combos = Combos()

# Initialize standard GPIO mapping
keyboard = KMKKeyboard()

keyboard.col_pins = (board.D3, board.D2, board.D1, board.D0)
keyboard.row_pins = (board.D10, board.D6, board.D5, board.D4)

# I dont know what this means but use this value
keyboard.diode_orientation = DiodeOrientation.COL2ROW

# Regular GPIO Encoder
encoder_handler = EncoderHandler()
encoder_handler.pins = (
    # regular direction encoder and a button
    (board.D9, board.D8, None,), # encoder #1 GPIO
)

# keyboard.modules = [MediaKeys(), Layers(), encoder_handler, hold_mod, statusLED, combos]
keyboard.modules = [MediaKeys(), Layers(), encoder_handler, hold_mod, statusLED, combos]

combos.combos = [
    Chord((1, 2), KC.HM(KC.LALT), match_coord=True),
]

encoder_handler.map = [(
    (KC.AUDIO_VOL_DOWN, KC.AUDIO_VOL_UP),
)
, (
    (KC.LSFT(KC.TAB), KC.TAB),
)
]

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

ALT_TAB = simple_key_sequence(
    (
        KC.LALT(no_release=True),
        KC.MACRO_SLEEP_MS(30),
        KC.TAB,
        KC.MACRO_SLEEP_MS(30),
        KC.LALT(no_press=True),
    )
)

keyboard.keymap = [
    # CounterClockWise, ClockWise, Press (Press is set to None because we will define Press in Matrix)
    [
        KC.NO, KC.MEDIA_PREV_TRACK, KC.MEDIA_NEXT_TRACK, KC.MUTE,
        COPY, CUT, PASTE, KC.MEDIA_PLAY_PAUSE,
        SELECT_ALL, STEAM, YOUTUBE, SETTING,
        DESKTOP, CHROME, TASK_MANAGER, KC.HM(KC.LALT)
    ], # Layer 1
]

if __name__ == '__main__':
    keyboard.debug_enabled = True
    keyboard.go()
