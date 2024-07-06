# map-my-world-bk
backend para &amp;#39;Map My World&amp;#39;, una aplicación destinada a explorar y revisar diferentes ubicaciones y categorías del mundo, como restaurantes, parques y museos.

# Requisitos
Tener instalado Python
Instalar FastAPI y uvicorn
    pip install fastapi uvicorn

# Tech
Utilizamos FastAPI para crear el API y uvicorn para correr la aplicación 

# Ejecutar aplicación localmente
En la terminal ubicarse en el root del proyecto y ejecutar 
    uvicorn main:app --reload

# Documentación
http://127.0.0.1:8000/docs
http://127.0.0.1:8000/redoc

# Cómo usar esta API?
Se utiliza DB en memoria que puede ser reemplazada por una DB como postgresql o cualquier otro motor de DB
Se crearon diferentes endpoints para habilitar features necesarias para resolver los requerimientos:

## GET /api/v1/locations
Lista todas las ubicaciones creadas en la DB

## GET /api/v1/categories
Lista todas las categorías creadas en la DB

## GET /api/v1/review
Lista las 10 sugerencias de combinaciones de ubicación y categoría para ser revisadas

## GET /api/v1/locations-and-categories
Hace una búsqueda en la DB de todas las categorías y las ubicaciones y genera los registros en DB de las combinaciones
posibles, este endpoint se crea para que se ejecute una vez al día y se actualice el listado de posibles combinaciones, 
así evitamos este procesamiento siempre que queramos procesar datos de combinaciones como en el endpoint /review

## POST /api/v1/add/location
Agregar una nueva ubicación

## POST /api/v1/add/category
Agregar una nueva categoría

## POST /api/v1/reviewed
Endpoint para hacer el registro de la combinación que ya fue revisada, este endpoint recibe el ID de la combinación que 
se revisó para actualizar el registro en la DB