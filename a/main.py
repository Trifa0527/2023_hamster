from roboid import *

a = HamsterS()
def f(a, b):
    for i in range(0, b):
        a.board_forward()
def r(a, b):
    for i in range(0, b):
        a.board_right()
def l(a, b):
    for i in range(0, b):
        a.board_left()
        
            # (1,3) r
f(a, 4)     # (5,3) r
r(a, 1)     # (5,3) b 
f(a, 1)     # (5,4) b       found
r(a, 2)     # (5,4) f
f(a, 3)     # (5,1) f
l(a, 1)     # (5,1) l
f(a, 2)     # (3,1) l       found
r(a, 2)     # (3,1) r
f(a, 2)     # (5,1) r
r(a, 1)     # (5,1) b
f(a, 2)     # (5,3) b
r(a, 1)     # (5,3) l
f(a, 4)     # (1,3) l
r(a, 2)     # (1,3) r