---
title: "Taller 6: Almacenamiento en Kubernetes"
---

## ¿Qué vas a aprender en este taller?

* Estudiar los conceptos sobre el almacenamiento en kubernetes.
* Aprovisionamiento y solicitud de volúmenes.
* Trabajar con recursos `PersitentVolumen`.
* Trabajar con recursos `PersitentVolumenClaim`.

## ¿Qué tienes que hacer?

## Ejercicio 1: Desplegando un servidor web persistente


Siguiendo la guía explicada en el [Ejemplo 2: Gestión dinámica de volúmenes](https://github.com/josedom24/curso_kubernetes_ies/blob/main/modulo8/ejemplo2.md), vamos a crear un servidor web que permita la ejecución de scripts PHP con almacenamiento persistente.

Para realizar esta actividad vamos a usar asignación dinámica de volúmenes y puedes usar, como modelos, los ficheros del ejemplo 2.

Realiza los siguientes pasos:

1. Crea un fichero yaml para definir un recurso PersistentVolumenClaim que se llame `pvc-webserver` y para solicitar un volumen de 2Gb.
2. Crea el recurso y comprueba que se ha asociado un volumen de forma dinámica a la solicitud.
3. Crea un fichero yaml para desplegar un servidor web desde la imagen `php:7.4-apache`, asocia el volumen al Pod que se va a crear e indica el punto de montaje en el *DocumentRoot* del servidor: `/var/www/html`.
4. Despliega el servidor y crea un fichero `info.php` en `/var/www/html`, con el siguiente contenido: `<?php phpinfo(); ?>`.
5. Define y crea un Service NodePort, accede desde un navegador al fichero `info.php` y comprueba que se visualiza de forma correcta.
6. Comprobemos la persistencia: elimina el Deployment, vuelve a crearlo y vuelve a acceder desde el navegador al fichero `info.php`. ¿Se sigue visualizando?

{% capture notice-text %}
## ¿Qué tienes que entregar?

1. Pantallazo con la definición del recurso PersistentVolumenClaim.
2. Pantallazo donde se visualice los recursos `pv` y `pvc` que se han creado.
3. Pantallazo donde se vea el fichero yaml para el despliegue.
4. Pantallazo donde se vea el acceso a `info.php`.
5. Pantallazo donde se vea que se ha eliminado y se ha vuelto a crear el despliegue y se sigue sirviendo el fichero `info.php`.
{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>		
## Ejercicio 2: Haciendo persistente la aplicación GuestBook

En este ejercicio vamos a volver a desplegar nuestra aplicación GuestBook, que realizamos en el taller 4 y 5, para añadirle persistencia a la base de datos redis.

Por lo tanto necesitaremos solicitar un volumen, que se asociará de forma dinámica.

### Creando el despliegue de redis para que guarde la información en un directorio

Si estudiamos la documentación de la imagen redis en [Docker Hub](https://hub.docker.com/_/redis), para que la información de la base de datos se guarde en un directorio `/data` del contenedor hay que ejecutar con docker:

```
docker run --name some-redis -d redis redis-server --appendonly yes
```

Es decir, hay que crear el contenedor ejecutando el proceso `redis-server` con los argumentos `--appendonly yes`.

Por lo tanto tenemos que cambiar el fichero de definición del Deployment de redis, [`redis-deployment.yaml`](https://github.com/josedom24/curso_kubernetes_ies/blob/main/modulo8/files/guestbook/plantilla-redis-deployment.yaml) de la siguiente manera:

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: redis
  labels:
    app: redis
    tier: backend
spec:
  replicas: 1
  selector:
    matchLabels:
      app: redis
      tier: backend
  template:
    metadata:
      labels:
        app: redis
        tier: backend
    spec:
      volumes:
        - name: volumen-redis
          persistentVolumeClaim:
            claimName: xxxxxxxxxxxx
      containers:
        - name: contenedor-redis
          image: redis
          command: ["redis-server"]
          args: ["--appendonly", "yes"]
          ports:
            - name: redis-server
              containerPort: 6379
          volumeMounts:
            - mountPath: xxxxxxxxxxxx
              name: volumen-redis
```
Hemos usado el parámetro `command` para ejecutar el proceso, y el parámetro `args` para indicar los argumentos.

**Nota**: Los valores `xxxxxxxxxxxx` tendrás que rellenarlos durante la realización de la actividad.

### Pasos a seguir

Realiza los siguientes pasos:

1. Crea un fichero yaml para definir un recurso PersistentVolumenClaim que se llame `pvc-redis` y para solicitar un volumen de 3Gb.
2. Crea el recurso y comprueba que se ha asociado un volumen de forma dinámica a la solicitud.
3. Modifica el fichero del despliegue de redis, modificando las `xxxxxxxxxxxx` por los valores correctos: el nombre del PersistentVolumenClaim y el directorio de montaje en el contenedor (como hemos visto anteriormente es `/data`).
4. Crea el despliegue de redis. El despliegue de la aplicación `guestbook` y la creación de los Services de acceso se hace con los ficheros que ya utilizamos anteriormente: [`guestbook-deployment.yaml`](https://github.com/josedom24/curso_kubernetes_ies/blob/main/modulo8/files/guestbook/guestbook-deployment.yaml), [`guestbook-srv.yaml`](https://github.com/josedom24/curso_kubernetes_ies/blob/main/modulo8/files/guestbook/guestbook-srv.yaml) y [`redis-srv.yaml`](https://github.com/josedom24/curso_kubernetes_ies/blob/main/modulo8/files/guestbook/redis-srv.yaml).
5. Accede a la aplicación y escribe algunos mensajes.
6. Comprobemos la persistencia: elimina el despliegue de redis, vuelve a crearlo, vuelve a acceder desde el navegador y comprueba que los mensajes no se han perdido.

{% capture notice-text %}
## ¿Qué tienes que entregar?

1. Pantallazo con la definición del recurso PersistentVolumenClaim.
2. Pantallazo donde se visualicen los recursos `pv` y `pvc` que se han creado.
3. Pantallazo donde se vea el fichero yaml modificado para el despliegue de redis.
4. Pantallazo donde se vea el acceso a la aplicación con los mensajes escritos.
5. Pantallazo donde se vea que se ha eliminado y se ha vuelto a crear el despliegue de redis y que se sigue sirviendo la aplicación con los mensajes.
{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>	
## Ejercicio 3: Haciendo persistente la aplicación Nextcloud 

Esta actividad es la continuación de la actividad realizada en el taller 5.

Siguiendo la guía que hemos desarrollado en [Ejemplo 3: Wordpress con almacenamiento persistente](https://github.com/josedom24/curso_kubernetes_ies/blob/main/modulo8/wordpress.md) vamos a configurar el despliegue de Nextcloud para que use volúmenes (vamos a usar dos volúmenes, uno para la aplicación y otro para la base de datos) para que la información no se pierda.

Realiza los siguientes pasos:

1. Crea los ficheros yaml para definir los recursos PersistentVolumenClaim para solicitar dos volúmenes de 4Gb.
2. Crea esos recursos y comprueba que se ha asociado un volumen de forma dinámica a cada solicitud.
3. Modifica los ficheros de despliegue de la aplicación y la base de datos para asociar los volúmenes a cada uno. Según la documentación de la imagen [Nextcloud](https://hub.docker.com/_/nextcloud) en Docker Hub, la forma más sencilla de hacer persistente la aplicación es montar el volumen en el directorio`/var/www/html/`.
5. Accede a la aplicación, configúrala y sube un fichero.
6. Comprobemos la persistencia: elimina los despliegues, vuelve a crearlos y vuelve a acceder desde el navegador y comprueba que la aplicación está configurada y mantiene el fichero que habías subido.

{% capture notice-text %}
## ¿Qué tienes que entregar?

1. Pantallazo donde se vean los ficheros yaml modificados para los despliegues.
2. Pantallazo donde se vea el acceso a la aplicación con el fichero que has subido.
3. Pantallazo donde se vea que se han eliminado y se han vuelto a crear los despliegues y que la aplicación sigue sirviendo el fichero que habíamos subido.
{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>
