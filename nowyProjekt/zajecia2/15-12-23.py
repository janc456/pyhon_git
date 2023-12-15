import matplotlib.pyplot as plt

x = [1,2,3,4]
y = [3,2,1,0]
plt.plot(x,y)
plt.plot(x,y, 'ro')
plt.grid(color='green', linestyle='--', linewidth=1)
plt.show()