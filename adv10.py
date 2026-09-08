#dataframe
import pandas as pd

# Create a dataset
data = {
    "Name": ["John", "Alice", "Bob", "David", "Emma"],
    "Marks": [75, 85, 60, 90, 70],
    "Attendance": [80, 90, 75, 95, 85]
}

# Load data into a DataFrame
df = pd.DataFrame(data)

# Display the DataFrame
print("Dataset:")
print(df)

# Display basic information
print("\nInformation:")
print(df.info())

# Display basic statistics
print("\nBasic Statistics:")
print(df.describe())

# Add a new column based on existing columns
df["Final Score"] = df["Marks"] * 0.8 + df["Attendance"] * 0.2

print("\nDataFrame after adding Final Score:")
print(df)

