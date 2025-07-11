import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv("snacks_sample_synthetic.csv")

# Clean it: drop any rows missing numeric values
df = df.dropna(subset=["energy_kcal_100g", "fat_100g", "sugars_100g", "proteins_100g", "nutriscore"])

# Scatter plot: Fat vs Sugars, colored by Nutri‑Score
plt.figure(figsize=(8,6))
sns.scatterplot(data=df, x="fat_100g", y="sugars_100g", hue="nutriscore", palette="viridis")
plt.title("Fat vs Sugars by Nutri-Score")
plt.xlabel("Fat (g/100g)")
plt.ylabel("Sugars (g/100g)")
plt.legend(title="Nutri-Score")
plt.show()

# Histogram: distribution of Nutri-Score grades
plt.figure(figsize=(6,4))
sns.countplot(data=df, x="nutriscore", order=["A","B","C","D","E"])
plt.title("Frequency of Nutri-Score Grades")
plt.show()


