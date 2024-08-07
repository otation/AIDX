import numpy as np
import matplotlib.pyplot as plt

ftemp = [63, 73, 80, 86, 84, 78, 66, 54, 45, 63]
F=np.array(ftemp)
(F-32)*5/9
plt.plot(F)
plt.show()
