import matplotlib.pyplot as plt
x= [i for i in range(-5,6)]
#print(x)
y = []
# y = ax + b
for i in x:
    y.append(2*i-3)

plt.plot(x,y)
plt.plot(x,y, 'ro')
plt.grid(color='green', linestyle='--', linewidth=1)
plt.show()

