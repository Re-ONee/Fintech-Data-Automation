import pandas as pd
import subprocess
import os

# 1. Decrypt the file temporarily using GPG
# In a real setup, you'd use a key, but for now, we use a command
print("Decrypting secure data...")
subprocess.run(["gpg", "--decrypt", "--output", "temp_stats.csv", "call_stats.csv.gpg"])

# 2. Load the data
df = pd.read_csv('temp_stats.csv')

# ... (rest of your analysis code here) ...

# 3. CRITICAL: Delete the temporary plain-text file after use
os.remove('temp_stats.csv')
print("Secure cleanup complete.")
