import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

csv_path = Path(__file__).parent / "email_spam_dataset (1).csv"
df = pd.read_csv(csv_path)

sns.set_theme(style="whitegrid")

fig, axes = plt.subplots(2, 3, figsize=(12, 7))
fig.suptitle("Email Spam Dataset ", fontsize=22, fontweight="bold")

# 1. Spam vs Ham
sns.countplot(x="label", data=df, palette="Set2", ax=axes[0,0])
axes[0,0].set_title("Spam vs Ham")

# 2. Word Count
sns.histplot(df["word_count"], kde=True, color="royalblue", ax=axes[0,1])
axes[0,1].set_title("Word Count Distribution")

# 3. Capital Words
sns.histplot(df["num_capital_words"], kde=True, color="orange", ax=axes[0,2])
axes[0,2].set_title("Capital Words")

# 4. Money Words
sns.countplot(x="has_money_words", hue="label", data=df, palette="Set2", ax=axes[1,0])
axes[1,0].set_title("Money Words")

# 5. Urgent Words
sns.countplot(x="has_urgent_words", hue="label", data=df, palette="coolwarm", ax=axes[1,1])
axes[1,1].set_title("Urgent Words")

# 6. Links
sns.countplot(x="has_link_words", hue="label", data=df, palette="viridis", ax=axes[1,2])
axes[1,2].set_title("Link Words")

plt.tight_layout()
plt.savefig("email_spam_graph.png")
plt.show()
