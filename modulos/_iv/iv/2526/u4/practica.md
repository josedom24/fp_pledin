---
title: "Práctica: Kubernetes"
---

Vas a trabajar con la imagen que has generado en IAW: o la Biblioteca (php) o la imagen polls (python django). Con cualquiera de las dos tienes que usar el despliegue con una base de datos mariadb. Realiza el despliegue en kubernetes. Para ello vamos a hacer dos ejercicios:

## Ejercicio1: Despliegue en minikube

Escribe los ficheros yaml que te posibilitan desplegar la aplicación en minikube. Recuerda que la base de datos debe tener un volumen para hacerla persistente. Debes crear ficheros para los deployments, services, ingress, volúmenes,...

Despliega la aplicación en minikube.

{% capture notice-text %}
## Entrega

1. Salida de los comando que nos posibilitan ver los recursos que has creado en el cluster.
2. Pantallazo accediendo a la aplicación utilizando el servicio.
3. Pantallazo accediendo a la aplicación utilizando el ingress.
4. Elimina el despliegue de la base datos, vuelve a crearla y comprueba que la aplicación no ha perdido los datos.
5. Escala la aplicación con 3 replicas. Muestra la salida oportuna para ver los pods que se han creado.
6. Modifica la aplicación, vuelve a crear una imagen con la nueva versión y actualiza el despliegue. No te olvide de anotar la modificación. Muestra la salida del historial de despliegue, la salida de `kubectl get all` y un pantallazo donde se vea la modificación que has realizado.
7. Entrega un zip con los ficheros yaml. Si has declarado algún ConfigMap o Secret sin definir en un fichero indica la instrucción para su creación.
8. Entrega un vídeo para donde expliques lo que has hecho en el ejercicio y sirva de prueba de funcionamiento.
{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>

## Ejercicio2: Despliegue en otra distribución de kubernetes

Instala un clúster de kubernetes (más de un nodo). Tienes distintas opciones para construir un cluster de kubernetes: [Alternativas para instalación simple de k8s](https://github.com/josedom24/curso_kubernetes_ies/blob/main/modulo2/alternativas.md).

Realiza el despliegue de la aplicación en el nuevo clúster. Es posible que no tenga instalado un ingress controller, por lo que no va a funcionar el ingress (puedes buscar como hacer la instalación: por ejemplo el [nginx controller](https://kubernetes.github.io/ingress-nginx/)).

Escala la aplicación y ejecuta `kubectl get pods -o wide` para ver cómo se ejecutan en los distintos nodos del clúster.

{% capture notice-text %}
## Entrega

1. Escribe un pequeño tutorial explicando la configuración que has realizado para instalar un clúster multinodo de k8s.
2. Muestra la salida del comando `kubectl get pods -o wide` después de hacer el escalado.
3. Entrega un vídeo para donde expliques lo que has hecho en el ejercicio y sirva de prueba de funcionamiento.
{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>