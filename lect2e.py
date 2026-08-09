import pandas as pd
students_df = pd.read_parquet("dea_class1.parquet",
                              columns=["name"])
students_df = pd.read_parquet("dea_class1.parquet",
                              filters=[["age",">",21]])
print(students_df)
