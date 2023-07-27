from roboid import *
import random

a = HamsterS()

def roulette():
    if random.randrange(1,3) == 1:
        a.wheels(100, -100)
        wait(1000*random.randrange(0,11))
        a.wheels(0)
    else:
        a.wheels(-100, 100)
        wait(1000*random.randrange(0,11))
        a.wheels(0)
    

roulette()