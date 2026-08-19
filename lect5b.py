import pandas as pd
import json
import glob
conn_str= "postgresql://admin:admin@localhost:5433/fitdb"

schemas= json.load(open("retail_db/schemas.json"))
customers_schema = schemas['customers']
customers_schema=sorted(customers_schema,
                        key=lambda col:col['column_position'])
cols=  [col['column_name'] for col in customers_schema]
#FILES = ["part-00000","part-00001"]
FILES= glob.glob("retail_db/customers/*")
print(FILES)
df = []
for file in FILES:
    customers_file = pd.read_csv(file,
                              header=None,names=cols)
    df.append(customers_file)

customers= pd.concat(df,ignore_index=True)
customers.to_sql("customers3",conn_str,index=False,
                 if_exists="replace")
