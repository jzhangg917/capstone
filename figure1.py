import matplotlib.pyplot as plt

# Define data
timestamps = [
    "March 22, 2018 08:30 AM", "March 22, 2018 10:00 AM", "March 22, 2018 12:30 PM", 
    "March 22, 2018 03:00 PM", "March 22, 2018 05:00 PM", "March 23, 2018 06:00 AM", 
    "March 23, 2018 08:00 AM", "March 23, 2018 10:00 AM", "March 23, 2018 02:00 PM", 
    "March 23, 2018 07:00 PM", "April 1, 2018 09:00 AM", "April 5, 2018 02:00 PM", 
    "May 15, 2018 03:00 PM"
]
descriptions = [
    "Municipal employees report sluggish system performance and inability to access specific files.",
    "IT teams begin investigating system disruptions, discovering encrypted files across municipal systems.",
    "Emergency alerts are issued to city departments, advising a shutdown of potentially affected systems.",
    "IT teams confirm the attack as ransomware; encryption activity is traced to weak RDP credentials.",
    "City officials are briefed on the attack, and emergency measures are discussed.",
    "Atlanta publicly announces the ransomware attack and warns residents about disruptions in city services.",
    "Public Wi-Fi at Hartsfield-Jackson Atlanta International Airport is disabled to prevent malware spread.",
    "Key municipal systems, including police reporting and court scheduling, are declared non-operational.",
    "A crisis command center is established to coordinate recovery efforts and public communications.",
    "City leaders hold an emergency press conference to address public concerns and outline immediate response plans.",
    "City leaders announce their refusal to pay the ransom, focusing on system restoration from backups.",
    "Federal indictment of Iranian nationals responsible for the ransomware campaign is announced.",
    "Recovery costs reach $17 million; efforts continue for system restoration and upgrades."
]

# Create the figure and axis
plt.figure(figsize=(30, 6))  # Adjust the figure width for a long horizontal timeline

# Plot the timeline
for i, (timestamp, description) in enumerate(zip(timestamps, descriptions)):
    plt.scatter(i, 0, color="blue", s=100)  # Points on the timeline
    plt.text(
        i, -0.2, timestamp, rotation=45, fontsize=8, ha="right", color="purple"
    )  # Add timestamp below points
    plt.text(
        i, 0.2, description, fontsize=8, wrap=True, color="black", ha="center", va="bottom"
    )  # Add descriptions above points

# Draw a horizontal line for the timeline
plt.plot(range(len(timestamps)), [0]*len(timestamps), color="gray", linestyle="--", linewidth=1)

# Formatting
plt.title("Expanded Timeline of Atlanta Ransomware Attack", fontsize=14)
plt.yticks([])  # Remove y-axis
plt.xticks([])  # Remove x-axis ticks
plt.tight_layout()

# Save the figure
plt.savefig('/Users/jackyzhang/Downloads/Expanded_Timeline.png', dpi=300, bbox_inches="tight")
plt.close()

print("Timeline saved successfully as 'Expanded_Timeline.png'.")
