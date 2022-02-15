---
title: "Práctica: Kubernetes"
---

En IAW has creado dos imágenes de dos aplicaciones: guestbook (php) y polls (python django). Elige una de ellas y despliégala en kuberenetes. Para ello vamos a hacer dos ejercicios:

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
7. Entrega la url del repositorio donde están los ficheros yaml.
{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>

## Ejercicio2: Despliegue en otra distribución de kubernetes

Instala un cluster de kubernetes (más de un nodo). Tienes distintas opciones para construir un cluster de kubernetes: [Alternativas para instalación simple de k8s](https://github.com/iesgn/curso_kubernetes_cep/blob/main/modulo2/alternativas.md).

Realiza el despliegue de la aplicación en el nuevo cluster. Es posible que no tenga instalado un ingress controller, por lo que no va a funcionar el ingress (puedes buscar como hacer la instalación: por ejemplo el [nginx controller](https://kubernetes.github.io/ingress-nginx/)).

Escala la aplicación y ejecuta `kubectl get pods -o wide` para ver cómo se ejecutan en los distintos nodos del cluster.

{% capture notice-text %}
## Entrega

1. Enseña al profesor la aplicación funcionando en el nuevo cluster.
{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>