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
df = df0[df0['Source'] == 'AUTOMATION']


count_ADAS = df[["Model Year","Highest Injury Severity"]].value_counts()
c2 = pd.DataFrame(count_ADAS).sort_values(by="Model Year")
c3 = c2[c2.index.get_level_values('Highest Injury Severity') != 'Unknown']
severity_order = ['No Injuries Reported', 'Minor', 'Moderate', 'Serious', 'Fatality']
c3.index = c3.index.set_levels(
    [c3.index.levels[0], pd.Categorical(c3.index.levels[1], categories=severity_order, ordered=True)]
)

# Sort the DataFrame
c3 = c3.sort_index(level=['Model Year', 'Highest Injury Severity'])


# Create a linear regression plot with lmplot
sns.lmplot(
    data=c3,
    x="Model Year",
    y="Proportion",
    hue="Highest Injury Severity",
    markers="o",
    palette="dark",
    aspect=2,  # Adjust aspect ratio
    height=6   # Height of the plot
)

# Customize the plot
plt.title("Linear Regression of Proportion of Incidents by Model Year and Injury Severity")
plt.xlabel("Year of Model")
plt.ylabel("Proportion")
plt.grid()

# Show the plot
plt.show()