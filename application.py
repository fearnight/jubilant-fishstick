from flask import Flask
import redis
import os

app = Flask(__name__)

# CONCEPTO CLAVE DE DEVOPS: 
# Nos conectamos al host llamado 'redis-db'. 
# Docker se encargará de traducir ese nombre a una IP interna automáticamente.
cache = redis.Redis(host='redis-db', port=6379)

@app.route('/')
def index():
    # la base de datos puede tardar un tiempo en arrancar por lo que intenta conectarse varias veces para darle tiempo
    retries = 5
    while True:
        try:
            # Incrementamos el contador en la base de datos
            count = cache.incr('visitas')
            break
        except redis.exceptions.ConnectionError as exc:
            if retries == 0:
                raise exc
            retries -= 1
    
    # Aquí devolvemos tu HTML pero con el dato dinámico inyectado
    return f"""
    <html>
        <body style="background-color: blue;">
            <h1>Hola mundo! Pipeline funcionando con Docker</h1>
            <h2>Esta página ha sido vista {count} veces.</h2>
            <p>(Este dato viene de una base de datos Redis)</p>
        </body>
    </html>
    """

if __name__ == "__main__":
    #flask solo escucha en el contenedor interno de ahi esa ip
    app.run(host="0.0.0.0", port=5000)