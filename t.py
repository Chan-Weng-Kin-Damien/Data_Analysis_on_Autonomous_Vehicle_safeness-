import pandas as pd
import matplotlib.pyplot as plt

# Sample data creation
data = {
    'Weather - Snow': ['Y', '', 'Y', '', 'Y'],
    'Weather - Cloudy': ['', 'Y', '', 'Y', ''],
    'Weather - Fog/Smoke': ['', '', 'Y', '', ''],
    'Weather - Rain': ['', 'Y', '', 'Y', ''],
    'Weather - Severe Wind': ['', '', '', 'Y', ''],
    'Weather - Unknown': ['', '', '', '', 'Y'],
    'Weather - Other': ['', '', '', '', ''],
    'Weather - Other Text': ['', '', '', 'Y', '']
}

# Create a DataFrame
df = pd.DataFrame(data)

# Count occurrences of 'Y' in each weather column
weather_counts = (df == 'Y').sum()

# Display the counts
print("Weather Counts:")
print(weather_counts)

# Plotting the pie chart
plt.figure(figsize=(10, 7))
plt.pie(weather_counts, labels=weather_counts.index, autopct='%1.1f%%', startangle=140, colors=plt.cm.viridis(range(len(weather_counts))))
plt.title('Occurrence of Weather Conditions', fontsize=16)
plt.axis('equal')  # Equal aspect ratio ensures the pie chart is circular.
plt.show()