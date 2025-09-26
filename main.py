from flask import Flask, render_template

app = Flask(__name__)

#criar 1° página do site
# route
# função -> o uqe voçê quer exibir no site
##Pagina inicial
@app.route("/")
def Homepage():
    return render_template("homepage.html")

##Pagina contatos
@app.route("/contatos")
def Contatos():
    return render_template("contatos.html")

##pagina usuarios
@app.route("/usuarios/<nome_usuario>")
def usuarios(nome_usuario):
    return render_template("usuarios.html", nome_usuario=nome_usuario)

#colocar o site no ar
if __name__ == "__main__":
    app.run(debug=True)