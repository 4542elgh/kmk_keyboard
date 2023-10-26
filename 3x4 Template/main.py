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
encoder_handler = EncoderHandler()
encoder_handler.pins = (
    # regular direction encoder and a button
    (board.D9, board.D8, None,), # encoder #1 GPIO
)

# Initialize standard GPIO mapping
keyboard = KMKKeyboard()

keyboard.col_pins = (board.D3, board.D2, board.D1, board.D0)
keyboard.row_pins = (board.D10, board.D6, board.D5, board.D4)

# I dont know what this means but use this value
keyboard.diode_orientation = DiodeOrientation.COL2ROW

# keyboard.modules = [MediaKeys(), Layers(), encoder_handler, hold_mod, statusLED, combos]
keyboard.modules = [MediaKeys(), encoder_handler, statusLED]

encoder_handler.map = [(
    (KC.AUDIO_VOL_DOWN, KC.AUDIO_VOL_UP),
)]

keyboard.keymap = [
    # CounterClockWise, ClockWise, Press (Press is set to None because we will define Press in Matrix)
    [
        KC.NO, KC.MEDIA_PREV_TRACK, KC.MEDIA_NEXT_TRACK, KC.MUTE,
        KC.N9, KC.N0, KC.NO, KC.NO,
        KC.N5, KC.N6, KC.N7, KC.N8,
        KC.N1, KC.N2, KC.N3, KC.N4,
    ], # Layer 1
]

if __name__ == '__main__':
    # Debug mode
    # keyboard.debug_enabled = True
    keyboard.go()
