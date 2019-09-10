#!/usr/bin/python3

# visbinary.py - Visualize a binary as colors.
# Copyright (c) 2019 Leon Maurice Adam.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

from argparse import ArgumentParser


# Pad 'hexstr' with n leading zeroes
def hex_pad(hexstr, n):
    return "0x" + hexstr[2:].zfill(n)


def visualize(f, colors256, print_b, columns, print_off):
    b = f.read(1)
    count = 0
    while b:
        # print offset if wanted
        if print_off and count == 0:
            print(hex_pad(hex(f.tell() - 1), 8) + "  |", end='')

        count += 1

        print("\033[", end='')
        if colors256:
            # TODO This is 'broken', fix it
            print(str(ord(b)), end='')
        else:
            i = ord(b)

            # 0x00 byte, black
            if i == 0:
                print("40", end='')
            # low bytes, green
            elif i in range(1, ord(' ')):
                print("42", end='')
            # ascii bytes, blue
            elif i in range(ord(' '), ord('~') + 1):
                print("44", end='')
            # high bytes, red
            elif i in range(ord('~') + 1, 255):
                print("41", end='')
            # 0xff bytes, white
            elif i == 255:
                print("47", end='')
        print("m", end='')

        if print_b:
            print(b.hex(), end='')
        else:
            print(" ", end='')

        # Begin new line and reset to default colors
        if count == columns:
            print("\033[0m")
            count = 0

        b = f.read(1)

    print()


def visbinary():
    parser = ArgumentParser(description="Visualize a binary as colors by byte type.")
    # TODO Fix 256 colors mode
    # parser.add_argument("--colors256", "-c", help="enable 256 color mode (requires a compatible terminal)", action="store_true")
    parser.add_argument("-p", "--print", help="print out the bytes as hex", action="store_true")
    parser.add_argument("-c", "--columns", type=int, default=32, help="number of bytes (columns) per row (default 32)")
    parser.add_argument("-o", "--offset", help="print out the file offset (in hex) at the beginning of each line", action="store_true")
    parser.add_argument("filename", help="path to the file you want to visualize")
    args = parser.parse_args()

    with open(args.filename, "rb") as f:
        print("File '" + args.filename + "':")
        visualize(f, False, args.print, args.columns, args.offset)
        f.close()


if __name__ == "__main__":
    visbinary()
