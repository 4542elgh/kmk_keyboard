# IMPORTANT: This kb.py file was created by Evan Liu and should not be modified.
# Last Modified on 2023-10-13
# This file contain GPIO pin mapping and does not contain any user defined macro/key binding.
# This file should be "set it then forget it", mess this file up and your board will not work anymore
# If you did mess this up, and dont have a backup, either contact Evan Liu or go to his blog to read up on how to rescure your board

# This is from CircuitPython, interacting with GPIO pins, also foundation of KMK
import board

# Import KMKKeyboard Base class, we will be extending this class
from kmk.kmk_keyboard import KMKKeyboard

# Scanners can accept customize pin and incorporate into custom layout
from kmk.scanners.keypad import KeysScanner
from kmk.scanners.encoder import RotaryioEncoder

# __  ______  __  __   _____ __  ______  __  ____    ____     _   ______  ______   __________  __  __________  __   ________  ___________    ____________    ______
# \ \/ / __ \/ / / /  / ___// / / / __ \/ / / / /   / __ \   / | / / __ \/_  __/  /_  __/ __ \/ / / / ____/ / / /  /_  __/ / / /  _/ ___/   / ____/  _/ /   / ____/
#  \  / / / / / / /   \__ \/ /_/ / / / / / / / /   / / / /  /  |/ / / / / / /      / / / / / / / / / /   / /_/ /    / / / /_/ // / \__ \   / /_   / // /   / __/
#  / / /_/ / /_/ /   ___/ / __  / /_/ / /_/ / /___/ /_/ /  / /|  / /_/ / / /      / / / /_/ / /_/ / /___/ __  /    / / / __  // / ___/ /  / __/ _/ // /___/ /___
# /_/\____/\____/__ /____/_/ /_/\____/\____/_____/_____/  /_/ |_/\____/ /_/      /_/  \____/\____/\____/_/ /_/    /_/ /_/ /_/___//____/  /_/   /___/_____/_____/      _
#   __  ______  / /__  __________   __  ______  __  __   / /______  ____ _      __   _      __/ /_  ____ _/ /_   __  ______  __  __   ____ _________     ____/ /___  (_)___  ____ _
#  / / / / __ \/ / _ \/ ___/ ___/  / / / / __ \/ / / /  / //_/ __ \/ __ \ | /| / /  | | /| / / __ \/ __ `/ __/  / / / / __ \/ / / /  / __ `/ ___/ _ \   / __  / __ \/ / __ \/ __ `/
# / /_/ / / / / /  __(__  |__  )  / /_/ / /_/ / /_/ /  / ,< / / / / /_/ / |/ |/ /   | |/ |/ / / / / /_/ / /_   / /_/ / /_/ / /_/ /  / /_/ / /  /  __/  / /_/ / /_/ / / / / / /_/ /
# \__,_/_/ /_/_/\___/____/____/   \__, /\____/\__,_/  /_/|_/_/ /_/\____/|__/|__/    |__/|__/_/ /_/\__,_/\__/   \__, /\____/\__,_/   \__,_/_/   \___/   \__,_/\____/_/_/ /_/\__, /
#                                /____/                                                                       /____/                                                      /____/

# https://wiki.seeedstudio.com/XIAO-RP2040/
#                ___
#         ------|   |------
# KEY0/D0 |               | 5V
# KEY1/D1 |               | GND
# KEY2/D2 |     XIAO      | 3V3
# KEY3/D3 |    RP2040     | RSW2/D10
# KEY4/D4 |               | RSW1/D9
# KEY5/D5 |               | D8
# KEY6/D6 |               | D7
#         -----------------

# GPIO to key mapping - each line is a new row. Piano is single row macro board
# GPIO can be seen by issuing this command in MU Editor's REPL:
    # import board
    # dir(board)

_KEY_CFG = [
    board.D0,  board.D1,  board.D2, board.D3, board.D4, board.D5, board.D6
]

# Building custom scanners for direct GPIO
# https://github.com/KMKfw/kmk_firmware/blob/master/docs/en/scanners.md

# Keyboard implementation class, inherit from KMKKeyboard base class
class PianoKB(KMKKeyboard):
    def __init__(self):
        # create and register the scanner
        self.matrix = [
            # Direct IO pin
            # https://github.com/KMKfw/kmk_firmware/blob/master/docs/en/scanners.md#keypad-keysscanner
            KeysScanner(
                # require argument:
                pins=_KEY_CFG,
                # optional arguments with defaults:
                # value_when_pressed=False,
                # pull=True,
                # interval=0.02,  # Debounce time in floating point seconds
                # max_events=64
            ),
            # Rotary encoder
            # https://github.com/KMKfw/kmk_firmware/blob/master/docs/en/scanners.md#rotaryioencoder
            RotaryioEncoder(
                pin_a=board.D10,
                pin_b=board.D9,
                # optional
                # divisor=4,
            )
        ]
        # Coordinate mapping for all the possible keys, this is a single row for Piano board, 0-5 are MX switch keys, 6 is rotary click button, 7, 8 are rotary encoder, for CCW CW rotation respectively
        # Notice that all of the encoders are at the end of the array, because we put the encoder scanner after the matrix scanner in keyboard.matrix https://github.com/KMKfw/kmk_firmware/blob/master/docs/en/scanners.md#rotaryioencoder
        coord_mapping = [0, 1, 2, 3, 4, 5, 6, 7, 8]
