import matplotlib.pyplot as plt
import pandas as pd

# File paths
read_csv_path = '/Users/jackyzhang/Downloads/ata_read.csv'
write_csv_path = '/Users/jackyzhang/Downloads/ata_write.csv'

# Load data from ata_write.csv
write_data = pd.read_csv(write_csv_path, names=["unix_time_sec", "unix_time_ns", "lba", "size", "entropy1", "entropy2"])

# Process ata_write.csv to extract relevant data
write_data["time_in_hours"] = (write_data["unix_time_sec"] - write_data["unix_time_sec"].min()) / 3600  # Convert UNIX time to hours
write_data["cumulative_files"] = write_data["size"].cumsum() / 4096  # Calculate cumulative number of 4KB files encrypted

# Sample data for the plot (adjust for better visualization)
sampled_data = write_data.iloc[::int(len(write_data)/10), :]  # Downsample to 10 points for readability

# Data for Figure 3: Encryption Activity Timeline
time = sampled_data["time_in_hours"]
encryption_activity = sampled_data["cumulative_files"]

# Plot Figure 3
plt.figure(figsize=(10, 6))
plt.plot(time, encryption_activity, marker='o', label='Encrypted Files Over Time', color='blue')
plt.title('Figure 2: Encryption Activity Timeline')
plt.xlabel('Time (hours)')
plt.ylabel('Number of Encrypted Files')
plt.grid(True)
plt.legend()
plt.savefig('/Users/jackyzhang/Downloads/CAPSTONE/Encryption_Activity_Timeline.png')  # Updated file path
plt.close()

# Data for Figure 4: Cost Comparisons of Ransomware Attacks
cities = ['Atlanta', 'Baltimore', 'Other Municipalities']
costs = [17, 18.2, 11.5]  # Costs in millions USD

# Plot Figure 4
plt.figure(figsize=(10, 6))
plt.bar(cities, costs, color=['blue', 'orange', 'green'])
plt.title('Figure 4: Cost Comparisons of Ransomware Attacks')
plt.xlabel('City')
plt.ylabel('Recovery Costs (in Millions USD)')
plt.savefig('/Users/jackyzhang/Downloads/CAPSTONE/Cost_Comparisons_Ransomware_Attacks.png')  # Updated file path
plt.close()

print("Figures saved successfully!")
