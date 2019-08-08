import time
import sys

dots = [".", "..", "...", "....", "....."] #array of dots for loading text

num = 0
num_dots = 0
for n in range(0, 101): #counter from 0 to 100
    if num_dots > 4:
        num_dots = 0
    sys.stdout.write('\r' + "{}% complete".format(num) +
    dots[num_dots] + ' ' * 10) #added padding for full "overwrite" of previous line
    num += 1
    num_dots += 1
    time.sleep(0.1)
