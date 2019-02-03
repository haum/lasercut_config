#! /usr/bin/env python
# -*- coding:utf8 -*-
#
# gen.py
#
# Copyright © 2019 Mathieu Gaborit (matael) <mathieu@matael.org>
#
# Licensed under the "THE BEER-WARE LICENSE" (Revision 42):
# Mathieu (matael) Gaborit wrote this file. As long as you retain this notice
# you can do whatever you want with this stuff. If we meet some day, and you
# think this stuff is worth it, you can buy me a beer or coffee in return
#


width, height = 10, 10
xclearance, yclearance = 2.5, 2.5
power_step = 0.1
speed_step = 600

print("""G21
G90
M3
M106
G92 X0 Y0 Z0""")

for row in range(10):
    for col in range(10):
        x_ref = (width + xclearance)*col
        y_ref = (height + yclearance)*row
        power = power_step*(col + 1)
        speed = speed_step*(row + 1)
        print(f'G0 X{x_ref} Y{y_ref}')
        print(f'G1 X{x_ref+width} Y{y_ref} S{power:.4f} F{speed}')
        print(f'G1 X{x_ref+width} Y{y_ref+height}')
        print(f'G1 X{x_ref} Y{y_ref+height}')
        print(f'G1 X{x_ref} Y{y_ref}')

print("""G0 X0 Y0
M5
M107""")
