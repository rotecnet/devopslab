from flask import Flask

app = Flask(__name__)

csrf = CSRFProtect(app)

@app.route("/")
def pagina_inicial():
    return "Hello DevOps Rodrigo"

if __name__ == '__main__':
    app.run()