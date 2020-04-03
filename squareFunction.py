'''
    Date: 2/04/2020
    Description: A function that takes input n (# of boxes) and size (size of the square) and 
    return the Xn, Yn, Wn, Hn and ebt (elevated body temperature) and write to a txt file

'''
import os, sys
import re
import math
import argparse
import numpy as np

FILE_NAME = 'output.txt'

def square(width, height, n, w, h):
    x0 = (width - n * w) // 2
    y0 = (height - n * h) //2
    coords = [[x0 + ix * w, y0 + iy * h] for iy in range(n) for ix in range(n)]
    return coords

print(square(320, 240, 2, 32, 24))



# def square(n, size, ebt):
#     xs = 320
#     ys = 256
#     nx = int(xs)/2
#     ny = int(ys)/2
  
#     print(nx, ny)
#     return nx, ny

# def writetoendofline(lines, line_no, append_txt):
#     lines[line_no] = lines[line_no].replace('\n', '') + append_txt + '\n'

# # open the file
# with open(FILE_NAME, 'r') as txtfile:
#     lines = txtfile.readlines()
# writetoendofline(lines, 1, '23 ')
# # writetoendofline(lines, 0, nx)
# # write to the file
# with open(FILE_NAME, 'w') as txtfile:
#     txtfile.writelines(lines)
# # write to the file
# txtfile.close()


# if __name__ == '__main__':
#     n = sys.argv[1]
#     size = sys.argv[2]
#     ebt = sys.argv[3]
#     square(n, size, ebt)