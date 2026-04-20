import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Load dataset
df = pd.read_csv("bitcoin.csv")

# 2. Inspect data
print(df.head())
print(df.info())
print(df.describe())
print(df.isnull().sum())

# 3. Convert date column
df['date'] = pd.to_datetime(df['date'])

# 4. Sort by date
df = df.sort_values('date')

# 5. Handle missing values
df = df.dropna()

# 6. Create new metrics
df['price_change'] = df['price'].diff()
df['volatility'] = df['price'].rolling(7).std()
df['pct_change'] = df['price'].pct_change() * 100

# 7. Charts (Exploratory)

# Price over time
plt.figure()
plt.plot(df['date'], df['price'])
plt.title("Bitcoin Price Over Time")
plt.xlabel("Date")
plt.ylabel("Price")
plt.show()

# Volume over time
plt.figure()
plt.plot(df['date'], df['total_volume'])
plt.title("Trading Volume Over Time")
plt.xlabel("Date")
plt.ylabel("Volume")
plt.show()

# Market cap over time
plt.figure()
plt.plot(df['date'], df['market_cap'])
plt.title("Market Cap Over Time")
plt.xlabel("Date")
plt.ylabel("Market Cap")
plt.show()

# Volatility
plt.figure()
plt.plot(df['date'], df['volatility'])
plt.title("Price Volatility")
plt.show()

# Histogram of price changes
plt.figure()
df['pct_change'].hist()
plt.title("Percentage Change Distribution")
plt.show()

# Scatter plot
plt.figure()
plt.scatter(df['total_volume'], df['price'])
plt.title("Volume vs Price")
plt.xlabel("Volume")
plt.ylabel("Price")
plt.show()

# Correlation heatmap
plt.figure()
sns.heatmap(df[['price','total_volume','market_cap','volatility']].corr(), annot=True)
plt.title("Correlation Heatmap")
plt.show()

# Boxplot
plt.figure()
sns.boxplot(y=df['price'])
plt.title("Price Boxplot")
plt.show()

# Rolling average
df['rolling_avg'] = df['price'].rolling(30).mean()

plt.figure()
plt.plot(df['date'], df['price'], label='Price')
plt.plot(df['date'], df['rolling_avg'], label='30 Day Avg')
plt.legend()
plt.title("Price vs Rolling Average")
plt.show()

# 8. Save cleaned dataset
df.to_csv("bitcoin_cleaned.csv", index=False)

print("Milestone 2 complete ✅")