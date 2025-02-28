import pandas as pd

# Define the Excel file path
file_path = "C:/Users/lrcoo/Downloads/AmesHousing.xlsx"

# Read the Excel file
df = pd.read_excel(file_path)

# Display the first few rows
print(df.head())

