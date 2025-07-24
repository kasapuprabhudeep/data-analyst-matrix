from mean_var_std import calculate
import matplotlib.pyplot as plt

# Test the function
result = calculate([0, 1, 2, 3, 4, 5, 6, 7, 8])

# Print dictionary
print(result)

# ===== VISUALIZATION SECTION =====

# Plotting row-wise and column-wise mean
row_mean = result['mean'][1]
col_mean = result['mean'][0]

plt.figure(figsize=(10, 5))

# Subplot 1: Bar chart for row-wise mean
plt.subplot(1, 2, 1)
plt.bar(range(1, 4), row_mean, color='skyblue')
plt.title("Row-wise Mean")
plt.xlabel("Row")
plt.ylabel("Mean Value")

# Subplot 2: Bar chart for column-wise mean
plt.subplot(1, 2, 2)
plt.bar(['Col 1', 'Col 2', 'Col 3'], col_mean, color='salmon')
plt.title("Column-wise Mean")
plt.xlabel("Column")
plt.ylabel("Mean Value")

plt.tight_layout()
plt.show()
