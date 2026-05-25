import pandas as pd
import matplotlib.pyplot as plt

# Read CSV File
df = pd.read_csv(r"/home/debasis/github/dataspace_AI-ML/DAY5/students_data.csv")

# Show DataFrame
print(df)

# Plot
plt.plot(df["Hours_Studied"], df["Marks"], marker='o')

# Labels
plt.xlabel("Hours Studied")
plt.ylabel("Marks")

# Title
plt.title("Hours Studied vs Marks")

# Grid
plt.grid(True) 

# Show Plot
plt.show()
