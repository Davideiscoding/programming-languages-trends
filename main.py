import pandas as pd
import matplotlib.pyplot as plt

# Getting the data
df = pd.read_csv("QueryResults.csv", names=["DATE", "TAG", "POSTS"], header=0)

# Formatting the date from string to datetime
df.DATE = pd.to_datetime(df.DATE)

# Reshape df with pivot to display one language per column
reshaped_df = df.pivot(index="DATE", columns="TAG", values="POSTS")

# Replaces any NaN value as 0
reshaped_df.fillna(0, inplace=True)

# Visualize data with Matplotlib

roll_df = reshaped_df.rolling(window=6).mean()

plt.figure(figsize=(16,20))
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.xlabel('Date', fontsize=14)
plt.ylabel('Number of Posts', fontsize=14)
plt.ylim(0, 35000)

for column in roll_df.columns:
    plt.plot(roll_df.index, roll_df[column],
             linewidth=2, label=roll_df[column].name)
plt.legend(fontsize=16)
plt.show()

