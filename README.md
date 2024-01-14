# flask-sqlAlchemy-postgreSQL-api 

## Proyecto hecho con Python 3, Flask, SQLAlchemy y PostgreSQL
### Endpoints

# Products
- /products
> Devuelve todos los productos.

- /products/<int:id>
> Devuelve un producto en especifico por el id.

- /products/delete/<int:id>
> Elimina un producto en especifico por el id.

- /products/find/categories
> Devuelve todas las categorias presentes en los productos sin repetir.
method: 'GET'

- /products/add
> Agrega un producto nuevo, el cual tiene obligatorios todos sus atributos.

```
method: 'POST',
headers: {'Content-Type': 'multipart/form-data'},
body: JSON.stringify({
  title: "",
  price: 0,
  description: "",
  category: "",
  images: File   //.jpg | .jpeg | .png
})
```

## Instalación Local

Descarga el proyecto usando git
```
$ git clone https://github.com/Mirkopantufla/flask-sqlAlchemy-postgreSQL-api.git
$ cd flask-sqlAlchemy-postgreSQL-api
```


## Como se ejecuta el proyecto?

- Instala los paquetes con `$ pipenv install`.
- Debes crear el entorno virual con `pipenv shell`
- Tambien no olvides seleccionar el interprete, Ctrl + Shift + P en Windows. Entonces, escribe “Python: Select Interpreter”
- Para iniciar el backend `$ python src/app.py`


## Librerias utilizadas

- flask              : 3.0.0  [doc](https://flask.palletsprojects.com/en/3.0.x/)
- flask-cors         : 4.0.0  [doc](https://flask-cors.readthedocs.io/en/latest/)
- flask-jwt-extended : 4.6.0  [doc](https://flask-jwt-extended.readthedocs.io/en/stable/)
- flask-migrate      : 4.0.5  [doc](https://flask-migrate.readthedocs.io/en/latest/)
- flask-sqlalchemy   : 3.1.1  [doc](https://flask-sqlalchemy.palletsprojects.com/en/3.1.x/)
- SQLAlchemy         : 2.0.25 [doc](https://docs.sqlalchemy.org/en/20/)
- python-dotenv      : 1.0.0  [doc](https://pypi.org/project/python-dotenv/)
- cloudinary         : 1.37.0 [doc](https://cloudinary.com/documentation)
- psycopg2-binary    : 2.9.9  [doc](https://www.psycopg.org/docs/)


## Backend para E-commerce
https://github.com/Mirkopantufla/nextjs-tailwind-fake-store
