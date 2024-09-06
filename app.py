from flask import Flask
from principal.routes import principal_bp
from autenticacion.routes import autenticacion_bp
from curriculums.routes import curriculums_bp

app = Flask(__name__) # Crear el servidor

app.secret_key = "iamasecretkey"

app.register_blueprint(principal_bp) # '/'
app.register_blueprint(autenticacion_bp, url_prefix='/autenticacion') # '/'
app.register_blueprint(curriculums_bp, url_prefix='/curriculums') # '/'

@app.route("/test")
def test():
    return "<h1>Este es un test</h1>"

if __name__ == "__main__":
    app.run(debug=True) # Ejecutar el servidor y recargar al hacer cambios