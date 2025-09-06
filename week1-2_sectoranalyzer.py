import pandas as pd

df = pd.read_csv('bist_data.csv')
print('--- original data ---')
print(df)
print('') # for a blank line

#group by 'sector' and calculate the mean of 'market_cap_mil_tl'
#sector_means = df.groupby('sector')['market_cap_mil_tl'].mean()

#sort the results in descending order
#sector_means_sorted = sector_means.sort_values(ascending=False)##

# this is the more pro way to write it in one line
sector_means = df.groupby('sector')['market_cap_mil_tl'].mean().sort_values(ascending=False)

print('--- average market cap by sector (descending) ---')
print(sector_means)