import pandas as pd
import random

# Define the number of rows
num_rows = 500

# Create the data
data = {
    "id": range(1111, 1111 + num_rows),  # Auto-incrementing integer starting at 1111
    "sh": [random.randint(1, 50) for _ in range(num_rows)],  # Random int between 1 and 50
    "ri": [random.randint(1, 50) for _ in range(num_rows)],  # Random int between 1 and 50
    "rity": [random.choice(['T', 'F']) for _ in range(num_rows)],  # Random char 'T' or 'F'
    "blre": [random.randint(1, 1000) for _ in range(num_rows)],  # Random int between 1 and 1000
    "re": [0 for _ in range(num_rows)],  # Fixed value 0
    "ke": [0 for _ in range(num_rows)],  # Fixed value 0
}

# Create a DataFrame
df = pd.DataFrame(data)

# Generate unique timestamp for filename
timestamp = pd.Timestamp.now().strftime('%Y%m%d_%H%M%S')

# Save to CSV with timestamp in filename
file_path = f"C:\Python-Projects\Mock Data Generator\Mock_BP_T_{timestamp}.csv"
df.to_csv(file_path, index=False)

print(f"File saved to: {file_path}")
