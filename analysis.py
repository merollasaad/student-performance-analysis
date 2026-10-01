import pandas as pd

# Load dataset
df = pd.read_csv("students.csv")

# Calculate average score
df["Average"] = df[["Math", "Physics", "English"]].mean(axis=1)

# Top student
top_student = df.loc[df["Average"].idxmax()]

print("Top Student:")
print(top_student)

print("\nOverall Average:")
print(df["Average"].mean())

print("\nSubject Averages:")
print(df[["Math", "Physics", "English"]].mean())

# Save processed data
df.to_csv("processed_students.csv", index=False)