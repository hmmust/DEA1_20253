import json
import pandas as pd
file1= open("dea_class1.json")
students= json.load(file1)
file1.close()
print(type(students),students[0].get("name"))
students_df = pd.DataFrame(students)
print(students_df)
