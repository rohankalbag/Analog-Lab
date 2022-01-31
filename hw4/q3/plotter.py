import matplotlib.pyplot as plt
import numpy as np

#_______________________________________________________________________________________________________________
filename = ["./front_readings","./reverse_readings"]  
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
def read_file(axis_index, filename):
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
    plt.title("OPAMP Circuit 3(a) - Schmidt Trigger")
    plt.xticks(range(-6,6))
    x_readings = read_file(x_axis_column_number,filename[0])
    y_readings = []
    for column in range(y_axis_column_start, 1 + y_axis_column_start):
        y_readings.append(read_file(column,filename[0]))    
    x_array = np.array(x_readings)
    y_array = np.array(y_readings).flatten()
    plt.plot(x_array,y_array, label="From -5V to 5V")
    x_readings = read_file(x_axis_column_number,filename[1])
    y_readings = []
    for column in range(y_axis_column_start, 1 + y_axis_column_start):
        y_readings.append(read_file(column,filename[1]))    
    x_array = np.array(x_readings)
    y_array = np.array(y_readings).flatten()
    plt.plot(x_array,y_array,label="From 5V to -5V")
    plt.ylabel("$V_{out}$")
    plt.xlabel("$V_{in}$")
    plt.legend()
    plt.show()







