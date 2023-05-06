import pandas as pd

df = pd.read_csv('criterion.csv')

# set year values to None if they are equal to '' or NaN
df['year'] = df['year'].apply(lambda x: None if x == '' or pd.isna(x) else x)

# strip whitespace from the beginning and end of the string of year
df['year'] = df['year'].str.strip()

# strip whitespace from the beginning and end of the string of BluRay_price if it is not NaN and is a string
df['BluRay_price'] = df['BluRay_price'].apply(lambda x: x.strip() if not pd.isna(x) and isinstance(x, str) else x)

df['DVD_price'] = df['DVD_price'].apply(lambda x: x.strip() if not pd.isna(x) and isinstance(x, str) else x)

# set isBluRay_available to True if BluRay_price is not NaN
df['isBluRay_available'] = df['BluRay_price'].notna()
 
# set isDVD_available to True if DVD_price is not NaN
df['isDVD_available'] = df['DVD_price'].notna()

# reorder columns
df = df[['spine', 'movie',  'director', 'media_type', 'country', 'year', 'runtime', 'isColor', 'aspect_ratio', 'language', 'isBluRay_available', 'isDVD_available',  'BluRay_price','DVD_price', 'poster_url', 'page_url', 'thumb_url']]

#save the dataframe to a csv file
df.to_csv('criterion_cleaned.csv', index=False)