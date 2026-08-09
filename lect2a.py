import json
student= {"name":"Ammar Omari",'Age':22, "Married":False}
students = [
    {"name":"Ammar Omari",'Age':22},
    {"name":"Abdullah Ahamd",'Age':21},
    {"name":"Shaker Zaid",'Age':21},
    {"name":"Hashem Saleh",'Age':22}
]
file1= open("dea_class1.json",mode="wt")
json.dump(students,file1)
file1.close()
