from flask import Flask,render_template,request
from flask.json import jsonify
from flask_mongoengine import MongoEngine, json
from mongoengine.fields import IntField, StringField




app=Flask(__name__)
app.config['MONGODB_SETTINGS'] = {
    'db': 'POS',
    'host': 'localhost',
    'port': 27017
} 

db=MongoEngine()
db.init_app(app)

class product(db.Document):
    pid=IntField()
    pname=StringField()
    price=IntField()
    stock=IntField()
    def to_json(self):
        return {
            "pid":self.pid,
            "pname":self.pname,
            "price":self.price,
            "stock":self.stock            
        }
#Route : DB Initialize
@app.route('/api/dbinit')
def dbinit():
    p1=product(pid=1,pname="apple",price=5,stock=50)
    p2=product(pid=2,pname="chai",price=5,stock=50)
    p3=product(pid=3,pname="change",price=5,stock=50)
    p1.save()
    p2.save()
    p3.save()
    return jsonify([p1,p2,p3])
#Get JSON
#POST
@app.route('/api/products',methods=["GET","POST"])
def products():
    if request.method=="GET":        
        products=product.objects
        return jsonify(products)
    else:
        #POST    
        #print('post')    
        dataReceived=request.json
        p1=product(pid=dataReceived['pid'],
                   pname=dataReceived['pname'],
                   price=dataReceived['price'],stock=dataReceived['stock'])
        p1.save()
        return p1.to_json()
#Get(ID)

@app.route('/api/products/<id>',methods=["GET","PUT","DELETE"])
def productApi(id):
    if request.method=="Get":           
        products=product.objects(pid=id)    
        return jsonify(products)
    elif request.method=="PUT":#Update
        dataReceived=request.json
        p=product.objects(pid=id).first()
        p.update(pname=dataReceived['pname'],price=dataReceived['price'],stock=dataReceived['stock'])
        return {"data":"Product Updated Successfully"};
    else:#Delete
        p=product.objects(pid=id).first()
        p.delete()
        return p.to_json()
        
#POST - Insert

#PUT - EDIT

#Delete 
        
    
    

        

@app.route('/')
def home():
    return "<h1>Welcom to POS Web API!</h1>"

app.run(debug=True,port=7000)