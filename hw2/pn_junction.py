import matplotlib.pyplot as plt
import numpy as np

#_______________________________________________________________________________________________________________
filename     = "pn_readings.txt"              
#_______________________________________________________________________________________________________________

with open(filename,'r') as t:
    values = t.readlines()
    values = [(i[0:-1].split()) for i in values]
    x_values = np.array([float(i[0]) for i in values])
    y_values = np.log(np.array([float(i[1]) for i in values]))

x1 = 0.604
x2 = 0.706
y1 = np.log(2.85E-04)
y2 = np.log(0.0111)

m = (y2-y1)/(x2-x1)
k = 1.38E-23
q = 1.6E-19
T = 300

n = q/(k*T*m)
print(n)

plt.xlabel("V")
plt.ylabel("$log_{e}(I)$")
plt.title("$log_{e}(I)-V$ characteristics for PN junction diode")
plt.plot(x_values,y_values)
plt.show()