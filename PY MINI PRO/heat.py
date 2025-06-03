import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("survey.csv")


heat_df = df[['work_interfere', 'no_employees']].dropna()


heatmap_data = pd.crosstab(heat_df['no_employees'], heat_df['work_interfere'])

plt.figure(figsize=(8, 6))
plt.imshow(heatmap_data, cmap='YlOrRd', aspect='auto')
plt.colorbar(label='Count')

plt.xticks(ticks=range(len(heatmap_data.columns)), labels=heatmap_data.columns, rotation=30)
plt.yticks(ticks=range(len(heatmap_data.index)), labels=heatmap_data.index)

plt.title("Stress Level vs Company Size")
plt.xlabel("How Mental Health Affects Work (Stress)")
plt.ylabel("Company Size")
plt.tight_layout()
plt.show()