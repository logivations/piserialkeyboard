# The MIT License (MIT)
#
# Copyright (c) 2017 Dan Halbert
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
#

"""
`adafruit_hid.keyboard_layout_us.KeyboardLayoutUS`
=======================================================

* Author(s): Dan Halbert
"""

#from adafruit_hid.keycode import Keycode

class KeyboardLayoutDE:
    """Map ASCII characters to appropriate keypresses on a standard US PC keyboard.

    Non-ASCII characters and most control characters will raise an exception.
    """

    # The ASCII_TO_KEYCODE bytes object is used as a table to maps ASCII 0-127
    # to the corresponding # keycode on a US 104-key keyboard.
    # The user should not normally need to use this table,
    # but it is not marked as private.
    #
    # Because the table only goes to 127, we use the top bit of each byte (ox80) to indicate
    # that the shift key should be pressed. So any values 0x{8,9,a,b}* are shifted characters.
    #
    # The Python compiler will concatenate all these bytes literals into a single bytes object.
    # Micropython/CircuitPython will store the resulting bytes constant in flash memory
    # if it's in a .mpy file, so it doesn't use up valuable RAM.
    #
    # \x00 entries have no keyboard key and so won't be sent.
    '''
    NONE          =byte((0));
    CONTROL_LEFT  =byte((1<<0));
    SHIFT_LEFT    =byte((1<<1));
    ALT_LEFT      =byte((1<<2));
    GUI_LEFT      =byte((1<<3));
    CONTROL_RIGHT =byte((1<<4));
    SHIFT_RIGHT   =byte((1<<5));
    ALT_RIGHT     =byte((1<<6));
    GUI_RIGHT     =byte((1<<7));
    '''
    SHIFT_FLAG = 0x80
    CONTROL_LEFT  =0x1
    SHIFT_LEFT    =0x2
    ALT_LEFT      =0x4
    GUI_LEFT      =0x8
    CONTROL_RIGHT =0x10
    SHIFT_RIGHT   =0x20
    ALT_RIGHT     =0x40
    GUI_RIGHT     =0x80
    ALT_Gr        =0x50

    ASCII_TO_KEYCODE = (
        b'\x00'  # NUL
        b'\x00'  # SOH
        b'\x00'  # STX
        b'\x00'  # ETX
        b'\x00'  # EOT
        b'\x00'  # ENQ
        b'\x00'  # ACK
        b'\x00'  # BEL \a
        b'\x2a'  # BS BACKSPACE \b (called DELETE in the usb.org document)
        b'\x2b'  # TAB \t
        b'\x28'  # LF \n (called Return or ENTER in the usb.org document)
        b'\x00'  # VT \v
        b'\x00'  # FF \f
        b'\x28'  # CR \r
        b'\x00'  # SO
        b'\x00'  # SI
        b'\x00'  # DLE
        b'\x00'  # DC1
        b'\x00'  # DC2
        b'\x00'  # DC3
        b'\x00'  # DC4
        b'\x00'  # NAK
        b'\x00'  # SYN
        b'\x00'  # ETB
        b'\x00'  # CAN
        b'\x00'  # EM
        b'\x00'  # SUB
        b'\x29'  # ESC
        b'\x00'  # FS
        b'\x00'  # GS
        b'\x00'  # RS
        b'\x00'  # US
        b'\x2c'  # SPACE
        b'\x1e'  # ! x1e|SHIFT_FLAG (shift 1)
        b'\x1F'  # " x34|SHIFT_FLAG (shift ')
        b'\x31'  # # x20|SHIFT_FLAG (shift 3)
        b'\x21'  # $ x21|SHIFT_FLAG (shift 4)
        b'\x22'  # % x22|SHIFT_FLAG (shift 5)
        b'\x23'  # & x24|SHIFT_FLAG (shift 7)
        b'\x31'  # '
        b'\x25'  # ( x26|SHIFT_FLAG (shift 9)
        b'\x26'  # ) x27|SHIFT_FLAG (shift 0)
        b'\x30'  # * x25|SHIFT_FLAG (shift 8)
        b'\x30'  # + x2e|SHIFT_FLAG (shift =)
        b'\x36'  # ,
        b'\x38'  # -
        b'\x37'  # .
        b'\x24'  # /
        b'\x27'  # 0
        b'\x1e'  # 1
        b'\x1f'  # 2
        b'\x20'  # 3
        b'\x21'  # 4
        b'\x22'  # 5
        b'\x23'  # 6
        b'\x24'  # 7
        b'\x25'  # 8
        b'\x26'  # 9
        b'\x37'  # : x33|SHIFT_FLAG (shift ;)
        b'\x36'  # ;
        b'\x64'  # < x36|SHIFT_FLAG (shift ,)
        b'\x27'  # =
        b'\x64'  # > x37|SHIFT_FLAG (shift .)
        b'\x2d'  # ? x38|SHIFT_FLAG (shift /)
        b'\x14'  # @ x1f|SHIFT_FLAG (shift 2)
        b'\x04'  # A x04|SHIFT_FLAG (shift a)
        b'\x05'  # B x05|SHIFT_FLAG (etc.)
        b'\x06'  # C x06|SHIFT_FLAG
        b'\x07'  # D x07|SHIFT_FLAG
        b'\x08'  # E x08|SHIFT_FLAG
        b'\x09'  # F x09|SHIFT_FLAG
        b'\x0a'  # G x0a|SHIFT_FLAG
        b'\x0b'  # H x0b|SHIFT_FLAG
        b'\x0c'  # I x0c|SHIFT_FLAG
        b'\x0d'  # J x0d|SHIFT_FLAG
        b'\x0e'  # K x0e|SHIFT_FLAG
        b'\x0f'  # L x0f|SHIFT_FLAG
        b'\x10'  # M x10|SHIFT_FLAG
        b'\x11'  # N x11|SHIFT_FLAG
        b'\x12'  # O x12|SHIFT_FLAG
        b'\x13'  # P x13|SHIFT_FLAG
        b'\x14'  # Q x14|SHIFT_FLAG
        b'\x15'  # R x15|SHIFT_FLAG
        b'\x16'  # S x16|SHIFT_FLAG
        b'\x17'  # T x17|SHIFT_FLAG
        b'\x18'  # U x18|SHIFT_FLAG
        b'\x19'  # V x19|SHIFT_FLAG
        b'\x1a'  # W x1a|SHIFT_FLAG
        b'\x1b'  # X x1b|SHIFT_FLAG
        b'\x1d'  # Y x1c|SHIFT_FLAG
        b'\x1c'  # Z x1d|SHIFT_FLAG
        b'\x25'  # [
        b'\x2d'  # \ backslash
        b'\x26'  # ]
        b'\x35'  # ^ x23|SHIFT_FLAG (shift 6)
        b'\x38'  # _ x2d|SHIFT_FLAG (shift -)
        b'\x2e'  # `
        b'\x04'  # a
        b'\x05'  # b
        b'\x06'  # c
        b'\x07'  # d
        b'\x08'  # e
        b'\x09'  # f
        b'\x0a'  # g
        b'\x0b'  # h
        b'\x0c'  # i
        b'\x0d'  # j
        b'\x0e'  # k
        b'\x0f'  # l
        b'\x10'  # m
        b'\x11'  # n
        b'\x12'  # o
        b'\x13'  # p
        b'\x14'  # q
        b'\x15'  # r
        b'\x16'  # s
        b'\x17'  # t
        b'\x18'  # u
        b'\x19'  # v
        b'\x1a'  # w
        b'\x1b'  # x
        b'\x1d'  # y
        b'\x1c'  # z
        b'\x24'  # { x2f|SHIFT_FLAG (shift [)
        b'\x64'  # | x31|SHIFT_FLAG (shift \)
        b'\x27'  # } x30|SHIFT_FLAG (shift ])
        b'\x30'  # ~ x35|SHIFT_FLAG (shift `)
        b'\x4c'  # DEL DELETE (called Forward Delete in usb.org document)
        b'\x00'  # 128
        b'\x00'  # 129
        b'\x00'  # 130
        b'\x00'  # 131
        b'\x00'  # 132
        b'\x00'  # 133
        b'\x00'  # 134
        b'\x00'  # 135
        b'\x00'  # 136
        b'\x00'  # 137
        b'\x00'  # 138
        b'\x00'  # 139
        b'\x00'  # 140
        b'\x00'  # 141
        b'\x00'  # 142
        b'\x00'  # 143
        b'\x00'  # 144
        b'\x00'  # 145
        b'\x00'  # 146
        b'\x00'  # 147
        b'\x00'  # 148
        b'\x00'  # 149
        b'\x00'  # 150
        b'\x00'  # 151
        b'\x00'  # 152
        b'\x00'  # 153
        b'\x00'  # 154
        b'\x00'  # 155
        b'\x00'  # 156
        b'\x00'  # 157
        b'\x00'  # 158
        b'\x00'  # 159
        b'\x00'  # 160
        b'\x00'  # 161
        b'\x00'  # 162
        b'\x00'  # 163
        b'\x00'  # 164
        b'\x00'  # 165
        b'\x00'  # 166
        b'\x00'  # 167
        b'\x00'  # 168
        b'\x00'  # 169
        b'\x00'  # 170
        b'\x00'  # 171
        b'\x00'  # 172
        b'\x00'  # 173
        b'\x00'  # 174
        b'\x00'  # 175
        b'\x00'  # 176
        b'\x00'  # 177
        b'\x00'  # 178
        b'\x00'  # 179
        b'\x00'  # 180
        b'\x00'  # 181
        b'\x00'  # 182
        b'\x00'  # 183
        b'\x00'  # 184
        b'\x00'  # 185
        b'\x00'  # 186
        b'\x00'  # 187
        b'\x2e'  # 188 ´
        b'\x00'  # 189
        b'\x00'  # 190
        b'\x00'  # 191
        b'\x00'  # 192
        b'\x00'  # 193
        b'\x00'  # 194
        b'\x00'  # 195
        b'\xc4'  # 196 Ä
        b'\x00'  # 197
        b'\x00'  # 198
        b'\x00'  # 199
        b'\x00'  # 200
        b'\x00'  # 201
        b'\x00'  # 202
        b'\x00'  # 203
        b'\x00'  # 204
        b'\x00'  # 205
        b'\x00'  # 206
        b'\x00'  # 207
        b'\x00'  # 208
        b'\x00'  # 209
        b'\x00'  # 210
        b'\x00'  # 211
        b'\x00'  # 212
        b'\x00'  # 213
        b'\x33'  # 214 Ö
        b'\x00'  # 215
        b'\x00'  # 216
        b'\x00'  # 217
        b'\x00'  # 218
        b'\x00'  # 219
        b'\x2f'  # 220 Ü
        b'\x00'  # 221
        b'\x00'  # 222
        b'\x2d'  # 223 ß
        b'\x00'  # 224
        b'\x00'  # 225
        b'\x00'  # 226
        b'\x00'  # 227
        b'\x34'  # 228 ä
        b'\x00'  # 229
        b'\x00'  # 230
        b'\x00'  # 231
        b'\x00'  # 232
        b'\x00'  # 233
        b'\x00'  # 234
        b'\x00'  # 235
        b'\x00'  # 236
        b'\x00'  # 237
        b'\x00'  # 238
        b'\x00'  # 239
        b'\x00'  # 240
        b'\x00'  # 241
        b'\x00'  # 242
        b'\x00'  # 243
        b'\x00'  # 244
        b'\x33'  # 245 ö
        b'\x00'  # 246
        b'\x00'  # 247
        b'\x00'  # 248
        b'\x00'  # 249
        b'\x00'  # 250
        b'\x00'  # 251
        b'\x2f'  # 252 ü
        b'\x00'  # 253
        b'\x00'  # 254
        b'\x00'  # 255

    )
    ASCII_TO_MODIFIER = (
        b'\x00'  # NUL
        b'\x00'  # SOH
        b'\x00'  # STX
        b'\x00'  # ETX
        b'\x00'  # EOT
        b'\x00'  # ENQ
        b'\x00'  # ACK
        b'\x00'  # BEL \a
        b'\x00'  # BS BACKSPACE \b (called DELETE in the usb.org document)
        b'\x00'  # TAB \t
        b'\x00'  # LF \n (called Return or ENTER in the usb.org document)
        b'\x00'  # VT \v
        b'\x00'  # FF \f
        b'\x00'  # CR \r
        b'\x00'  # SO
        b'\x00'  # SI
        b'\x00'  # DLE
        b'\x00'  # DC1
        b'\x00'  # DC2
        b'\x00'  # DC3
        b'\x00'  # DC4
        b'\x00'  # NAK
        b'\x00'  # SYN
        b'\x00'  # ETB
        b'\x00'  # CAN
        b'\x00'  # EM
        b'\x00'  # SUB
        b'\x00'  # ESC
        b'\x00'  # FS
        b'\x00'  # GS
        b'\x00'  # RS
        b'\x00'  # US
        b'\x00'  # SPACE
        b'\x00'  # ! x1e|SHIFT_FLAG (shift 1)
        b'\x20'  # " x34|SHIFT_FLAG (shift ')
        b'\x00'  # # x20|SHIFT_FLAG (shift 3)
        b'\x20'  # $ x21|SHIFT_FLAG (shift 4)
        b'\x20'  # % x22|SHIFT_FLAG (shift 5)
        b'\x20'  # & x24|SHIFT_FLAG (shift 7)
        b'\x20'  # '
        b'\x20'  # ( x26|SHIFT_FLAG (shift 9)
        b'\x20'  # ) x27|SHIFT_FLAG (shift 0)
        b'\x20'  # * x25|SHIFT_FLAG (shift 8)
        b'\x00'  # + x2e|SHIFT_FLAG (shift =)
        b'\x00'  # ,
        b'\x00'  # -
        b'\x00'  # .
        b'\x20'  # /
        b'\x00'  # 0
        b'\x00'  # 1
        b'\x00'  # 2
        b'\x00'  # 3
        b'\x00'  # 4
        b'\x00'  # 5
        b'\x00'  # 6
        b'\x00'  # 7
        b'\x00'  # 8
        b'\x00'  # 9
        b'\x20'  # : x33|SHIFT_FLAG (shift ;)
        b'\x20'  # ;
        b'\x00'  # < x36|SHIFT_FLAG (shift ,)
        b'\x20'  # =
        b'\x20'  # > x37|SHIFT_FLAG (shift .)
        b'\x20'  # ? x38|SHIFT_FLAG (shift /)
        b'\x50'  # @ x1f|SHIFT_FLAG (shift 2)
        b'\x20'  # A x04|SHIFT_FLAG (shift a)
        b'\x20'  # B x05|SHIFT_FLAG (etc.)
        b'\x20'  # C x06|SHIFT_FLAG
        b'\x20'  # D x07|SHIFT_FLAG
        b'\x20'  # E x08|SHIFT_FLAG
        b'\x20'  # F x09|SHIFT_FLAG
        b'\x20'  # G x0a|SHIFT_FLAG
        b'\x20'  # H x0b|SHIFT_FLAG
        b'\x20'  # I x0c|SHIFT_FLAG
        b'\x20'  # J x0d|SHIFT_FLAG
        b'\x20'  # K x0e|SHIFT_FLAG
        b'\x20'  # L x0f|SHIFT_FLAG
        b'\x20'  # M x10|SHIFT_FLAG
        b'\x20'  # N x11|SHIFT_FLAG
        b'\x20'  # O x12|SHIFT_FLAG
        b'\x20'  # P x13|SHIFT_FLAG
        b'\x20'  # Q x14|SHIFT_FLAG
        b'\x20'  # R x15|SHIFT_FLAG
        b'\x20'  # S x16|SHIFT_FLAG
        b'\x20'  # T x17|SHIFT_FLAG
        b'\x20'  # U x18|SHIFT_FLAG
        b'\x20'  # V x19|SHIFT_FLAG
        b'\x20'  # W x1a|SHIFT_FLAG
        b'\x20'  # X x1b|SHIFT_FLAG
        b'\x20'  # Y x1c|SHIFT_FLAG
        b'\x20'  # Z x1d|SHIFT_FLAG
        b'\x50'  # [
        b'\x50'  # \ backslash
        b'\x50'  # ]
        b'\x00'  # ^ x23|SHIFT_FLAG (shift 6)
        b'\x20'  # _ x2d|SHIFT_FLAG (shift -)
        b'\x20'  # `
        b'\x00'  # a
        b'\x00'  # b
        b'\x00'  # c
        b'\x00'  # d
        b'\x00'  # e
        b'\x00'  # f
        b'\x00'  # g
        b'\x00'  # h
        b'\x00'  # i
        b'\x00'  # j
        b'\x00'  # k
        b'\x00'  # l
        b'\x00'  # m
        b'\x00'  # n
        b'\x00'  # o
        b'\x00'  # p
        b'\x00'  # q
        b'\x00'  # r
        b'\x00'  # s
        b'\x00'  # t
        b'\x00'  # u
        b'\x00'  # v
        b'\x00'  # w
        b'\x00'  # x
        b'\x00'  # y
        b'\x00'  # z
        b'\x50'  # { x2f|SHIFT_FLAG (shift [)
        b'\x50'  # | x31|SHIFT_FLAG (shift \)
        b'\x50'  # } x30|SHIFT_FLAG (shift ])
        b'\x50'  # ~ x35|SHIFT_FLAG (shift `)
        b'\x00'  # DEL DELETE (called Forward Delete in usb.org document)
        b'\x00'
        b'\x00'
        b'\x00'
        b'\x00'
        b'\x00'
        b'\x00'
        b'\x00'
        b'\x00'
        b'\x00'
        b'\x00'
        b'\x00'
        b'\x00'
        b'\x00'
        b'\x00'
        b'\x00'
        b'\x00'
        b'\x00'
        b'\x00'
        b'\x00'
        b'\x00'
        b'\x00'
        b'\x00'
        b'\x00'
        b'\x00'
        b'\x00'
        b'\x00'
        b'\x00'
        b'\x00'
        b'\x00'
        b'\x00'
        b'\x00'
        b'\x00'
        b'\x00'
        b'\x00'
        b'\x00'
        b'\x00'
        b'\x00'
        b'\x00'
        b'\x00'
        b'\x00'
        b'\x00'
        b'\x00'
        b'\x00'
        b'\x00'
        b'\x00'
        b'\x00'
        b'\x00'
        b'\x00'
        b'\x00'
        b'\x00'
        b'\x00'
        b'\x00'
        b'\x00'
        b'\x00'
        b'\x00'
        b'\x00'
        b'\x00'
        b'\x00'
        b'\x00'
        b'\x00'
        b'\x00'  # ´
        b'\x00'
        b'\x00'
        b'\x00'
        b'\x00'
        b'\x00'
        b'\x00'
        b'\x00'
        b'\x20'  # Ä
        b'\x00'
        b'\x00'
        b'\x00'
        b'\x00'
        b'\x00'
        b'\x00'
        b'\x00'
        b'\x00'
        b'\x00'
        b'\x00'
        b'\x00'
        b'\x00'
        b'\x00'
        b'\x00'
        b'\x00'
        b'\x00'
        b'\x00'
        b'\x20'  # Ö
        b'\x00'
        b'\x00'
        b'\x00'
        b'\x00'
        b'\x00'
        b'\x20'  # Ü
        b'\x00'
        b'\x00'
        b'\x00'  # ß
        b'\x00'
        b'\x00'
        b'\x00'
        b'\x00'
        b'\x00'  # ä
        b'\x00'
        b'\x00'
        b'\x00'
        b'\x00'
        b'\x00'
        b'\x00'
        b'\x00'
        b'\x00'
        b'\x00'
        b'\x00'
        b'\x00'
        b'\x00'
        b'\x00'
        b'\x00'
        b'\x00'
        b'\x00'
        b'\x00'  # ö
        b'\x00'
        b'\x00'
        b'\x00'
        b'\x00'
        b'\x00'
        b'\x00'
        b'\x00'  # ü
        b'\x00'
        b'\x00'
        b'\x00'
    )

    def __init__(self,keyboard=None):
        """Specify the layout for the given keyboard.

        :param keyboard: a Keyboard object. Write characters to this keyboard when requested.

        Example::

            kbd = Keyboard()
            layout = KeyboardLayoutUS(kbd)
        """

        #self.keyboard = keyboard


    def keycodes(self, char):
        """Return a tuple of keycodes needed to type the given character.

        :param char: A single ASCII character in a string.
        :type char: str of length one.
        :returns: tuple of Keycode keycodes.
        :raises ValueError: if ``char`` is not ASCII or there is no keycode for it.

        Examples::

            # Returns (Keycode.TAB,)
            keycodes('\t')
            # Returns (Keycode.A,)
            keycode('a')
            # Returns (Keycode.SHIFT, Keycode.A)
            keycode('A')
            # Raises ValueError because it's a accented e and is not ASCII
            keycode('é')
        """
        keycode, modifier = self._char_to_keycode(char)
        #if keycode & self.SHIFT_FLAG:
        #    return (32, keycode & ~self.SHIFT_FLAG)

        return (modifier,keycode)

    def _char_to_keycode(self, char):
        """Return the HID keycode for the given ASCII character, with the SHIFT_FLAG possibly set.

        If the character requires pressing the Shift key, the SHIFT_FLAG bit is set.
        You must clear this bit before passing the keycode in a USB report.
        """
        char_val = ord(char)
        if char_val > 255:
            raise ValueError("Not an ASCII character.")
        keycode = self.ASCII_TO_KEYCODE[char_val]
        modifier = self.ASCII_TO_MODIFIER[char_val]
        #if keycode == 0:
        #    raise ValueError("No keycode available for character.")
        return keycode, modifier
