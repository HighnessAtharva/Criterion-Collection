import pandas as pd

df = pd.read_csv("../criterion.csv")

# set year values to None if they are equal to '' or NaN
df["year"] = df["year"].apply(lambda x: None if x == "" or pd.isna(x) else x)

# strip whitespace from the beginning and end of the string of year
df["year"] = df["year"].str.strip()

# strip whitespace from the beginning and end of the string of BluRay_price if it is not NaN and is a string
df["BluRay_price"] = df["BluRay_price"].apply(
    lambda x: x.strip() if not pd.isna(x) and isinstance(x, str) else x
)

df["DVD_price"] = df["DVD_price"].apply(
    lambda x: x.strip() if not pd.isna(x) and isinstance(x, str) else x
)


# set BluRay_price to 0 if it is NaN
df["BluRay_price"] = df["BluRay_price"].fillna(0)
 
# set DVD_price to 0 if it is NaN
df["DVD_price"] = df["DVD_price"].fillna(0)

# set BluRay_price to 0 if it is equal to 'Currently Unavailable'
df["BluRay_price"] = df["BluRay_price"].apply(lambda x: 0 if x == "Currently Unavailable" else x)

# set DVD_price to 0 if it is equal to 'Currently Unavailable'
df["DVD_price"] = df["DVD_price"].apply(lambda x: 0 if x == "Currently Unavailable" else x)

# set BluRay_price to -1 if it is equal to 'Out of print'
df["BluRay_price"] = df["BluRay_price"].apply(lambda x: -1 if x == "Out Of Print" else x)

# set DVD_price to -1 if it is equal to 'Out of print'
df["DVD_price"] = df["DVD_price"].apply(lambda x: -1 if x == "Out Of Print" else x)
 
# set year to -1 if it is ''
df["year"] = df["year"].apply(lambda x: -1 if x == "" else x)

# same with runtime and aspect_ratio
df["runtime"] = df["runtime"].apply(lambda x: -1 if x == "" else x)
 
df["aspect_ratio"] = df["aspect_ratio"].apply(lambda x: -1 if x == "" else x)

# set isBluRay_available to True if BluRay_price is not 0 or -1
df["isBluRay_available"] =  df["BluRay_price"].apply(lambda x: True if x != 0 and x != -1 else False)

# set isDVD_available to True if DVD_price is not NaN or 0 or -1
df["isDVD_available"] = df["DVD_price"].apply(lambda x: True if x != 0 and x != -1 else False)

# reorder columns
df = df[
    [
        "spine",
        "movie",
        "director",
        "media_type",
        "country",
        "year",
        "runtime",
        "isColor",
        "aspect_ratio",
        "language",
        "isBluRay_available",
        "isDVD_available",
        "BluRay_price",
        "DVD_price",
        "poster_url",
        "page_url",
        "thumb_url",
    ]
]

# save the dataframe to a csv file
df.to_csv("criterion_cleaned.csv", index=False)
