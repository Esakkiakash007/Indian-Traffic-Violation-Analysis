import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("final_cleaned.csv")
print(df.head())
print(df.shape)
print(df.info())
print(df.isnull().sum())
print(df.duplicated().sum())

top_fines = df.groupby(
    'Violation_Type'
)['Fine_Amount'].mean().sort_values(
    ascending=False
).head(10)

top_fines.plot(
    kind='bar'
)

plt.title(
    'Average Fine by Violation Type'
)

plt.show()

age_group = df.groupby(
    'Driver_Age'
).size()

age_group.plot(
    kind='bar'
)

plt.title(
    'Driver Age Distribution'
)

plt.xlabel(
    'Driver Age'
)

plt.ylabel(
    'Number of Violations'
)

plt.show()

avg_speed = df.groupby(
    'Vehicle_Type'
)['Recorded_Speed'].mean().sort_values(
    ascending=False
)

avg_speed.plot(
    kind='bar'
)

plt.title(
    'Average Speed by Vehicle Type'
)

plt.xlabel(
    'Vehicle Type'
)

plt.ylabel(
    'Average Speed'
)

plt.show()

weather_fine = df.groupby(
    'Weather_Condition'
)['Fine_Amount'].mean().sort_values(
    ascending=False
)

weather_fine.plot(
    kind='bar'
)

plt.title(
    'Average Fine by Weather Condition'
)

plt.xlabel(
    'Weather Condition'
)

plt.ylabel(
    'Average Fine'
)

plt.show()


numeric_df = df.select_dtypes(
    include='number'
)

plt.figure(
    figsize=(12,8)
)

monthly = df.groupby('Month').size()
monthly.plot(kind='bar')

plt.title('Monthly Violations')
plt.xlabel('Month')
plt.ylabel('Number of Violations')

plt.show()

import matplotlib.pyplot as plt

df['Driver_Gender'].value_counts().plot(
    kind='pie',
    autopct='%1.1f%%'
)

plt.title(
    'Violations by Gender'
)

plt.ylabel('')

plt.show()

df['Vehicle_Type'].value_counts().plot(
    kind='bar'
)

plt.title('Violations by Vehicle Type')
plt.xlabel('Vehicle Type')
plt.ylabel('Number of Violations')

plt.show()

df.to_csv("final_cleaned.csv", index=False)