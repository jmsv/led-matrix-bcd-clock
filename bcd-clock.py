#!/usr/bin/env python

import max7219.led as led
from time import time, sleep
import datetime, thread

matrix = led.matrix(cascaded=1)


def main():
    prev_sec = datetime.datetime.now().second
    while(datetime.datetime.now().second == prev_sec):
        pass
    sleep(0.005)
    starttime = time()
    while(True):
        now = datetime.datetime.now()
        display_number(now.hour, now.minute, now.second)
        #print('time:  ' + str(time())
        #      + '    start time:  ' + str(starttime)
        #      + '    current microseconds:  ' + str(now.microsecond))
        '''Uncomment 3 lines above to print time stats'''
        sleep(1.0 - ((time() - starttime) % 1.0))


def display_number(hours, minutes, seconds):
    bin_list = []
    '''hours'''
    stringh = str(hours).zfill(2)
    bin_list.extend(den_to_bin(stringh[n]) for n in range(0, 2))
    '''minutes'''
    stringm = str(minutes).zfill(2)
    bin_list.extend(den_to_bin(stringm[n]) for n in range(0, 2))
    '''seconds'''
    strings = str(seconds).zfill(2)
    bin_list.extend(den_to_bin(strings[n]) for n in range(0, 2))
    matrix_led(bin_list)
    del bin_list[:]


def matrix_led(binary_list):
    for pix_col, binary in enumerate(binary_list):
        for pix_row, bit in enumerate(binary):
            matrix.pixel(pix_col+1, pix_row+2, int(bit), redraw=True)
            

def den_to_bin(n):
    return '{0:04b}'.format(int(n)).zfill(4)


#main() #uncomment when debugging


try:
    main()
except:
    try:
        print('\nClearing matrix...')
        matrix.letter(0, 0)
        print('Done. Exiting...')
    except:
        print('\nAborting...')

