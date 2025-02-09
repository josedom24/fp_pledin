---
title: "Taller 2: Trabajando con ReplicaSet"
---

## ¿Qué vas a aprender en este taller?

* Definición de un ReplicaSet.
* Describir un ReplicaSet con fichero yaml.
* Gestionar el ciclo de vida de un ReplicaSet.

## ¿Qué tienes que hacer?

Como indicamos en el contenido de este módulo, no se va  a trabajar directamente con los Pods (realmente tampoco vamos a trabajar directamente con los ReplicaSet, en el siguiente módulo explicaremos los Deployments que serán el recurso con el que trabajaremos).  En este ejercicio vamos a crear un ReplicaSet que va a controlar un conjunto de Pods. Para ello, realiza los siguientes pasos:

1. Crea un fichero yaml con la descripción del recurso ReplicaSet, teniendo en cuenta los siguientes aspectos:
    * Indica nombres distintos para el ReplicaSet y para el contenedor de los Pods que va a controlar.
    * El ReplicaSet va a crear 3 réplicas.
    * La imagen que debes desplegar es `iesgn/test_web:latest`.
    * Indica de manera adecuada una etiqueta en la especificación del Pod que vas a definir que coincida con el *selector* del ReplicaSet.
2. Crea el ReplicaSet.
3. Comprueba que se ha creado el ReplicaSet y los 3 Pods.
4. Obtén información detallada del ReplicaSet creado.
5. Vamos a probar la tolerancia a fallos: Elimina uno de los 3 Pods, y comprueba que inmediatamente se ha vuelto a crear un nuevo Pod.
6. Vamos a comprobar la escalabilidad: escala el ReplicaSet para tener 6 Pods de la aplicación.
7. Elimina el ReplicaSet y comprueba que se han borrado todos los Pods.

{% capture notice-text %}
## ¿Qué tienes que entregar?

1. Pantallazo del fichero yaml que has creado con la definición del ReplicaSet.
2. Pantallazo donde se comprueba que el ReplicaSet y los 3 Pods se han creado.
3. Pantallazo donde se ve la información detallada del ReplicaSet.
4. Pantallazo donde se ven los Pods que se han creado, después de eliminar uno de ellos.
5. Pantallazo donde se ven los Pods que se han creado después del escalado.

{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>		
