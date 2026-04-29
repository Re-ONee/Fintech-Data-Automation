import pandas as pd

# 1.Load the data
df = pd.read_csv('call_stats.csv')

# 2.Sort agents by CSAT_Score (Customer Satisfaction)
top_performers = df.sort_values(by='CSAT_Score', ascending=False).head(2)
struggling_performers = df.sort_values(by='CSAT_Score', ascending=True).head(2)

# New -- Fraud/Anomaly Detection --
# Flag anyone with 95+ Score but less than 60 seconds handle time
red_flags = df[(df['CSAT_Score'] >= 95) & (df['Average_Handle_Time'] < 60)]

# 3. Print the results to the terminal
print("--- TOP PERFORMERS THIS WEEK ---")
print(top_performers[['Agent_Name', 'CSAT_Score']])

print("\n--- SECURITY ALERT: SUSPICIOUS ACTIVITY ---")
if not red_flags.empty:
	print("WARNING: The following agents show unnautural patterns:")
	print(red_flags[['Agent_Name', 'CSAT_Score', 'Average_Handle_Time']])
else:
	print("No suspicious patterns dected")

