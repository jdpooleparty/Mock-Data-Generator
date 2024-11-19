# Importing the missing 'string' module and re-trying the generation process

import random
import string
import pandas as pd

# Define the number of rows for the new dataset
num_rows_large = 5000

# Create the data for 5000 rows
data = {
    "id": [random.randint(1, 10000) for _ in range(num_rows_large)],  # Random number between 0001 and 10000
    "sh": [random.randint(1, 100) for _ in range(num_rows_large)],  # Random int between 1 and 100
    "co": [random.choice(string.ascii_uppercase) for _ in range(num_rows_large)],  # Random capitalized letter
    "batch": [random.randint(2660000, 2702000) for _ in range(num_rows_large)],  # Random number between 2660000 and 2702000
    "den": [round(random.uniform(1.0, 1000.0), 5) for _ in range(num_rows_large)],  # Random float between 1.0 and 1000.0
    "mas": [round(random.uniform(1.0, 1000.0), 5) for _ in range(num_rows_large)],  # Random float between 1.0 and 1000.0
    "thi": [round(random.uniform(1.0, 1000.0), 5) for _ in range(num_rows_large)],  # Random float between 1.0 and 1000.0
    "order_id": [round(random.uniform(100000.0, 200000.0), 1) for _ in range(num_rows_large)],  # Random float between 100000.0 and 200000.0
}

# Create a DataFrame
df = pd.DataFrame(data)

# Generate unique timestamp for filename
timestamp = pd.Timestamp.now().strftime('%Y%m%d_%H%M%S')

# Save to CSV with timestamp in filename
file_path = f"C:\Python-Projects\Mock Data Generator\Mock_BS_V_{timestamp}.csv"
df.to_csv(file_path, index=False)

print(f"File saved to: {file_path}")