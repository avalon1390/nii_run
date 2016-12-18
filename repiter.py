import time


class Repiter:
    def repit(x, t,w,e):
        while True:
            print(time.time(),t.set(w,e))
            time.sleep(x)
