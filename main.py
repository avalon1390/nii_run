from sensors import Temperature_sensor, Switcher
from repiter import Repiter
from threading import Thread


t1 = Temperature_sensor(123)
t2 = Switcher(332)
f = Repiter
t11 = Thread(target=f.repit, args=(3.0, t1, 0, True))
t22 = Thread(target=f.repit, args=(2.0, t2, 1, True))

t11.start()
t22.start()
t11.join()
t22.join()

