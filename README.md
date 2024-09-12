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