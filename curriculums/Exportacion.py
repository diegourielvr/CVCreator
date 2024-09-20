from flask import render_template, send_file
from io import BytesIO
import subprocess
import tempfile
import os

def exportar(formato:str, id_plantilla, nombre_cv, datos):
    formato = formato.lower()
    nombre_plantilla = f"tex/plantilla{id_plantilla}.tex"

    if formato == "pdf":
        # return exportarPDF(nombre_plantilla, nombre_cv, datos)
        return exportarPDF(nombre_plantilla, nombre_cv, datos)

    if formato == "tex":
        return exportarTEX(nombre_plantilla, nombre_cv, datos)
        
def exportarTEX(nombre_pt, nombre_cv, datos):
    # Renderizar plantilla .tex con jinja para asignar los valores
    nuevo_archivo = render_template(nombre_pt, **datos)
    return send_file(BytesIO(nuevo_archivo.encode('utf-8')),
                     download_name=f"{nombre_cv}.tex", # Nombre del archivo (al no existir es necesario indicar uno)
                     as_attachment=True) # Descargar en lugar de mostar en el navgeador

def exportarPDF(nombre_pt, nombre_cv, datos):
    # Renderiza la plantilla .tex en memoria
    contenido_tex = render_template(nombre_pt, **datos)
    # contenido_tex = render_template(nombre_pt)

    # Crear un directorio temporal para almacenar los archivos
    with tempfile.TemporaryDirectory() as tempdir:
        # Ruta para el archivo .tex en el directorio temporal
        ruta_tex = os.path.join(tempdir, 'archivo.tex')

        # Escribir el contenido del archivo .tex en el archivo temporal
        with open(ruta_tex, 'w', encoding='utf-8') as archivo_tex:
            archivo_tex.write(contenido_tex)
            
        # Ejecutar pdflatex para generar el archivo PDF en el mismo directorio temporal
        subprocess.run(['pdflatex', '-output-directory', tempdir, ruta_tex])
        
        # Ruta para el archivo PDF generado
        ruta_pdf = os.path.join(tempdir, 'archivo.pdf')
        
         # Abrir el archivo PDF generado y cargarlo en memoria
        pdf_buffer = BytesIO()
        with open(ruta_pdf, 'rb') as archivo_pdf:
            pdf_buffer.write(archivo_pdf.read())
            
        # Volver al inicio del buffer para que pueda ser leído correctamente
        pdf_buffer.seek(0)
        
        # Enviar el archivo PDF como respuesta
        return send_file(pdf_buffer,
                         as_attachment=True,
                         download_name=f'{nombre_cv}.pdf',
                         mimetype='application/pdf')