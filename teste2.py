import os
import random
import time
i = 0

while (i == 0):
    a = random.randint(0, 10)
    os.system('clear')

    for ii in range(11):
        if ii == a:
            print('|------o-------|', '   jarda: ', a*10)
        else:
            print('|--------------|')

    if a == 10:
        print('TOUCHDOWN!!!')
        i = 1
    time.sleep(1)
