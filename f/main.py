from roboid import *
import random
import threading

a = HamsterS()
global q
q = 0
sensivity = 70
def main():
    while 1:
        left = a.left_proximity() 
        right = a.right_proximity()
        print(left, right)
        wait(500)

def block():
    wait(100)
    a.wheels(-50, 50)
    wait(600)
    a.wheels(0)
    left = a.left_proximity()
    right = a.right_proximity()
    f = left + right
    wait(500)
    a.wheels(50, -50)
    wait(1200)
    a.wheels(0)
    wait(500)
    left = a.left_proximity()
    right = a.right_proximity()
    s = left + right
    print(f, s)
    if s < f:
        return 0
    if f < s:
        a.wheels(50, -50)
        wait(1200)
        a.wheels(0)
        wait(500)

# maint = threading.Thread(target=main)
# maint.start()

while 1:
    left = a.left_proximity()
    right = a.right_proximity()

    if left > 75 and right > 75:
        block()
    else:
        a.wheels(50)
# while True:
#     left = a.left_proximity() 
#     right = a.right_proximity()
#     if left>60:
#         a.wheels(sensivity, -sensivity)
#     elif right>60:
#         a.wheels(-sensivity, sensivity)
#     else:
#         if left == 0 and right > 30:
#             a.wheels(-80)
#             wait(200)
#             a.wheels(-sensivity, sensivity)
#             wait(200)
#         elif right == 0 and left > 30:
#             a.wheels(-80)
#             wait(200)
#             a.wheels(-sensivity, sensivity)
#             wait(200)
#         a.wheels(100)