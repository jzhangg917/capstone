import matplotlib.pyplot as plt

# Data for the timeline
events = [
    {"time": "March 22, 2018 08:30 AM", "event": "Municipal employees report sluggish system performance and inability to access specific files."},
    {"time": "March 22, 2018 10:00 AM", "event": "IT teams begin investigating system disruptions, discovering encrypted files across municipal systems."},
    {"time": "March 22, 2018 12:30 PM", "event": "Emergency alerts are issued to city departments, advising a shutdown of potentially affected systems."},
    {"time": "March 22, 2018 03:00 PM", "event": "IT teams confirm the attack as ransomware; encryption activity traced to weak RDP credentials."},
    {"time": "March 22, 2018 05:00 PM", "event": "City officials are briefed on the attack, and emergency measures are discussed."},
    {"time": "March 23, 2018 06:00 AM", "event": "Atlanta publicly announces the ransomware attack and warns residents about disruptions in city services."},
    {"time": "March 23, 2018 08:00 AM", "event": "Public Wi-Fi at Atlanta International Airport disabled to prevent malware spread."},
    {"time": "March 23, 2018 10:00 AM", "event": "Key municipal systems, including police reporting and court scheduling, are declared non-operational."},
    {"time": "March 23, 2018 02:00 PM", "event": "A crisis command center is established to coordinate recovery efforts and public communications."},
    {"time": "March 23, 2018 07:00 PM", "event": "City leaders hold an emergency press conference to address public concerns."},
    {"time": "April 1, 2018 09:00 AM", "event": "City leaders announce their refusal to pay the ransom and shift focus to recovery."},
    {"time": "April 5, 2018 02:00 PM", "event": "Federal indictment of Iranian nationals linked to SamSam ransomware campaign."},
    {"time": "May 15, 2018 03:00 PM", "event": "Recovery costs reach $17 million; efforts continue for system restoration and upgrades."},
]

# Prepare data for plotting
times = range(len(events))  # X-axis positions
labels = [event["time"] for event in events]
descriptions = [event["event"] for event in events]

# Adjust figure size for full horizontal expansion
plt.figure(figsize=(30, 6))  # Adjust figure size for wide layout
plt.scatter(times, [1] * len(events), color="blue", zorder=5, s=200)  # Scatter plot for points
plt.hlines(y=1, xmin=0, xmax=len(events) - 1, color="gray", linestyles="dashed")  # Connect points

# Add labels and descriptions with appropriate spacing
for i, (label, desc) in enumerate(zip(labels, descriptions)):
    plt.text(i, 1.05, label, rotation=90, ha='center', fontsize=10, color='darkblue')  # Rotate time labels
    plt.text(i, 0.8, desc, ha='center', wrap=True, fontsize=9, bbox=dict(facecolor='white', alpha=0.8, edgecolor='gray'))  # Event descriptions

# Enhance overall plot appearance
plt.title("Expanded Timeline of Atlanta Ransomware Attack", fontsize=18, pad=30)
plt.axis("off")  # Turn off axes

# Save the figure
plt.savefig('/Users/jackyzhang/Downloads/CAPSTONE/Expanded_Timeline_Filled.png', bbox_inches="tight")
plt.close()

print("Timeline expanded horizontally and saved!")
