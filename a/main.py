from roboid import *

a = HamsterS()
def f(b):
    for i in range(0, b):
        a.board_forward()
def r(b):
    for i in range(0, b):
        a.board_right()
def l(b):
    for i in range(0, b):
        a.board_left()
        
            # (1,3) r
f(4)     # (5,3) r
r(1)     # (5,3) b 
f(1)     # (5,4) b       found
r(2)     # (5,4) f
f(3)     # (5,1) f
l(1)     # (5,1) l
f(2)     # (3,1) l       found
r(2)     # (3,1) r
f(2)     # (5,1) r
r(1)     # (5,1) b
f(2)     # (5,3) b
r(1)     # (5,3) l
f(4)     # (1,3) l
r(2)     # (1,3) r