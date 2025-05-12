import os
import pandas as pd
import matplotlib.pyplot as plt

CLEAN_PATH = os.path.join('data', 'cleaned', 'netflix_cleaned.csv')
df = pd.read_csv(CLEAN_PATH, parse_dates=['date_added'])

mv = df.isnull().sum().loc[lambda x: x > 0].sort_values(ascending=False)
if not mv.empty:
    plt.figure(figsize=(8,4))
    mv.plot.bar()
    plt.title('Missing Values by Column')
    plt.ylabel('Count')
    plt.tight_layout()
    plt.savefig('missing_values.png')
    plt.show()
else:
    print("No missing values remain in any column.")

plt.figure()
df['duration_int'].hist(bins=30)
plt.title('Duration Distribution')
plt.xlabel('Duration (min or seasons)')
plt.ylabel('Count')
plt.tight_layout()
plt.savefig('duration_histogram.png')
plt.show()

plt.figure()
df['country'].value_counts().head(10).plot.bar()
plt.title('Top 10 Countries by Number of Shows')
plt.ylabel('Count')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig('top_countries.png')
plt.show()

df['year_added'] = df['date_added'].dt.year
plt.figure()
df['year_added'].value_counts().sort_index().plot()
plt.title('Shows Added Per Year')
plt.xlabel('Year')
plt.ylabel('Count')
plt.tight_layout()
plt.savefig('shows_per_year.png')
plt.show()

print("EDA complete. Plots saved as:\n",
      " missing_values.png\n",
      " duration_histogram.png\n",
      " top_countries.png\n",
      " shows_per_year.png")
