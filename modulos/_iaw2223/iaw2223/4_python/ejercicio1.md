---
title: "Ejericio 1: Ejecución de aplicaciones python flask"
---

1. Crea una máquina en OOpenStack con la que vamos a trabajar los ejercicios y talleres de esta unidad.
2. Clona el repositorio de la aplicación [guestbook](https://github.com/josedom24/guestbook).
3. `guestbook` es una aplicación escrita en python flask. Es una aplicación donde podemos dejar guardadas mensajes en un "libro de visita". Los mensajes se van a guardar en una base de daros no relacional llamada redis. redis es una base de datos clave-valor y necesitamos instalarla:

```
apt install redis
```

	Pra más información sobre redis puedes ller este interesante artículo: [Redis, base de datos no relacional](https://www.josedomingo.org/pledin/2015/02/redis-base-de-datos-no-relacional/).

4. Crea un entorno virtual donde vamos a instalar las librerías necesarias para que funcione nuestra aplicación (fichero `requirements.txt`).
5. Ejecuta el servidor web de desarrollo ejecutando la siguientes instrucción: `python3 app.py`. Recuerda abrir el puerto 5000 en el grupo de seguridad y accede desde el navegador a la URL `http://172.22.X.X:5000`.

![guestbook](img/guestbook.png)

Si te interesa puedes ver en el código del programa cómo conectamos a redis en la dirección `127.0.0.1` en el puerto `6379`. Los mensajes se guardan en una vlace que es una lista que se llama `lista`. Puedes acceder a la base de datos y ver el contenido de esa clave:

```
$ redis-cli 
127.0.0.1:6379> lrange lista 0 -1
1) "Hola"
```

{% capture notice-text %}
En entornos de producción no se usa el servidor web de desarrollo para servir las páginas web escritas en python. En este tema vamos a estudiar la configuración de los servidores web y de los servidores de aplicación para servir páginas web python.

{% endcapture %}<div class="notice--warning">{{ notice-text | markdownify }}</div>





