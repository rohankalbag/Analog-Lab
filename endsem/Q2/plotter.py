import imp


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

x = pd.read_csv('plotvalues.csv')
plt.plot(np.array(x['Frequency(Hz)']), 20*np.log10(np.array(x['Vpp(mV)'])/1000),'r-o')
plt.xlabel("Frequency")
plt.ylabel("20*log_10(Vpp/1000mV)")
plt.show()