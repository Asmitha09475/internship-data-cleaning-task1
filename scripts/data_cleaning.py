import os
import pandas as pd
import matplotlib.pyplot as plt

RAW_PATH = os.path.join('data', 'raw', 'netflix_titles.csv')
CLEAN_PATH = os.path.join('data', 'cleaned', 'netflix_cleaned.csv')
PLOT_PATH = os.path.join(os.path.dirname(__file__), 'missing_values.png')

df = pd.read_csv(RAW_PATH)

df['date_added'] = pd.to_datetime(df['date_added'], dayfirst=True, errors='coerce')
df['date_added'] = df['date_added'].ffill().bfill()
df = df.dropna(subset=['show_id', 'title', 'date_added', 'duration'])

df['director'] = df['director'].fillna('Unknown')
df['cast']     = df['cast'].fillna('Unknown')
df['country']  = df['country'].fillna('Unknown')
df['rating']   = df['rating'].fillna('Unknown')

df['duration_int'] = df['duration'].str.extract(r'(\d+)').astype(float)
median_dur = df['duration_int'].median()
df['duration_int'] = df['duration_int'].fillna(median_dur)
df['duration_unit'] = df['duration'].str.extract(r'([A-Za-z]+)').fillna('Unknown')

df = df.drop_duplicates()

for col in ['type', 'title', 'country', 'rating', 'listed_in']:
    df[col] = df[col].astype(str).str.strip().str.title()

df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')

mv = df.isnull().sum().loc[lambda x: x>0].sort_values(ascending=False)
if not mv.empty:
    plt.figure(figsize=(8,4))
    mv.plot.bar()
    plt.tight_layout()
    plt.savefig(PLOT_PATH)
    plt.show()

os.makedirs(os.path.dirname(CLEAN_PATH), exist_ok=True)
df.to_csv(CLEAN_PATH, index=False)
print("Cleaned data saved to", CLEAN_PATH)