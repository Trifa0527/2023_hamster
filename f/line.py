from roboid import *
import threading

car = HamsterS()

while 1:
    left, right = car.left_floor(), car.right_floor()
    print(left, right)
    if left<30:
        if left < 10 and right < 10:
            car.wheels(0)
            break
        left = 0
        right = 200
    elif right<30:
        left = 200
        right = 0
    elif right > 75 and left > 75:
        car.wheels(left, right)
    else:
        car.wheels(left/2, right/2)
    