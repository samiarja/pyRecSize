'''
    Date: 2/04/2020
    Description: A function that takes input n (# of boxes) and size (size of the square) and 
    return the Xn, Yn, Wn, Hn and ebt (elevated body temperature) and write to a txt file

'''
import os, sys
import re

FILE_NAME = 'output.txt'

def square(n, size,ebt):
    width = 320
    height= 256
    minTemperture = -100
    Prediction_Reange_Num = 1
    Prediction_Reange_Interval  = 10
    Trend_Reange_Num  = 1
    Trend_Reange_Interval = 1
    Region_Trend_Min = minTemperture
    Region_Trend_Max  = 30
    x0 = (width - n * size) // 2
    y0 = (height - n * size) // 2
    Predicition_Region = [[x0 + ix * size, y0 + iy * size, size, size] for iy in range(n) for ix in range(n)]
    Min_Temperture = [[minTemperture] for iy in range(n) for ix in range(n)]
    Max_Temperture = [[ebt] for iy in range(n) for ix in range(n)]
    Prediction_Reange_Num = [[Prediction_Reange_Num] for iy in range(n) for ix in range(n)]
    Prediction_Reange_Interval  = [[Prediction_Reange_Interval] for iy in range(n) for ix in range(n)]
    Trend_Reange_Num = [[Trend_Reange_Num] for iy in range(n) for ix in range(n)]
    Trend_Reange_Interval = [[Trend_Reange_Interval] for iy in range(n) for ix in range(n)]
    Region_Trend_Min = [[Region_Trend_Min] for iy in range(n) for ix in range(n)]
    Region_Trend_Max = [[Region_Trend_Max] for iy in range(n) for ix in range(n)]
    
    return Predicition_Region, Min_Temperture, Max_Temperture, Prediction_Reange_Num, Prediction_Reange_Interval, Trend_Reange_Num, Trend_Reange_Interval, Region_Trend_Min, Region_Trend_Max

def writetoendofline(lines, line_no, append_txt):
    lines[line_no] = lines[line_no].replace('\n', '') + append_txt + '\n'
    
n = int(input("Enter Number of Boxes: "))
size = int(input("Enter Size of the boxes: "))
ebt = int(input("Enter Elevated Body Temperature: "))

row_1, row_2, row_3, row_4, row_5, row_6, row_7, row_8, row_9 = square(n, size, ebt)

# open the file
with open(FILE_NAME, 'r') as txtfile:
    lines = txtfile.readlines()

writetoendofline(lines, 0, " ".join(str(x) for x in [str(i) for i in row_1]))
writetoendofline(lines, 1, " ".join(str(x) for x in [str(i) for i in row_2]))
writetoendofline(lines, 2, " ".join(str(x) for x in [str(i) for i in row_3]))
writetoendofline(lines, 3, " ".join(str(x) for x in [str(i) for i in row_4]))
writetoendofline(lines, 4, " ".join(str(x) for x in [str(i) for i in row_5]))
writetoendofline(lines, 5, " ".join(str(x) for x in [str(i) for i in row_6]))
writetoendofline(lines, 6, " ".join(str(x) for x in [str(i) for i in row_7]))
writetoendofline(lines, 7, " ".join(str(x) for x in [str(i) for i in row_8]))
writetoendofline(lines, 8, " ".join(str(x) for x in [str(i) for i in row_9]))

# write to the file
with open(FILE_NAME, 'w') as txtfile:
    txtfile.writelines(lines)

txtfile.close()

with open(FILE_NAME, 'r') as my_file:
    text = my_file.read()
    text = text.replace("[", "")
    text = text.replace("]", "")

with open(FILE_NAME, 'w') as my_file:
    my_file.write(text)
my_file.close()

print("Process Completed...")
print("Please check output.txt...")
