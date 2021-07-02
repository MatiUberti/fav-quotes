from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

#CONFIGURAMOS QUE LA APP SE CONECTE CON LA BASE DE DATOS NUEVA DE POSTGRESQL
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql+psycopg2://postgres:Mamoncito1880@localhost/quotes"
#ESTO ES PARA CONECTAR A HEROKU
#app.config["SQLALCHEMY_DATABASE_URI"] = "postgres://gvlibuoplxhuzn:d9755325b86ee6b43515722191571d61042f1c3dfce80f9a72ce9e953647cf5e@ec2-52-1-20-236.compute-1.amazonaws.com:5432/d31ag9q0c6rarm"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]= False #ESTO ES PARA QUE NO GENERE GASTO DE RAM A DOPE

db = SQLAlchemy(app)

class FavQuotes(db.Model):   #ARMAMOS UNA CLASE PARA CREAR LA TABLA QUE VAMOS A USAR
    id = db.Column(db.Integer, primary_key=True)     #ACA DEFINIMOS LAS 3 COLUMNAS CON SU TIPO DE DATO Y NRO DE CARACTERES QUE AGUANTE
    author = db.Column(db.String(30))
    quotes = db.Column(db.String(2000))

@app.route("/")   #CADA APP.ROUTE VA A SER EL URL DE CADA PANTALLA DE NUESTRA WEB
def index(): #aca definimos nuestra home
    result = FavQuotes.query.all()   #AGREGAMOS ESTA VARIABLE QUE RECUPERA DATOS DE LA BASE DE DATOS
    return render_template("index.html", result = result) #LA AGREGAMOS ACA TMB EN RESULT

@app.route("/quotes")
def quotes():
    return render_template("quotes.html")

@app.route("/process", methods=["POST"])
def process():
    author = request.form["author"] #ESTO ES PARA QUE RECUPERE LO QUE INGRESE EL USUARIO EN EL FORM
    quote = request.form["quote"]
    quotedata = FavQuotes(author = author, quotes = quote)
    db.session.add(quotedata)
    db.session.commit()
    return redirect(url_for("index")) #DESPUES DE RECUPERAR ESOS DATOS NOS REDIRIGE A LA FUNCION INDEX TRANSFORMADA