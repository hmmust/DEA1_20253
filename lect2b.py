import json
json_str = '{"id":10,"name":"tea", "price":1.5}'
tea= json.loads(json_str)
print(tea.get("price"))