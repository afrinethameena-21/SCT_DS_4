# Importing required libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from google.colab import files

# Load the dataset (replace 'your_file.csv' with the file path after uploading)
uploaded = files.upload()

# Reading the CSV file into a pandas DataFrame

accident_data = pd.read_csv(/content/Road_Accident_Data[1].csv)

# Convert 'Accident Date' and 'Time' columns to datetime
accident_data['Accident Date'] = pd.to_datetime(accident_data['Accident Date'], errors='coerce')
accident_data['Time'] = pd.to_datetime(accident_data['Time'], format='%H:%M', errors='coerce')

# Drop rows where 'Time' is NaT (Not a Time)
accident_data = accident_data.dropna(subset=['Time'])

# Extract hour from 'Time'
accident_data['Hour'] = accident_data['Time'].dt.hour

# Categorize accidents into time of day periods
def categorize_time_of_day(hour):
    if 6 <= hour < 12:
        return 'Morning'
    elif 12 <= hour < 18:
        return 'Afternoon'
    elif 18 <= hour < 24:
        return 'Evening'
    else:
        return 'Night'

# Apply categorization to the 'Hour' column
accident_data['Time of Day'] = accident_data['Hour'].apply(categorize_time_of_day)

# Filter necessary columns for further analysis
relevant_columns = ['Accident_Severity', 'Day_of_Week', 'Road_Surface_Conditions', 
                    'Weather_Conditions', 'Time', 'Latitude', 'Longitude']
filtered_data = accident_data[relevant_columns]

# Count of accidents per road surface condition
road_surface_count = filtered_data['Road_Surface_Conditions'].value_counts()

# Count of accidents by weather condition
weather_condition_count = filtered_data['Weather_Conditions'].value_counts()

# Visualizing road surface conditions vs accident count
plt.figure(figsize=(10, 6))
sns.barplot(x=road_surface_count.index, y=road_surface_count.values)
plt.xticks(rotation=45)
plt.title('Accidents by Road Surface Conditions')
plt.ylabel('Number of Accidents')
plt.xlabel('Road Surface Conditions')
plt.tight_layout()
plt.show()

# Visualizing accidents by weather conditions
plt.figure(figsize=(10, 6))
sns.barplot(x=weather_condition_count.index, y=weather_condition_count.values)
plt.xticks(rotation=45)
plt.title('Accidents by Weather Conditions')
plt.ylabel('Number of Accidents')
plt.xlabel('Weather Conditions')
plt.tight_layout()
plt.show()

# Visualizing accident hotspots based on Latitude and Longitude
plt.figure(figsize=(10, 8))
sns.scatterplot(data=filtered_data, x='Longitude', y='Latitude', hue='Accident_Severity', palette='coolwarm', s=10)
plt.title('Accident Hotspots by Severity')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.legend(title='Accident Severity', loc='upper right')
plt.tight_layout()
plt.show()

# Count the number of accidents for each time of day
time_of_day_count = accident_data['Time of Day'].value_counts()

# Visualize accidents by time of day using a pie chart
plt.figure(figsize=(8, 8))
plt.pie(time_of_day_count.values, labels=time_of_day_count.index, autopct='%1.1f%%', startangle=90, colors=sns.color_palette('coolwarm', n_colors=len(time_of_day_count)))
plt.title('Accidents by Time of Day')
plt.axis('equal')  # Equal aspect ratio ensures the pie chart is a circle.
plt.show()

# Analyzing the distribution of accidents by time of day (hourly)
accident_by_hour = accident_data['Hour'].value_counts().sort_index()

plt.figure(figsize=(10, 6))
sns.lineplot(x=accident_by_hour.index, y=accident_by_hour.values, marker='o')
plt.title('Accident Count by Time of Day (Hourly)')
plt.xlabel('Hour of Day')
plt.ylabel('Number of Accidents')
plt.xticks(range(0, 24))
plt.tight_layout()
plt.show()
