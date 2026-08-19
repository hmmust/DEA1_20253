import pandas as pd

conn_str= "postgresql://admin:admin@localhost:5433/fitdb"

customers2_df = pd.read_csv("customers2.csv")
customers2_df.to_sql("customers2",conn_str,index=False,if_exists="replace")
print(customers2_df)