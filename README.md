# CVCreator

## Como instalar

1. **Clonar el repositorio**

```bash
git https://github.com/diegourielvr/CVCreator.git
```

2. **Entrar a la carpeta**

```bash
cd CVCreator
```

3. **Crear y activar entorno virtual**

```bash
python -m venv .venv
```
- En windows:

```bash
.\.venv\Scripts\activate
```
- En Unix:

```bash
source .venv/bin/activate
```


4. **Instalar dependencias**

```bash
pip install -r requirements.txt
```
- Instalar MikTeX

https://miktex.org/howto/install-miktex


## Configurar base de datos

1. **Ejecutar instrucciones de schema.sql**
- Desde MySql Workbench o desde terminal

## Cambiar informacion de la bd

1. Cambiar usuario y contraseña

- Modificar ConectorDBAutenticacion.py y ConectorDBCurriculums.py

## Ejecución

1. Ejecutar app.py

```bash
python app.py
```

## Añadir plantillas .tex

Para añadir o crear una plantilla .tex, es recomendable utilizar bloques [raw](https://jinja.palletsprojects.com/en/3.1.x/templates/#escaping). Los bloques marcados con {% raw %} y {% endraw%} serán omitidos por jinja, dentro de este espacio se debe colocar el código de la plantilla. tex. 

### Problemas

1. LaTeX Error: There's no line here to end

Se debe a que uno o más saltos de linea (lineas en blanco) antes o despues de \\begin{tabular} estan presentes y esto causa problemas al momento de compilar a pdf con pdflatex.
Solución: Mover los bloques {% raw %} y {% endraw %} a un lugar donde no generen saltos de linea.

- Ejemplo:
```tex
    \section*{\large Skills}{% endraw %}{% for habilidad in habilidades %}{% raw %} % Aquí no se generan saltos de linea
    \subsection*{\small {% endraw %}{{ habilidad.nombre }}{% raw %}}
    \begin{tabularx}{\textwidth}{cY}
        % Dentro de \tabular se pueden dejar saltos de linea y no deberia afectar
        {% endraw %}{% for subhabilidad in habilidad.subhabilidades %}{% raw %}
        \tiny{\faChevronRight}        & {% endraw %}{{ subhabilidad }}{% raw %} \\
        {% endraw %}{% endfor %}{% raw %}
    \end{tabularx}{% endraw %}{% endfor %}{% raw %} % Aquí tampoco se generan saltos de linea
```