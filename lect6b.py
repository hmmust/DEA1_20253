import pandas as pd

products_df = pd.read_csv("products.csv")
# head, tail, sample
print(products_df.head())
print(products_df.tail(10))
print(products_df.sample(10))
random_products = products_df.sample(10)
print(random_products)
print(products_df.dtypes)
print(products_df.info())
print(products_df.describe())
print(products_df.describe(include="object"))