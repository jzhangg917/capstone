import matplotlib.pyplot as plt

# Data
timestamps = [
    "March 22, 2018 08:30 AM", "March 22, 2018 10:00 AM", "March 22, 2018 12:30 PM", 
    "March 22, 2018 03:00 PM", "March 22, 2018 05:00 PM", "March 23, 2018 06:00 AM", 
    "March 23, 2018 08:00 AM", "March 23, 2018 10:00 AM", "March 23, 2018 02:00 PM", 
    "March 23, 2018 07:00 PM", "April 1, 2018 09:00 AM", "April 5, 2018 02:00 PM", 
    "May 15, 2018 03:00 PM"
]

# Descriptions with six breaklines
descriptions = [
    "Municipal employees \nreport sluggish\nsystem performance \nand inability to\naccess specific files.\n\n",
    "IT teams begin \ninvestigating system \ndisruptions,\ndiscovering encrypted files\nacross municipal systems.\n\n",
    "Emergency alerts \nare issued to \ncity departments,\nadvising a shutdown of\npotentially \naffected systems.\n\n",
    "IT teams confirm \nthe attack as ransomware;\nencryption activity \nis traced to\nweak RDP credentials.\n\n",
    "City officials \nare briefed on the attack\nand emergency measures are\ndiscussed \n\nto mitigate impact.\n\n",
    "Atlanta publicly \nannounces the \nransomware attack\nand warns residents about\ndisruptions in city services.\n\n",
    "Public Wi-Fi at \nHartsfield-Jackson Atlanta\nInternational Airport disabled to\nprevent malware spread.\n\n",
    "Key municipal systems, \nincluding police\nreporting and \ncourt scheduling,\nare declared non-operational.\n\n",
    "A crisis command center \nis established\nto coordinate recovery efforts\nand manage \npublic communications.\n\n",
    "City leaders \nhold an emergency\n press conference\nto address public \nconcerns and\noutline immediate plans.\n\n",
    "City leaders \nannounce their \nrefusal to\npay the ransom\n, focusing on\nsystem restoration from backups.\n\n",
    "Federal indictment \nof Iranian nationals \nresponsible\nfor the ransomware campaign\nis announced.\n\n",
    "Recovery costs \nreach $17 million;\nefforts continue for system\nrestoration and long-term upgrades.\n\n"
]

# Prepare data for plotting
times = range(len(timestamps))  # X-axis positions

# Adjust figure size and horizontal layout
plt.figure(figsize=(50, 14))  # Extra wide and slightly taller figure
plt.scatter(times, [1] * len(timestamps), color="blue", zorder=5, s=300)  # Larger blue dots
plt.hlines(y=1, xmin=0, xmax=len(timestamps) - 1, color="gray", linestyles="solid")  # Solid timeline line

# Add labels and descriptions with closer spacing
for i, (label, desc) in enumerate(zip(timestamps, descriptions)):
    plt.text(i, 1.01, label, rotation=90, ha='center', fontsize=12, color='darkblue')  # Time labels closer to line
    plt.text(i, 0.97, desc, ha='center', fontsize=10, bbox=dict(facecolor='white', alpha=0.8, edgecolor='gray'))  # Descriptions closer to line

# Enhance overall plot appearance
plt.title("Timeline of Atlanta Ransomware Attack", fontsize=20, pad=50)
plt.axis("off")  # Turn off axes

# Save the figure
plt.savefig('/Users/jackyzhang/Downloads/CAPSTONE/figure1.png', bbox_inches="tight")
plt.close()

print("Timeline with closer events and descriptions saved!")
