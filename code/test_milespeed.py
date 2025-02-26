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