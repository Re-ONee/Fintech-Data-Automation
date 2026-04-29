import pandas as pd
import matplotlib.pyplot as plt

# 1. Load the data
df = pd.read_csv('call_stats.csv')

# 2. Performance Analysis
df_sorted = df.sort_values(by='CSAT_Score', ascending=False)

# 3. Create the Visualization
plt.figure(figsize=(10, 6))
plt.bar(df_sorted['Agent_Name'], df_sorted['CSAT_Score'], color='skyblue')

# Add labels and a title
plt.xlabel('Agent Name', fontsize=12)
plt.ylabel('CSAT Score (%)', fontsize=12)
plt.title('Weekly Team Performance Dashboard', fontsize=14)
plt.axhline(y=85, color='red', linestyle='--', label='Target Score (85%)') # A target line
plt.legend()

# 4. Save the chart as an image
plt.savefig('team_performance.png')
print("--- Dashboard Generated: team_performance.png ---")

# 5. Security Alert (Keeping our Fraud Detection logic)
red_flags = df[(df['CSAT_Score'] >= 95) & (df['Average_Handle_Time'] < 60)]
if not red_flags.empty:
    print("\n[SECURITY ALERT] Suspicious patterns detected in FakeAgent data.")
