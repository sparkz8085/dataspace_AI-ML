# File: src/main.py
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('./premier-player-23-24.csv')




# Age vs xG_90
plt.figure(figsize=(10, 6))
plt.scatter(df['Age'], df['xG_90'], alpha=0.7, s=50)
plt.title('Age vs xG_90 (Player Performance)')
plt.xlabel('Age')
plt.ylabel('xG_90')
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()



# MP by Team
team_mp = df.groupby('Team')['MP'].sum()

plt.figure(figsize=(12, 6))
team_mp.plot(kind='bar', color='lightgreen')
plt.title('Total Matches Played by Team')
plt.xlabel('Team')
plt.ylabel('Total Matches Played (MP)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()



# Position distribution
pos_count = df['Pos'].value_counts()

plt.figure(figsize=(8, 8))
pos_count.plot(kind='pie', autopct='%1.1f%%', startangle=90, colors=['gold', 'lightblue', 'lightcoral', 'lightgreen'])
plt.title('Player Position Distribution')
plt.ylabel('')  # Remove ylabel for pie chart
plt.show()
