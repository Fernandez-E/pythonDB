import pandas as pd
import sqlite3

# create dataframe
data = pd.DataFrame({
    'ID': [1, 2, 3, 4],
    'Name': ['Alice', 'Bob', 'Charlie', 'David']
})

# database connection
conn = sqlite3.connect('mydatabase.db')

data.to_sql('Cliente', conn, if_exists='replace', index=False)

conn.close()
