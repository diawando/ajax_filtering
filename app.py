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
    return