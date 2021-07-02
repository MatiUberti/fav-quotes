from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")   #CADA APP.ROUTE VA A SER EL URL DE CADA PANTALLA DE NUESTRA WEB
def index(): #aca definimos nuestra home
    fruits = ["apple", "banana", "orange", "grape"] #ACA CARGAMOS UNA LISTA QUE VA A PODER USARSE EN EL HTML
    return render_template("Index.html", quote= "Soy Willy Polvoron", fruits=fruits) #ACA INSERTAMOS TODO EL HTML QUE VA A IR EN NUESTRA PAG, EN ESTE CASO EL INDEX o home
                                        #podemos definir variables que podemos usar en el html que usemos
                                        #tmb le cargamos la lista con un nombre de variable
@app.route("/about")
def about():
    return "<h1>Soy mati</h1>" #PODEMOS ESCRIBIR TODO EL HTML ACA TMB

@app.route("/quotes")
def quotes():
    return "<h1>La vida es una sucesion de asados</h1>"