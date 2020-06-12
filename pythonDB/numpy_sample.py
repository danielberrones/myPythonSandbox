import numpy as np
import matplotlib.pyplot as plt
import random

a = []
for x in range(5):
    a.append(random.randint(0,1000))

a1 = np.asarray(a)
print(np.max(a1))

plt.plot(a1)
plt.title("5 Random Numbers from 0-1000")
plt.xlabel("This is X")
plt.ylabel("This is Y")
plt.legend(["THIS IS THE LEGEND"])
plt.show()

print(len(a1))
