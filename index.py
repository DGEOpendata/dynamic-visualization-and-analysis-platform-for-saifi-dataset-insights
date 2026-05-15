python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the SAIFI dataset
data = pd.read_csv('Annual_SAIFI_2013_2025.csv')

# Display the first few rows of the dataset
print(data.head())

# Convert the 'Year' column to datetime
data['Year'] = pd.to_datetime(data['Year'], format='%Y')

# Plotting the SAIFI trends
plt.figure(figsize=(12, 6))
sns.lineplot(data=data, x='Year', y='SAIFI_Value', marker='o')
plt.title('Annual SAIFI Value Trends (2013-2025)')
plt.xlabel('Year')
plt.ylabel('SAIFI Value')
plt.grid(True)
plt.show()

# Calculate statistical metrics
mean_saifi = data['SAIFI_Value'].mean()
median_saifi = data['SAIFI_Value'].median()
std_saifi = data['SAIFI_Value'].std()

print(f"Mean SAIFI: {mean_saifi}")
print(f"Median SAIFI: {median_saifi}")
print(f"Standard Deviation of SAIFI: {std_saifi}")

# Save the summary statistics to a CSV file
summary_stats = pd.DataFrame({
    'Metric': ['Mean', 'Median', 'Standard Deviation'],
    'SAIFI_Value': [mean_saifi, median_saifi, std_saifi]
})
summary_stats.to_csv('SAIFI_Summary_Statistics.csv', index=False)
