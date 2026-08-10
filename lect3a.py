import requests
import pandas as pd
from io import StringIO

res = requests.get("https://raw.githubusercontent.com/hmmust/DEA1_20253/refs/heads/main/customers.csv")
if res:
    class1 = pd.read_csv(StringIO(res.text))
    print(class1)
else:
    print("File not found")