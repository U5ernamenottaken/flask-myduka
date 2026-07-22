from flask import Flask,render_template,request,redirect,url_for
from database import get_products,get_sales,get_stock,insert_products,insert_sales,insert_stock

app = Flask(__name__)

@app.route('/')
def home():
    x = 78
    name = 'Kyle' 
    tup = ('Ericka','Alisha','Shanice')
    nums = [1,2,3,4,4,5,5,6,6]
    
    return render_template('index.html',value = x,b = name,tp = tup,nums = nums)

@app.route('/products')
def products():
    products_data = get_products()
    return render_template('products.html',products_data=products_data)

@app.route('/sales')
def sales():
    sales_data = get_sales()
    return render_template('sales.html',sales_data=sales_data)

@app.route('/stock')
def stock():
    stock_data = get_stock()
    return render_template('stock.html',stock_data=stock_data)

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/login')
def login():
    return render_template('login.html')
@app.route('/add_products',methods = ['GET','POST'])
def add_products():
 if request.method == 'POST':
     products_name = request.form['p_name']
     buying_price = request.form['b_price']
     selling_price = request.form['s_price']

     new_products = (products_name,buying_price,selling_price)
     insert_products(new_products)
     print('product adding successful')
 return redirect(url_for('products'))
@app.route('/add_sales',methods =['GET','POST'])
def add_sales():
    if request.method == 'POST':
        product_id = request.form['pid']
        quantity = request.form['quantity']
        new_sale = (product_id,quantity)
        insert_sales(new_sale)
        print('Sales added successfully')
    return redirect(url_for('sales'))
@app.route('/add_stock',methods =['GET','POST','DELETE','UPDATE'])
def add_stock():
    if request.method == 'POST':
        stock_id = request.form['stid']
        quantity = request.form['st_quantity']
        new_stock = (stock_id,quantity)
        insert_stock(new_stock)
        print('Stock added successfully')
        return redirect(url_for('stock'))
        
app.run(debug=True)
