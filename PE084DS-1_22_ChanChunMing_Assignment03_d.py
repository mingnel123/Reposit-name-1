#question (d)
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Read the CSV file
data = pd.read_csv('expectancy.csv')

# Extract the columns from the DataFrame
year = data['Year']
age = data['Age']

# Perform linear regression (OLS)
slope, intercept = np.polyfit(year, age, 1)
ols_line = slope * np.array(year) + intercept

# Create the scatter plot using Seaborn
sns.scatterplot(data=data, x='Year', y='Age', label='Age Over Time')

# Plot the OLS line
plt.plot(year, ols_line, color='red', label='OLS Line')

# Set the plot labels and title
plt.xlabel('Year')
plt.ylabel('Age')
plt.title('Hong Kong Life(Age Over Time)')

# Display the plot
plt.legend()
plt.show()

