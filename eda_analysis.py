import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("sales_data.csv")

print("Dataset Information")
print(df.info())

print("\nStatistical Summary")
print(df.describe())

print("\nMissing Values")
print(df.isnull().sum())

correlation = df[['Sales','Profit']].corr()

print("\nCorrelation Matrix")
print(correlation)

sns.heatmap(correlation,
            annot=True,
            cmap='Blues')

plt.title("Sales vs Profit Correlation")
plt.show()

sns.barplot(x='Category',
            y='Sales',
            data=df)

plt.title("Sales by Category")
plt.show()
