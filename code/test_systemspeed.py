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
df = df0[['Source2', 'SV Precrash Speed (MPH)']]
print(df)
custom_order = ['OTHER', 'ADS', 'ADAS']
df['Source2'] = pd.Categorical(df['Source2'], categories=custom_order, ordered=True)

# Sort the DataFrame by the custom order
df = df.sort_values(by='Source2')
df = df[df['SV Precrash Speed (MPH)'].notna()]
df = df[df['SV Precrash Speed (MPH)'] != 0]

# Display the filtered DataFrame
print(df)

#draw
sns.set_theme(style="ticks", palette="pastel")

# Load the example tips dataset
#tips = sns.load_dataset(df)

# Draw a nested boxplot to show bills by day and time

# Create the boxplot
plt.figure(figsize=(10, 6))
sns.boxplot(x='Source2', y='SV Precrash Speed (MPH)', data=df)

# Adding title and labels
plt.title('Boxplot of Precrash Speed by Source2')
plt.xlabel('Source2')
plt.ylabel('SV Precrash Speed (MPH)')

# Show the plot
plt.show()