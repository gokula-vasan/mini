import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("survey.csv")

# Filter valid age and drop missing condition data
df = df[df['Age'].between(18, 65)]
df = df.dropna(subset=['Age', 'treatment'])

# Group data by treatment status
treatment_groups = [df[df['treatment'] == status]['Age'] for status in df['treatment'].unique()]

# Plot box plot
plt.figure(figsize=(8, 6))
plt.boxplot(treatment_groups, labels=df['treatment'].unique())

plt.title("Age vs Mental Health Treatment")
plt.xlabel("Treatment Status")
plt.ylabel("Age")
plt.tight_layout()
plt.show()
