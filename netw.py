from bs4 import BeautifulSoup
import requests
import pandas as pd

url = 'https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue'
page = requests.get(url)

soup = BeautifulSoup(page.text, 'html.parser')

table = soup.find('table', class_ = 'wikitable sortable')

tableh = table.find_all('th')
headers = [th.get_text(strip=True) for th in tableh]

df = pd.DataFrame(columns=headers)

rows = table.find_all('tr')[1:]

for row in rows:
    cells = row.find_all('td')
    row_data = [cell.get_text(strip=True) for cell in cells] #We cleaning cells

    #Add row to df
    if row_data:
        df.loc[len(df)] = row_data
df.to_csv(r'~/companies.csv', index=False)