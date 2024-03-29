visbinary.py - Visualize a binary as colors by byte type.
==============================================================================
The colors are chosen by the type of the byte read:

- black for `0x00`
- green for _low_ bytes (`0x01` to `0x1f`)
- blue for _ASCII_ bytes (`0x20` to `0x7e`)
- red for _high_ bytes (`0x7f` to `0xfe`)
- white for `0xff`

By default, colors are **not** printed in 256-color mode, you can however enable
it by using the `-a` (or `--additional-colors`) parameter. This will display
above colors in more shades with respect to the value of the byte read
(darker means lower byte value and vice versa).  
**Notice that this requires a compatible terminal!**

You can visualize any file you want (granted that you have access to it),
though currently only one at a time.

Requirements
-------------------------------------------------------------------------------
- A color-compatible terminal (emulator)
- Python 3

Usage
-------------------------------------------------------------------------------
    visbinary.py [-h] [-a] [-p] [-c COLUMNS] [-o] filename  
  
    positional arguments:  
      filename              path to the file you want to visualize
  
    optional arguments:  
      -h, --help            show this help message and exit
      -a, --additional-colors
                            enable 256 color mode (requires a compatible terminal)
      -p, --print           print out the bytes as hex
      -c COLUMNS, --columns COLUMNS
                            number of bytes (columns) per row (default 32)
      -o, --offset          print out the file offset (in hex) at the beginning of
                            each line

Licensing
-------------------------------------------------------------------------------
visbinary.py - Visualize a binary as colors.
Copyright (c) 2019 Leon Maurice Adam.

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.

-----------
(For a copy of the GNU General Public License see the file _COPYING_ in this folder)
