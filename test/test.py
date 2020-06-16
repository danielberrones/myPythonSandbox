import matplotlib.pyplot as plt

myLabels = ("PHP","WordPress","JavaScript","Python","HTML/CSS")
totals = [50,50,50,10,30]

plt.pie(totals, labels=myLabels)
plt.show()