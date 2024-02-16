---
title: "Taller 5: Despliegues parametrizados"
---

## ¿Qué vas a aprender en este taller?

* Configuración de aplicaciones usando variables de entorno.
* Gestionar el recurso ConfigMap.
* Gestionar el recurso Secrets.

## ¿Qué tienes que hacer?

## Ejercicio 1: Configurando nuestra aplicación Temperaturas 

En un ejemplo anterior: [Ejemplo completo: Desplegando y accediendo a la aplicación Temperaturas](https://github.com/josedom24/curso_kubernetes_ies/blob/main/modulo6/temperaturas.md) habíamos desplegado una aplicación formada por dos microservicios que nos permitía visualizar las temperaturas de municipios.

Recordamos que el componente `frontend` hace peticiones al componente `backend` utilizando el nombre `temperaturas-backend`, que es el nombre que asignamos al Service ClusterIP para el acceso al `backend`.

Vamos a cambiar la configuración de la aplicación para indicar otro nombre.

Podemos configurar el nombre del servidor `backend` al que vamos acceder desde el `frontend` modificando la variable de entorno **TEMP_SERVER** a la hora de crear el despliegue del `frontend`.

Por defecto el valor de esa variable es:

```
TEMP_SERVER temperaturas-backend:5000
```

Vamos a modificar esta variable en el despliegue del `frontend` y cambiaremos el nombre del Service del `backend` para que coincidan, para ello realiza los siguientes pasos:

1. Crea un recurso `ConfigMap` con un dato que tenga como clave `SERVIDOR_TEMPERATURAS` y como contenido `servidor-temperaturas:5000`.
2. Modifica el fichero de despliegue del `frontend`: [`frontend-deployment.yaml`](https://github.com/josedom24/curso_kubernetes_ies/blob/main/modulo6/files/temperaturas/frontend-deployment.yaml) para añadir la modificación de la variable `TEMP_SERVER` con el valor que hemos guardado en el `ConfigMap`.
3. Realiza el despliegue y crea el Service para acceder al `frontend`.
4. Despliega el microservicio `backend`.
5. Modifica el fichero [`backend-srv.yaml`](https://github.com/josedom24/curso_kubernetes_ies/blob/main/modulo6/files/temperaturas/backend-srv.yaml) para cambiar el nombre del Service por `servidor-temperaturas` y crea el Service.
6. Accede a la aplicación usando el puerto asignado al Service NodePort del `frontend` o creando el recurso `Ingress`.

{% capture notice-text %}
## ¿Qué tienes que entregar?

1. Pantallazo donde se vea la definición del recurso `ConfigMap`.
2. Pantallazo donde se vea la modificación del fichero `frontend-deployment.yaml`.
3. Pantallazo donde se vea la modificación del fichero `backend-srv.yaml`.
4. Pantallazo donde se compruebe que la aplicación está funcionando.
{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>		
## Ejercicio 2: Despliegue y acceso de la aplicación Nextcloud

Basándonos en el [Ejemplo completo: Despliegue y acceso a Wordpress + MariaDB](https://github.com/josedom24/curso_kubernetes_ies/blob/main/modulo7/wordpress.md) vamos a realizar el despliegue de la aplicación NextCloud + MariaDB. Para ello ten en cuenta lo siguiente:

* El despliegue de la base de datos se haría de la misma forma que encontramos en el ejemplo de Wordpress, pero para esta actividad vamos a usar la imagen `mariadb:10.5`.
* Según la documentación de [NextCloud en DockerHub](https://hub.docker.com/_/nextcloud) las variables de entorno que tienes que modificar serían: `MYSQL_DATABASE`, `MYSQL_USER`, `MYSQL_PASSWORD` y `MYSQL_HOST`.
* Al igual que en el ejemplo utiliza un recurso ConfigMap para guardar los valores de configuración no sensibles, y un recurso Secret para los datos sensibles.
* Utiliza los ficheros yaml del ejemplo haciendo las modificaciones oportunas.


{% capture notice-text %}
## ¿Qué tienes que entregar?

1. Pantallazo donde se vea el contenido del fichero de despliegue de NextCloud.
2. Pantallazo donde se vean los recursos que se han creado.
3. Pantallazo donde se compruebe que la aplicación está funcionando.
{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>	
