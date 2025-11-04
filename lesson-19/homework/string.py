import pandas as pd
url='https://raw.githubusercontent.com/IslomovSH/python-homework/refs/heads/main/lesson-19/homework/task/sales_data.csv'
sales=pd.read_csv(url)
groups=sales.groupby("Category")
groups.size()

#You are given a dataset containing sales data for an e-commerce website. The dataset (task\sales_data.csv) has
#the following columns:


#Group the data by the Category column and calculate the following aggregate statistics for each category:
#Total quantity sold.
#Average price per unit.
#Maximum quantity sold in a single transaction.
groups.get_group('Clothing')
groups.agg(
    total_quantity=('Quantity', 'sum'),
    average_price=('Price', 'mean'),
    max_quantity=('Quantity', 'max')
)

#Identify the top-selling product in each category based on the total quantity sold
top_products=sales.loc[groups['Quantity'].idxmax()]
top_products

#Find the date on which the highest total sales (quantity * price) occurred.
#Eng baland sotuv sodir bo'lgan kunni toping

sales['Total_sales']=sales['Quantity']*sales['Price']
daily_sales=sales.groupby('Date')['Total sales'].sum()
daily_sales

#Homework Assignment 2: Examining Customer Orders
import pandas as pd
url='https://raw.githubusercontent.com/IslomovSH/python-homework/refs/heads/main/lesson-19/homework/task/customer_orders.csv'
cust_orders=pd.read_csv(url)

#Group the data by CustomerID and filter out customers who have made less than 20 orders.
custs=cust_orders.groupby('CustomerID').filter(lambda x: len(x)>=20)
print(custs)

#Identify customers who have ordered products with an average price per unit greater than $120.

avg_price_per_cust=cust_orders.groupby('CustomerID')['Price'].mean()
high_price_than120=avg_price_per_cust[avg_price_per_cust>120]
print(high_price_than120)

#Find the total quantity and total price for each product ordered, and filter out products that have a
#total quantity less than 5 units.

result=(cust_orders.groupby('Product').agg(
    total_quantity=('Quantity', 'sum'),
    total_price=('Quantity', lambda x: (x*cust_orders.loc[x.index, 'Price']).sum())
))

result=result[result['total_quantity']>=5]
print(result)

import sqlite3
import pandas as pd

conn=sqlite3.connect(r"task/population.db")
# Bazadagi barcha jadvallarni ko‘rsatish
query = "SELECT name FROM sqlite_master WHERE type='table';"
tables = pd.read_sql(query, conn)
print(tables)


# population jadvalidagi barcha ma'lumotni Pandas DataFrame ga o‘qish
df = pd.read_sql("SELECT * FROM population", conn)

# Natijani ko‘rish
print(df.head())



