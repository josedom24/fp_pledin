---
title: "Ejercicio 2: Instalación de la aplicación BookMedik"
---

Vamos a instala la aplicación BookMedik, un sistema para llevar el control de citas medicas, pacientes, médicos, historiales e citas, áreas medicas y mucho mas, pensado para centros médicos, clínicas y médicos independientes. Puedes encontrar la aplicación en [https://github.com/evilnapsis/bookmedik](https://github.com/evilnapsis/bookmedik).

Para realizar la instalación sigue los siguientes pasos:

1. Crea la base de datos y las tablas necesarias recuperando la copia de seguridad e la base de datos que encuentras en el fichero `schema.sql`. Se creará una base de datos llamada `bookmedik` crea un usuario que tenga privilegios sobre dicha base de datos.
2. Crea un virtualhost con el que accederas con el nombre *bookmedik.tunombre.org*. Copia en el DocumentRoot los ficheros de la aplicación (podrías clonar el repositorio en el DocumentRoot).
3. Vamos a configurar el acceso a la base de datos desde la aplicación, para ello cambia el fichero `core\controller\Database.php` indicando el usuario de acceso (el que has creado en el punto 1), su contraseña, la base de datos que se llama `bookmedik` y la dirección donde se encuentra la base de datos, que en este caso es `localhost`.
4. Accede al virtualhost usa el usuario `admin` y contraseña `admin`.

{% capture notice-text %}
## Entrega...

* Entrega una captura de la configuración del virtualhost.
* Entrega el contenido del fichero `Database.php`.
* Entrega una captura con el acceso a `bookmedik`, después del login.
{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>