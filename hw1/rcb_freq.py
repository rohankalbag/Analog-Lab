import matplotlib.pyplot as plt
import numpy as np

#_______________________________________________________________________________________________________________
filename     = "rcb_readings"              
#_______________________________________________________________________________________________________________

x_axis_column_number = 1                     
y_axis_column_start = x_axis_column_number+1  


global readings
global x_readings
global y_readings

x_readings = []
y_readings = []

numbers =['0','1','2','3','4','5','6','7','8','9']

#This function read the file and returns the x and y axis values
def read_file(axis_index):
    axis_readings = []
    readings_file = open(filename, "r");
    for x in readings_file:
        if x == "":
            continue
        elif not(x[0] in numbers):
            continue
        x = x.replace("\n", "")
        readings = [float(d) for d in x.split()]
        try:
            axis_readings.append(readings[axis_index])
        except:
            print("error")
            exit(0)
    return axis_readings



if __name__ == '__main__':
    x_readings = read_file(x_axis_column_number)
    y_readings = []
    for column in range(y_axis_column_start, 1 + y_axis_column_start):
        y_readings.append(read_file(column))    
    x_array = np.array(x_readings)
    y_array = np.array(y_readings).flatten()
    #print(x_array)
    #print(y_array)
    peak_val = max(y_array)
    index = np.where(y_array == peak_val)[0]
    print("Peak Amplitude Frequency:",x_array[index][0],"Hz")
    print("Maximum Amplitude in dB:", y_array[index][0])
    i=index.copy()
    while(abs(y_array[index][0]-y_array[i][0])<3):
        #print(abs(y_array[index][0]-y_array[i][0]))
        i+=1
    print("f_upper:",x_array[i][0],"Hz")
    i=index.copy()
    while(abs(y_array[index][0]-y_array[i][0])<3):
        i-=1
    print("f_lower:",x_array[i][0],"Hz")








