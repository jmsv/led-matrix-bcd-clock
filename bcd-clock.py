#!/usr/bin/env python

import max7219.led as led
from time import sleep
import datetime, thread

matrix = led.matrix(cascaded=1)


def main():
    prev_sec = datetime.datetime.now().second
    while(datetime.datetime.now().second == prev_sec):
        pass
    sleep(0.4)
    while(True):
        thread.start_new_thread(clock_update, ())
        sleep(0.99871)
        # ^ sleep of just less than a second
        # ^ actual value based on experimental data

def clock_update():
    now = datetime.datetime.now()
    display_number(now.hour, now.minute, now.second)


def display_number(hours, minutes, seconds):
    bin_list = []
    #hours
    stringh = str(hours).zfill(2)
    bin_list.append(den_to_bin(stringh[0]).zfill(4))    
    bin_list.append(den_to_bin(stringh[1]).zfill(4))
    #minutes
    stringm = str(minutes).zfill(2)
    bin_list.append(den_to_bin(stringm[0]).zfill(4))    
    bin_list.append(den_to_bin(stringm[1]).zfill(4))
    #seconds
    strings = str(seconds).zfill(2)
    bin_list.append(den_to_bin(strings[0]).zfill(4))    
    bin_list.append(den_to_bin(strings[1]).zfill(4))
    #matrix
    matrix_led(bin_list)
    #print(bin_list)
    del bin_list[:]


def matrix_led(binary_list):
    for pix_col, binary in enumerate(binary_list):
        for pix_row, bit in enumerate(binary):
            matrix.pixel(pix_col+1, pix_row+2, int(bit), redraw=True)
            

def den_to_bin(n):
    return '{0:04b}'.format(int(n))


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


