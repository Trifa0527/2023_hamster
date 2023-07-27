from roboid import *

a = HamsterS()

def rgb(r, l):                                         
    a.leds(r[0], r[1] , r[2], l[0], l[1], l[2])

rgb([255, 0, 255], [0,255,0])