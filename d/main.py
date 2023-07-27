from roboid import *

a = HamsterS()

def buzzer(time, hz):
    a.buzzer(hz)
    wait(1000*time)
    a.buzzer(0)

def note(time, note):
    a.note(note, time)

# buzzer(1, 500)
# note(0.2, "C4")