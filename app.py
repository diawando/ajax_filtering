from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:lavie@localhost:5432/products"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = "supersecretkey"
db = SQLAlchemy(app)

class Produit(db.Model):
    __tablename__ = "produits"
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(70), nullable=False)
    image = db.Column(db.String(255), nullable=False)
    category = db.Column(db.String(70), nullable=False)
    price = db.Column(db.Integer, nullable=False)


@app.route('/')
def inde():
    return render_template('index.html')

@app.route("/fetchrecords",methods=["POST","GET"])
def fetchrecords():
    if request.method == 'POST':
        query = request.form['action']
        minimum_price = request.form['minimum_price']
        maximum_price = request.form['maximum_price']
        category = request.form['category']
        name = request.form['name']
        #print(query)
        if query == '':
            data = Produit.query().all
        else:
             filters = [Produit.price.between(minimum_price, maximum_price)]
             if category:
                 filters.append(Produit.category == category)
             if name:
                 filters.append(Produit.name == name)
 
             # Appliquer les filtres
             data = Produit.query.filter(*filters).all()
            
        productlist = data
    return jsonify({'htmlresponse': render_template('response.html', productlist=productlist)})
  
if __name__ == "__main__":
    app.run(debug=True)