import pandas as pd

url = 'https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-states.csv'

pd.set_option('display.max_rows', None)
df = pd.read_csv(url)
