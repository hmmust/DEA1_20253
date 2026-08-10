import requests
import pandas as pd
res = requests.get("https://raw.githubusercontent.com/hmmust/DEA1_20253/refs/heads/main/dea_class1.json")
#if r.status_code ==200:
if res:
    #print(res.text)
    #print(res.json())
    class1 = pd.DataFrame(res.json())
    print(class1)
    #print(res.status_code)
    #print(res.content)
else:
    print("File not found")