import pandas as pd
students_df = pd.read_json("dea_class1.json")
students_df.rename({"Age":"age"},axis=1, inplace=True)
print(students_df)

students_df.to_json("dea_class1_cleared.json",orient="columns")
students_df.to_parquet("dea_class1.parquet",compression="snappy")