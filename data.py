import pandas as pd

# Read the csv file in
df = pd.read_csv('Resources/cities.csv')

# Save to file
df.to_html('Data.html', index=False)

# Assign to string
table = df.to_html()
print(table)
