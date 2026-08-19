import pandas as pd

conn_str= "postgresql://admin:admin@localhost:5433/fitdb"

sales = pd.read_sql_query(
    "select distinct order_status from orders order by 1",
    conn_str)
customers_df = pd.read_sql("customers",conn_str)
print(customers_df)
