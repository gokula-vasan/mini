
import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("survey.csv")  # Replace with your dataset path

# Preprocess: Drop missing values in relevant columns
df = df[['mental_health_interview', 'treatment']].dropna()

# Create a grouped count
grouped = df.groupby(['mental_health_interview', 'treatment']).size().unstack()

# Plotting
grouped.plot(kind='bar', figsize=(8, 6), colormap='Set2')

plt.title("Support at Interview vs Treatment Need")
plt.xlabel("Support from Employer During Interview")
plt.ylabel("Number of Respondents")
plt.xticks(rotation=20)
plt.legend(title='Received Treatment')
plt.tight_layout()
plt.show()
