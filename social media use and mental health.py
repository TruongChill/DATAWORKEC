import matplotlib.pyplot as plt

# Data
time_of_social_media = ['< 2h', '2-4h', '4-6h', '> 6h']
health_issues = ['Back pain', 'Fatigue', 'Myopia', 'Acne']

# Generate chart data
data = [
    [11,23 ,37, 52],
    [18, 30, 49, 66],
    [30, 32, 45, 68],
    [62, 71, 88, 100]
]

# Create Line Graph
fig, ax = plt.subplots()

for i, row in enumerate(data):
    ax.plot(time_of_social_media, row, label=health_issues[i])

# Set labels and title
ax.set_xlabel('Time of Social Media Usage')
ax.set_ylabel('Health Issue Severity')
ax.set_title('Health Issue Severity based on Time of Social Media Usage')

# Display legend
ax.legend()

plt.show()