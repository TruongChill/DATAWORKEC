import matplotlib.pyplot as plt

# Data
issues = ['Waking up during sleep', 'Difficulty sleeping', 'Headache', 'Feeling cold', 'Nightmares', 'Eye pain', 'No issues']
quantity = [13, 9, 7, 11, 4, 8, 18]

# Create Scatter Plot
plt.scatter(range(len(issues)), quantity)

# Set labels and title
plt.xlabel('Sleep-related Issues')
plt.ylabel('Quantity (n)')
plt.title('Scatter Plot for Sleep-related Issues')

# Adjust x-axis ticks
plt.xticks(range(len(issues)), issues, rotation=45, ha='right')

# Display the plot
plt.show()