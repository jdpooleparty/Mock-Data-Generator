# Importing the missing 'string' module and re-trying the generation process

import random
import string
import pandas as pd

# Function to generate random 10-letter words

def random_word(length=10):

    return ''.join(random.choices(string.ascii_lowercase, k=length))



# Define the number of rows

num_rows = 500

# Re-create the data with the corrected setup
data = {
    "id": range(1, num_rows + 1),  # Auto-incrementing integer starting at 1
    "doc": [random_word() for _ in range(num_rows)],  # Random 10-letter words
    "pl": [random.randint(1, 3) for _ in range(num_rows)],  # Random int between 1 and 3
    "den": [round(random.uniform(1.0, 1000.0), 5) for _ in range(num_rows)],  # Random float between 1.0 and 1000.0
    "mas": [round(random.uniform(1.0, 1000.0), 5) for _ in range(num_rows)],  # Random float between 1.0 and 1000.0
    "vol": [round(random.uniform(1.0, 1000.0), 5) for _ in range(num_rows)],  # Random float between 1.0 and 1000.0
}

# Create a DataFrame
df = pd.DataFrame(data)

# Generate unique timestamp for filename
timestamp = pd.Timestamp.now().strftime('%Y%m%d_%H%M%S')

# Save to CSV with timestamp in filename
file_path = f"C:\Python-Projects\Mock Data Generator\Mock_VS_T_{timestamp}.csv"
df.to_csv(file_path, index=False)

print(f"File saved to: {file_path}")
