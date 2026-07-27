from flask import Flask,render_template,request,redirect,url_for,flash
from database import get_products,get_sales,get_stock,insert_products,insert_sales,insert_stock,check_available_stock,profit_per_day,profit_per_product,sales_per_day,sales_per_product,insert_user,check_exiting_user



app = Flask(__name__)

app.secret_key = "#L3ssthan#0_0mu$hr00m$"

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
    products_data = get_products()
    return render_template('sales.html',sales_data=sales_data,products_data=products_data)

@app.route('/stock')
def stock():
    stock_data = get_stock()
    products_data = get_products()
    return render_template('stock.html',stock_data=stock_data,products_data=products_data)

@app.route('/dashboard')
def dashboard():
    sales_product = sales_per_product()
    sales_day = sales_per_day()

    product_profit = profit_per_product()
    profit_day = profit_per_day()

    product_names = [i[0] for i in sales_product]
    p_sales = [float(i[1]) for i in sales_product]
    p_profit = [float(i[1]) for i in product_profit]

    dates = [str(i[0]) for i in sales_day]
    d_sales = [float(i[1]) for i in sales_day]
    d_profit = [float(i[1]) for i in product_profit]

    return render_template('dashboard.html',sales_product=sales_product,sales_day=sales_day,product_profit=product_profit,
                           profit_day=profit_day,product_names=product_names,p_sales=p_sales,p_profit=p_profit,
                           dates=dates,d_sales=d_sales,d_profit=d_profit)

@app.route('/register',methods = ['POST','GET'])
def register():
    if request.methods == 'POST':
        full_name = request.form['name']
        email =request.form['email']
        phone_number =request.form['phone']
        password =request.form['password']

    existing_user = check_exiting_user(email)

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
        available_stock = check_available_stock(product_id)

        if float(quantity)>available_stock:
            flash("Insufficient stock","danger")
            return redirect(url_for('sales'))

        new_sale = (product_id,quantity)
        insert_sales(new_sale)
        flash("Sale added successfully","success")
    return redirect(url_for('sales'))
@app.route('/add_stock',methods =['GET','POST','DELETE','UPDATE'])
def add_stock():
    if request.method == 'POST':
        stock_id = request.form['stid']
        quantity = request.form['st_quantity']
        new_stock = (stock_id,quantity)
        insert_stock(new_stock)
        flash("Stock added successfully","success")
        return redirect(url_for('stock'))
        
app.run(debug=True)
