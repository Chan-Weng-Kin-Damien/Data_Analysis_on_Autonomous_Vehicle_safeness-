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

# Display the sorted DataFrame
print(c3)
total_cases = c3.groupby(level='Model Year')['count'].sum()
c3['Proportion'] = 100*(c3['count'] / c3.groupby(level='Model Year')['count'].transform('sum'))

print(c3)

# Step 3: Create a bar plot using Seaborn
g = sns.catplot(
    data=c3, kind="bar",
    x="Highest Injury Severity", y="Proportion",hue="Model Year",
    errorbar="sd", palette="dark", alpha=.6, height=6
)
g.despine(left=True)
g.set_axis_labels("Year of Model", "Percentage")
g.legend.set_title("Highest Injury Severity")
plt.show()
