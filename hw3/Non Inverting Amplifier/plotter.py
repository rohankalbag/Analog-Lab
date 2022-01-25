import matplotlib.pyplot as plt
import numpy as np

#_______________________________________________________________________________________________________________
filename = ["bode_10k","bode_100k"]   
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
    plt.title("Bode Plot for Non Inverting Amplifier")
    x_readings = read_file(x_axis_column_number,filename[0])
    y_readings = []
    for column in range(y_axis_column_start, 1 + y_axis_column_start):
        y_readings.append(read_file(column,filename[0]))    
    x_array = np.array(x_readings)
    y_array = np.array(y_readings).flatten()
    plt.plot(np.log10(x_array),y_array, label="$R_{2}=10k\Omega$")
   
    x_readings = read_file(x_axis_column_number,filename[1])
    y_readings = []
    for column in range(y_axis_column_start, 1 + y_axis_column_start):
        y_readings.append(read_file(column,filename[1]))    
    x_array = np.array(x_readings)
    y_array = np.array(y_readings).flatten()
    plt.plot(np.log10(x_array),y_array,label="$R_{2}=100k\Omega$")
    plt.ylabel("$20log_{10}(V_{out}/V_{in})$")
    plt.xlabel("$log_{10}(frequency)$")
    plt.legend()
    plt.show()







