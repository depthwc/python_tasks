import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# 1. Basic Plotting
x1 = np.linspace(-10, 10, 400)
y1 = x1**2 - 4*x1 + 4
plt.figure(figsize=(16, 24))

plt.subplot(5, 2, 1)
plt.plot(x1, y1, 'b')
plt.title('1. Plot of f(x) = x² - 4x + 4')
plt.xlabel('x')
plt.ylabel('f(x)')

# 2. Sine and Cosine Plot
x2 = np.linspace(0, 2 * np.pi, 400)
plt.subplot(5, 2, 2)
plt.plot(x2, np.sin(x2), 'r--', label='sin(x)', marker='o', markevery=40)
plt.plot(x2, np.cos(x2), 'g-.', label='cos(x)', marker='x', markevery=40)
plt.title('2. Sine and Cosine')
plt.xlabel('x')
plt.ylabel('Value')
plt.legend()

# 3. Subplots (2x2 Grid)
x3 = np.linspace(0.01, 5, 100)
x4 = np.linspace(-2, 2, 100)
fig3, axs = plt.subplots(2, 2, figsize=(10, 8))
fig3.suptitle('3. Function Subplots')

axs[0, 0].plot(x4, x4**3, 'm')
axs[0, 0].set_title('f(x) = x³')
axs[0, 0].set_xlabel('x')
axs[0, 0].set_ylabel('y')

axs[0, 1].plot(x4, np.sin(x4), 'c')
axs[0, 1].set_title('f(x) = sin(x)')

axs[1, 0].plot(x3, np.exp(x3), 'g')
axs[1, 0].set_title('f(x) = e^x')

axs[1, 1].plot(x3, np.log(x3 + 1), 'r')
axs[1, 1].set_title('f(x) = log(x + 1)')

for ax in axs.flat:
    ax.set(xlabel='x', ylabel='y')

plt.tight_layout(rect=[0, 0, 1, 0.95])

# 4. Scatter Plot
x4 = np.random.uniform(0, 10, 100)
y4 = np.random.uniform(0, 10, 100)
plt.figure(figsize=(8, 6))
plt.subplot(5, 2, 3)
plt.scatter(x4, y4, c='purple', marker='*')
plt.title('4. Scatter Plot of Random Points')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)

# 5. Histogram
data5 = np.random.normal(0, 1, 1000)
plt.subplot(5, 2, 4)
plt.hist(data5, bins=30, color='skyblue', alpha=0.7)
plt.title('5. Histogram of Normal Distribution')
plt.xlabel('Value')
plt.ylabel('Frequency')

# 6. 3D Surface Plot
fig6 = plt.figure(figsize=(8, 6))
ax6 = fig6.add_subplot(111, projection='3d')
X6 = np.linspace(-5, 5, 100)
Y6 = np.linspace(-5, 5, 100)
X6, Y6 = np.meshgrid(X6, Y6)
Z6 = np.cos(X6**2 + Y6**2)
surf = ax6.plot_surface(X6, Y6, Z6, cmap='viridis')
fig6.colorbar(surf)
ax6.set_title('6. 3D Surface: f(x, y) = cos(x² + y²)')
ax6.set_xlabel('x')
ax6.set_ylabel('y')
ax6.set_zlabel('f(x, y)')

# 7. Bar Chart
products = ['Product A', 'Product B', 'Product C', 'Product D', 'Product E']
sales = [200, 150, 250, 175, 225]
colors = ['red', 'blue', 'green', 'orange', 'purple']
plt.figure(figsize=(8, 6))
plt.subplot(5, 2, 5)
plt.bar(products, sales, color=colors)
plt.title('7. Sales by Product')
plt.xlabel('Products')
plt.ylabel('Sales')

# 8. Stacked Bar Chart
time = ['T1', 'T2', 'T3', 'T4']
cat_a = [3, 5, 1, 6]
cat_b = [2, 3, 4, 1]
cat_c = [1, 2, 5, 2]
plt.subplot(5, 2, 6)
plt.bar(time, cat_a, label='Category A')
plt.bar(time, cat_b, bottom=cat_a, label='Category B')
bottom_cat_c = np.array(cat_a) + np.array(cat_b)
plt.bar(time, cat_c, bottom=bottom_cat_c, label='Category C')
plt.title('8. Stacked Bar Chart')
plt.xlabel('Time Period')
plt.ylabel('Values')
plt.legend()

plt.tight_layout()
plt.show()
