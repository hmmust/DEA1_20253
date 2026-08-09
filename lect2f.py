import requests

r = requests.get("https://raw.githubusercontent.com/hmmust/DEA1_20253/refs/heads/main/dea_class1.json")
print(r.text)