---
title: "Taller 7: Instalación de un CMS con Helm"
---

## ¿Qué vas a aprender en este taller?

* Instalación y configuración de Helm.
* Instalación de un CMS con Helm.
* Ciclo de vida de la aplicación instalada con Helm.

## ¿Qué tienes que hacer?

Vamos a instalar el CMS Wordpress usando Helm. Para ello, realiza los siguientes pasos:

1. Instala la última versión de Helm.
2. Añade el repositorio de bitnami
3. Busca el chart de bitnami para la instalación de Wordpress. 
4. Busca la documentación del chart y comprueba los parámetros para cambiar el tipo de Service y el nombre del blog.
5. Instala el chart definiendo el tipo del Service como `NodePort` y poniendo tu nombre como nombre del blog.
6. Comprueba los Pods, ReplicaSet, Deployment y Services que se han creado.
7. Accede a la aplicación.

{% capture notice-text %}
## ¿Qué tienes que entregar?

1. Pantallazo con la búsqueda del chart con el comando `helm`.
2. Pantallazo donde se compruebe que se ha desplegado de forma correcta.
3. Pantallazo donde se vean los Pods, ReplicaSets, Deployments y Services que se han creado.
4. Pantallazo donde se vea el acceso al blog y se vea tu nombre como título del blog.
{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>		
