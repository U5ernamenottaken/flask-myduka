import psycopg2
#Establishing a database connection
conn = psycopg2.connect(host='localhost',port=5432,user='postgres',password='pa55word',dbname='flask_myduka')

#creating a cursor object
cur = conn.cursor()
def get_products():
    cur.execute("select*from products")
    products = cur.fetchall()
    return products
products = get_products()
print(products)
def insert_products():
    cur.execute("insert into products(name,buying_price,selling_price)values('shoes','300','500')")
    conn.commit()
insert_products()
products = get_products()
print(products)
