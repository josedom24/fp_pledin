---
title: "Taller 1: Trabajando con Pods"
---

## ¿Qué vas a aprender en este taller?

* Definición de pod.
* Describir un pod con fichero yaml.
* Gestionar el ciclo de vida de un pod.

## ¿Qué tienes que hacer?

Vamos a crear nuestro primer Pod, y para ellos vamos a desplegar una
imagen que nos ofrece un servidor web con una página estática. Para
ello realiza los siguientes pasos:

1. Crea un fichero yaml con la descripción del recurso Pod, teniendo en cuenta los siguientes aspectos:
    * Indica nombres distintos para el Pod y para el contenedor.
    * La imagen que debes desplegar es `iesgn/test_web:latest`.
    * Indica una etiqueta en la descripción del Pod.
2. Crea el Pod.
3. Comprueba que el Pod se ha creado y está corriendo.
4. Obtén información detallada del Pod creado.
5. Accede de forma interactiva al Pod y comprueba los ficheros que están en el DocumentRoot (`usr/local/apache2/htdocs/`).
6. Crea una redirección con `kubectl port-forward` utilizando el puerto de localhost 8888 y sabiendo que el Pod ofrece el servicio en el puerto 80. Accede a la aplicación desde un navegador.
7. Muestra los logs del Pod y comprueba que se visualizan los logs de los accesos que hemos realizado en el punto anterior.
8. Elimina el Pod, y comprueba que ha sido eliminado.

{% capture notice-text %}
## ¿Qué tienes que entregar?

1. Pantallazo del fichero yaml que has creado con la definición del Pod.
2. Pantallazo donde se comprueba que el Pod ha sido creado.
3. Pantallazo donde se ve la información detallada del Pod.
4. Pantallazo donde se ve el fichero `index.html` del DocumentRoot.
5. Pantallazo del navegador accediendo a la aplicación con el `port-forward`.
6. Pantallazo donde se ve los logs de acceso del Pod.

{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>		
