
import json

student= {"name":"Ammar Omari",'Age':22, "Married":False}
ammar= json.dumps(student)
print(type(ammar))
ammar = '{"name": "Ammar Omari", "Age": 22, "Married": false}'
print(ammar)