import matplotlib.pyplot as plt
import numpy as np

# Define the x values
x = np.linspace(-10, 10, 400)  # Generates 400 points between -10 and 10

# Define the lines
y1 = 2 * x + 1
y2 = 2 * x + 2
y3 = 2 * x + 3

# Plot the lines
plt.plot(x, y1, label='y = 2x + 1', color='black', linestyle='-')  # Solid line
plt.plot(x, y2, label='y = 2x + 2', color='gray', linestyle='--')  # Dashed line
plt.plot(x, y3, label='y = 2x + 3', color='black', linestyle=':')  # Dotted line

# Add title and labels
plt.title('Graphs of y = 2x + 1, y = 2x + 2, and y = 2x + 3')
plt.xlabel('x-axis')
plt.ylabel('y-axis')

# Add legend
plt.legend()

# Show the grid
plt.grid(True, linestyle='--', linewidth=0.5)

# Display the plot
plt.show()