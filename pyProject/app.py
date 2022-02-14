#Using Flask Web Framework Module
from flask import Flask,render_template,request
import mysql.connector
from werkzeug.utils import redirect

#Connection Object
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="112233",
  database="northwind"
)

#Create Flask Application
app=Flask(__name__)

#Build Site URLS - Routes - API - Pages
#Site/index = Function - Method - Controller Action
@app.route('/about')
def about():
    return render_template('about.html')
@app.route('/base')
def base():
    return render_template('base.html')

@app.route('/base2')
def base2():
    return render_template('base2.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/')
def home():
    return render_template('home.html')

#CRUD Routes Actions
#database Functions
def getProducts():
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM products")
    products = mycursor.fetchall()
    return products

def getProductsByName(pname):
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM products where productname like '"+pname + "%'")
    products = mycursor.fetchall()
    return products

#Routes - Action - URLS - Pages
#Select - Read
@app.route('/products',methods=["GET","POST"])
def products():
    productsmodel=[]
    if request.method=="GET":
        productsmodel=getProducts()
    else:
        pname=request.form["pname"]
        productsmodel=getProductsByName(pname)
    return render_template('products.html',products=productsmodel)


#Insert Data
def InsertProduct(pname,uprice,stock):
    mycursor = mydb.cursor()
    sql = f"INSERT INTO Products (ProductName, UnitPrice,UnitsInStock) VALUES ('{pname}', {uprice},{stock})"
    mycursor.execute(sql)
    mydb.commit()
 

  
@app.route('/newproduct',methods=["GET","POST"])
def newproduct():
    if request.method=="GET":        
        return render_template('newproduct.html')
    else:
        #Post
        p= request.form["pname"]
        pr= request.form["price"]
        s= request.form["stock"]
        InsertProduct(p,pr,s)
        return redirect("products")

def UpdateProduct(pid,pname,uprice,stock):
    mycursor = mydb.cursor()
    sql = f"update Products Set ProductName='{pname}', UnitPrice={uprice},UnitsInStock={stock} where Productid={pid}"
    mycursor.execute(sql)
    mydb.commit()
    
def SearchProductByID(pid):
    mycursor = mydb.cursor()
    sql = f"Select * from Products where Productid={pid}"
    mycursor.execute(sql)
    product = mycursor.fetchone()
    return product

def DeleteProductByID(pid):
    mycursor = mydb.cursor()
    sql = f"Delete from Products where Productid={pid}"
    mycursor.execute(sql)

@app.route('/editproduct/<id>',methods=["GET","POST"])
def editproduct(id):
    if request.method=="GET":
        editProduct=SearchProductByID(id)        
        return render_template('editproduct.html',product=editProduct)
    else:
        pname=request.form["pname"]
        price=request.form["price"]
        stock=request.form["stock"]
        UpdateProduct(id,pname,price,stock)
        return redirect("/products")

def DeleteProductByID(pid):
    mycursor = mydb.cursor()
    sql = f"Delete from Products where Productid={pid}"
    mycursor.execute(sql)
    mydb.commit()

    
@app.route('/deleteproduct/<id>',methods=["GET","POST"])
def deleteproduct(id):
    if request.method=="GET":    
        deletedProduct=SearchProductByID(id)        
        return render_template('deleteproduct.html',product=deletedProduct)
    else:#POST - Confirm
        DeleteProductByID(id)
        return redirect('/products')
        

#Start Web Server App(Back End App)
app.run(debug=True,port=1000)