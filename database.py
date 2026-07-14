import psycopg2
#Establishing a database connection
conn = psycopg2.connect(host='localhost',port=5432,user='postgres',password='pa55word',dbname='flask_myduka')

#creating a cursor object
cur = conn.cursor()
def get_products():
    cur.execute("select*from products")
    products = cur.fetchall()
    return products

def insert_products(product_values):
    cur.execute("insert into products(name,buying_price,selling_price)values(%s,%s,%s)",product_values)
    conn.commit()
product1 = ('Juice',100,150)
#insert_products(product1)
products = get_products()
print(products)

#Viewing data in the sales table 
def get_sales():
    cur.execute("select*from sales")
    sales = cur.fetchall()
    return sales

#inserting data into the sales table 
def insert_sales(sales_values):
    cur.execute("insert into sales(pid,quantity)values(%s,%s)",sales_values)
    conn.commit()
#sale1 = (2,20)
#insert_sales(sale1)
sales = get_sales()

print(sales)
#Viewing data into the stock table 
def get_stock():
    cur.execute("select*from stock")
    stock = cur.fetchall()
    return stock
#inserting data into the sales table 
def insert_stock(stock_values):
    cur.execute("insert into stock(pid,stock_quantity)values(%s,%s)",stock_values)
    conn.commit()
#stock1 = (2,300) 
#insert_stock(stock1)
stock = get_stock()
print(stock)

#calculating the sales per product
def sales_per_product():
    cur.execute("""
    select products.id,sum(quantity*selling_price) from products 
                inner join sales on products.id=sales.pid group by products.id
                """)
    sales_product = cur.fetchall()
    return sales_product
sales_prod = sales_per_product()
print(sales_prod)

#sales per day
def sales_per_day():
    cur.execute("""
    select date(sales.created_at) as date,sum(sales.quantity*products.selling_price) from products 
                inner join sales on products.id=sales.pid group by sales.created_at
                """)
    sales_day = cur.fetchall()
    return sales_day
sale_day = sales_per_day()
print(sale_day)

#profit per day
def profit_per_day():
   cur.execute("""
    select sales.created_at,sum(selling_price-buying_price) from products 
        inner join sales on products.id=sales.pid group by sales.created_at
        """)
   profit = cur.fetchall()
   return profit
profit_day = profit_per_day()
print(profit_day)

#profit per product
def profit_per_product():
    cur.execute("""select products.id,sum(selling_price-buying_price) from products 
        inner join sales on products.id=sales.pid group by products.id
                """)
    profit_prod = cur.fetchall()
    return profit_prod

profit_product = profit_per_product()
print(profit_product)
