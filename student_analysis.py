import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("students.csv")

# Display basic statistics
print("Average marks:\n", df.mean())
print("\nMaximum marks:\n", df.max())
print("\nMinimum marks:\n", df.min())

# Plot Maths marks
plt.bar(df['Name'], df['Maths'])
plt.title("Maths Marks of Students")
plt.xlabel("Student")
plt.ylabel("Marks")
plt.show()

# Calculate average score per student
df['Average'] = df[['Maths', 'Science', 'English']].mean(axis=1)

plt.bar(df['Name'], df['Average'])
plt.title("Average Performance of Students")
plt.xlabel("Student")
plt.ylabel("Average Marks")
plt.show()
