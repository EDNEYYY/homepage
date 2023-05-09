from flask import Flask, g, render_template
from flask import jsonify


app = Flask(__name__)

#criar a 1 pagina do site
#route - www.com.br/usuarios
#função - o que vc quer exibir naquela pagina




@app.route("/homepage")
def homepage():
    return render_template("homepage.html")

@app.route("/contatos")
def contatos():
    return render_template("contatos.html")

@app.route("/usuarios")
def usuarios():
    return render_template("usuarios.html")

if __name__ == "__main__":
    app.run(debug=True)
    



