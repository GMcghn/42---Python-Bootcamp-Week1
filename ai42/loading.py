import sys
import time

def y(elem):
    z = elem*2
    return z


def ft_progress(r, sleep_time, y):
    ts = time.time()
    zz = 0
    for i in range(1,r+1):
        if i/r == 1: 
            x='' 
        else: 
            x='>'
        
        zz += y(i)
        te = time.time()
        elapsed = te - ts
        ETA = elapsed/i*r - elapsed
        print('ETA: {}s [ {}%][{}{}{}] {}/{} | elapsed time {}s'.format(
            round(ETA,2), round(i/r*100), (round(i/r*20))*'=', x ,(20-round(i/r*20))*' ',  i, r , round(elapsed,2)
            ), end ="\r")
        
        if i == r:
            print()
            print(zz)

        time.sleep(sleep_time)

# ft_progress(100, 0.05, y)