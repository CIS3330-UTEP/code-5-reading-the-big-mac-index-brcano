import csv
import pandas as pd
big_mac_file = './big-mac-full-index.csv'

def load_data():
    df = pd.read_csv("big-mac-full-index.csv")
    df.columns = df.columns.str.strip().str.lower()
    df['year'] = pd.to_datetime(df['date']).dt.year
    return df

def get_big_mac_price_by_year(year, country_code):
    df = load_data()
    year = int(year)
    filtered_df = df[(df['year'] == year) & (df['iso_a3'].str.lower() == country_code.lower())]
    return round(filtered_df['dollar_price'].mean(), 2)

def get_big_mac_price_by_country(country_code):
    df = load_data()
    filtered_df = df[df['iso_a3'].str.lower() == country_code.lower()]
    return round(filtered_df['dollar_price'].mean(), 2)

def get_the_cheapest_big_mac_price_by_year(year):
    df = load_data()
    year = int(year)
    filtered_df = df[df['year'] == year]
    cheapest_row = filtered_df.loc[filtered_df['dollar_price'].idxmin()]
    return f"{cheapest_row['name']}({cheapest_row['iso_a3']}): ${round(cheapest_row['dollar_price'], 2)}"

def get_the_most_expensive_big_mac_price_by_year(year):
    df = load_data()
    year = int(year)
    filtered_df = df[df['year'] == year]
    expensive_row = filtered_df.loc[filtered_df['dollar_price'].idxmax()]
    return f"{expensive_row['name']}({expensive_row['iso_a3']}): ${round(expensive_row['dollar_price'], 2)}"

if __name__ == "__main__":
    print(get_big_mac_price_by_year(2022, "usa"))
    print(get_big_mac_price_by_country("usa"))
    print(get_the_cheapest_big_mac_price_by_year(2008))
    print(get_the_most_expensive_big_mac_price_by_year(2003))