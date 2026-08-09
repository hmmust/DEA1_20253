import pandas as pd
import pyarrow.csv as pa_csv

customers= pd.read_csv("customers.csv",sep=",",header=0)
customers= pd.read_csv("customers.csv",sep=",",header=0,
                       engine="pyarrow")
customers_table = pa_csv.read_csv("customers.csv")
customers= customers_table.to_pandas()
customers.to_csv("customers2.csv",index=False,
                 columns=['customer_id','customer_fname'])
print(customers)
