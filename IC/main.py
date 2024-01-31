# Thanks for using this PianoPad, made with ♥ by Evan Liu
# Ivy this is for you
# This main.py contain most basic macropad functionalities, if you want to get familarize with all the features please make a back up of main.py and modify according to the official doc:
# http://kmkfw.io/docs/Getting_Started/

# This is from CircuitPython, foundation of KMK
import board

# This is standard GPIO mapping for all matrix-like boards
from kb import PianoKB

# Key Code are in this builtin class
# http://kmkfw.io/docs/keycodes
from kmk.keys import KC

# Add Media key support
# http://kmkfw.io/docs/media_keys
from kmk.extensions.media_keys import MediaKeys

# Macro
# http://kmkfw.io/docs/sequences
from kmk.handlers.sequences import simple_key_sequence

# Rotary Encoder EC11 (Knob)
# http://kmkfw.io/docs/encoder
from kmk.modules.encoder import EncoderHandler
# Initialize Encoder class
encoder_handler = EncoderHandler()

# Hold modifier with timeout (eg. Hold alt, and switch to Layer one for knob clicking tab tab tab)
# Use KC.HM(Modifier) to place a modifier on hold until timeout
from kmk.modules.holdmod import HoldMod
# Holding Mod key while do something else
hold_mod = HoldMod()
hold_mod.tap_time = 5000

# Initialize Keyboard class
keyboard = PianoKB()

# Enable modules
keyboard.modules = [encoder_handler, hold_mod, MediaKeys()]

COPY = simple_key_sequence(
    (
        KC.LGUI(no_release=True),
        KC.C
    )
)

PASTE = simple_key_sequence(
    (
        KC.LGUI(no_release=True),
        KC.V
    )
)

DESKTOP = simple_key_sequence(
    (
        KC.LGUI(no_release=True),
        KC.D
    )
)

SCREENSHOT = simple_key_sequence(
    (
        KC.LSFT(no_release=True),
        KC.LGUI(no_release=True),
        KC.N3
    )
)

# Your keymap
keyboard.keymap = [
    [COPY, PASTE, SCREENSHOT, DESKTOP, KC.MEDIA_PREV_TRACK, KC.MEDIA_NEXT_TRACK, KC.MUTE, KC.VOLD, KC.VOLU], # Layer 1
    [KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.LSFT(KC.TAB), KC.TAB] # Layer 2
]

if __name__ == '__main__':
    # keyboard.debug_enabled = True
    keyboard.go()
