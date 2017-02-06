import pandas as pd

filepath = '/'
df = pd.read_csv(filepath);
df.set_index('Date', inplace=Ture);
df1 = pd.read_csv(filepath,index_col=0)

