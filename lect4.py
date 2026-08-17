import pandas as pd

conn_str= "postgresql://admin:admin@localhost:5433/fitdb"

sales = pd.read_sql_query(
    "select distinct order_status from orders order by 1",
    conn_str)

print(sales)
