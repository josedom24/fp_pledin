---
title: "Ejercicio 3: Creando un cluster de MySQL"
---

Siguiendo el [Ejemplo2: Despliegue de un cluster de MySQL](https://github.com/josedom24/curso_kubernetes_ies/blob/main/modulo9/ejemplo2.md) de esta unidad, crea un clúster de MySQL con un primario y un secundario y realiza algunas pruebas para comprobar su funcionamiento.

Realiza los siguientes pasos:

1. Crea los ficheros yaml necesarios para definir el ConfigMap, los servicios y el StatefulSet, de manera que los volúmenes asociados tengan 2GiB de tamaño y el servicio MySQL que ejecuten los secundarios se denomine `mysql-lectura`.
2. Crea un pod efímero que pueble la base de datos con la información que quieras.
3. Crea un pod efímero que consulte la base de datos del secundario.


{% capture notice-text %}
## ¿Qué tienes que entregar?

1. Pantallazo con la definición de los recursos.
2. Pantallazo donde se visualice que se han creado los pods, los servicios y los volúmenes.
3. Pantallazo donde se visualice la consulta a la base de datos.
{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>
