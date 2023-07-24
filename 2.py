import time

import pandas as pd
import requests

df = pd.read_csv('ISSTA23.csv')
count = 0
for i in range(46, df.shape[0]):
    content = requests.get(df.loc[i, 'PDF']).content
    with open(f'pdf/{i}.pdf', 'wb') as f:
        f.write(content)
    print(df.loc[i, "标题"])

    count += 1
    if count % 10 == 0:
        time.sleep(30)