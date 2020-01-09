---
title: "Ejercicio 1: Corrector ortográfico de documentos markdown (test)"
permalink: /iawgs/u04/ejercicio1.html
---

Antes de comenzar date de alta en el servicio web [travis](https://travis-ci.org/) con tu cuenta de github. **Travis** nos permite hacer integración continúa en los proyectos que tenemos guardados en nuestros repositorios de GitHub.

Imaginemos que estamos escribiendo documentos markdown y lo guardamos en un repositorio de github. Queremos que cada vez que hagamos una modificación (commit - push) queremos probar (test) si tienes alguna falta de ortografía. Ese proceso lo vamos a hacer de forma automática y continua con travis. Si tenemos activada la IC en travis sobre nuestro repositorio, cada vez que hagamos un push, travis va a crear una máquina (entorno de pruebas), va a clonar nuestro repositorio y va a realizar la prueba (test) que indiquemos en el fichero `.travis.yml`. Cuando termine la prueba nos va mandar un correo informándonos si la prueba ha tenido éxito o no.

Por lo tanto realiza los siguientes pasos:

* Realiza un fork del repositorio de GitHub: [https://github.com/josedom24/ic-travis-diccionario](https://github.com/josedom24/ic-travis-diccionario).
* Activa la IC en travis de tu repositorio.
* Comprueba la prueba que vamos a realizar estudiando el fichero `.travis.yml`.
* Realiza cambios en los ficheros que están en el directorio `doc` y comprueba en travis como se van ejecutando las pruebas.

Para seguir profundizando en la integración continúa investiga y realiza el mismo ejercicio usando [gitlab](https://about.gitlab.com/product/continuous-integration/) o [github actions](https://github.com/features/actions).

