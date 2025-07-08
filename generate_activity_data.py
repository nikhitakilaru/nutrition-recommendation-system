import pandas as pd
import numpy as np

df = pd.read_csv('data/food_activity.csv')

# Strip all column names to avoid hidden spaces
df.columns = [col.strip() for col in df.columns]

# Add columns if missing
if 'ActivityMinutes' not in df.columns:
    df['ActivityMinutes'] = np.random.randint(10, 60, size=len(df))
if 'SedentaryMinutes' not in df.columns:
    df['SedentaryMinutes'] = np.random.randint(300, 800, size=len(df))

df.to_csv('data/food_activity.csv', index=False)
print("✅ Activity data added!")
