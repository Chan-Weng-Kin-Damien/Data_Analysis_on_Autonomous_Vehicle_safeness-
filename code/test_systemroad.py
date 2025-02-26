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

df0 = pd.concat([ADAS, ADS], ignore_index=True)
df = df0[['Source2', 'Roadway Type']]
print(df)
custom_order = ['OTHER', 'ADS', 'ADAS']
df['Source2'] = pd.Categorical(df['Source2'], categories=custom_order, ordered=True)

# Sort the DataFrame by the custom order
df = df.sort_values(by='Source2')
df = df.dropna(subset=['Roadway Type'])




count_ADAS = df[["Roadway Type"]].value_counts()
c2 = pd.DataFrame(count_ADAS)
c3 = c2[c2.index.get_level_values('Roadway Type') != 'Unknown']


# Sort the DataFrame

# Display the sorted DataFrame
print(c3)
total_cases = c3.sum()
c3['Proportion'] = 100*(c3['count'] / int(total_cases))

print(c3)

# Set up the bar chart
plt.figure(figsize=(8, 6))
sns.barplot(x='Roadway Type', y='Proportion', data=c3, palette='viridis')

# Add titles and labels
plt.title('Count of Different type of road: AUTOMATION', fontsize=16)
plt.xlabel('type', fontsize=14)
plt.ylabel('proportion', fontsize=14)

# Show the plot
plt.xticks(rotation=45)
plt.tight_layout()  # Adjust layout to prevent clipping
plt.show()

"""
# Step 3: Create a bar plot using Seaborn
g = sns.catplot(
    data=c3, kind="bar",
    x="Roadway Type", y="Proportion",hue="Source2",
    errorbar="sd", palette="dark", alpha=.6, height=6
)
g.despine(left=True)
g.set_axis_labels("Year of Model", "Percentage")
g.legend.set_title("Highest Injury Severity")
plt.show()


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
"""