from roboid import *

a = HamsterS()

def gofoward(time, intensity):
    a.wheels(intensity)
    wait(time*1000)                 # time초 후 멈춤
    a.wheels(0)
    
def goback(time, intensity):
    a.wheels(-intensity)
    wait(time*1000)                 # time초 후 멈춤
    a.wheels(0)

def rotate(direction, degree):
    if direction == "r":
        a.wheels(100, -100)         # |속도|를 100으로 했을 때 1°당 약 3ms가 소요됨
        wait(3.33*degree)
        a.wheels(0)
    if direction == "l":
        a.wheels(-100, 100)
        wait(3.33*degree)
        a.wheels(0)

# rotate('l', 45)
# gofoward(3, 100)
# goback(3, 100)