import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("students.csv")

subject_avg = df[["Math", "Physics", "English"]].mean()

plt.figure(figsize=(6,4))
subject_avg.plot(kind="bar")
plt.title("Average Score per Subject")
plt.ylabel("Score")
plt.tight_layout()
plt.savefig("subject_analysis.png")

print("Chart saved successfully.")