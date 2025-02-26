import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Specify the path to your CSV file
filepath_ADAS = r'C:\Users\user\Desktop\2425\society and sports\AKAHACK\SGO-2021-01_Incident_Reports_ADAS.csv' 
filepath_ADS = r"C:\Users\user\Desktop\2425\society and sports\AKAHACK\SGO-2021-01_Incident_Reports_ADS.csv"
filepath_OTHER = r'C:\Users\user\Desktop\2425\society and sports\AKAHACK\SGO-2021-01_Incident_Reports_OTHER.csv'

# Read the CSV file
ADAS = pd.read_csv(filepath_ADAS)
ADS =  pd.read_csv(filepath_ADS)
OTHER =  pd.read_csv(filepath_OTHER)

ADAS['Source'] = 'AUTOMATION'
ADS['Source'] = 'AUTOMATION'
OTHER['Source'] = 'OTHER'
ADAS['Source2'] = 'ADAS'
ADS['Source2'] = 'ADS'
OTHER['Source2'] = 'OTHER'

df0 = pd.concat([ADAS, ADS, OTHER], ignore_index=True)


df = df0[df0['Source2'] == 'OTHER']

weather_counts = (df == 'Y').sum()

weather_columns = [
    'Weather - Snow',
    'Weather - Cloudy',
    'Weather - Fog/Smoke',
    'Weather - Rain',
    'Weather - Severe Wind',
    'Weather - Other',
    'Weather - Other Text',
]

# Count occurrences of 'Y' in the specified weather columns
weather_counts = (df[weather_columns] == 'Y').sum()

# Display the counts
print("Weather Counts:")
print(weather_counts)

# Plotting the pie chart
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0', '#ffb3e6', '#c2f0c2', '#ff6666']

# Plotting the pie chart
plt.figure(figsize=(10, 7))
plt.pie(weather_counts, labels=weather_counts.index, autopct='%1.1f%%', startangle=140, colors=colors)
plt.title('Occurrence of Weather Conditions for Other', fontsize=16)
plt.axis('equal')  # Equal aspect ratio ensures the pie chart is circular.
plt.show()