from flask import Blueprint, render_template

principal_bp = Blueprint(
    'principal', # Nombre del Blueprint
    __name__,  # Ruta del archivo actual
    template_folder="templates", # Carpeta de arhivos html
    static_folder="static" # Carpeta de archivos estaticos
)

@principal_bp.route("/") # Index
def index():
    return render_template('principal.html')