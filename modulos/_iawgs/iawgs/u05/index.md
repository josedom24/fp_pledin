---
title: Introducción a la integración continúa y despliegue continuo
permalink: /iawgs/u05/index.html
---

## Objetivos

* Conocer el software de integración continúa más utilizados
* Tener una primera experiencia con travis para realizar la integración continúa (en este caso simplemente realizar de forma automática que todos los cambios en nuestra página web estática es válida)
* Despliegue manual de nuestra página en el servicio surge.sh
* Entender el concepto de despliegue continúo y comprobar la función de despliegue de travis sobre surge.sh

## Contenidos

* Integración continua: La integración continua requiere que cada vez que alguien haga un commit se construya la aplicación entera y que se ejecuten una serie de tareas automatizados: Las pruebas y el despliegue se automatizan.
* Integración continua: Práctica de desarrollo software donde los miembros del equipo integran su trabajo frecuentemente, al menos una vez al día. Cada integración se verifica con un build automático (que incluye la ejecución de pruebas) para detectar errores de integración tan pronto como sea posible.

Procesos que se realizan en la IC:

* Se recoge el código fuente de un repositorio compartido.
* Se analiza el código
* Se compila o transforma el código necesario (build)
* Se ejecutan los test (unitarios, integrales y funcionales)
* Se generan informes y documentación

Es un cambio de paradigma. Es necesario la aceptación de los miembros del equipo, puesto que la integración continua es una práctica y no una herramienta.

![IC](img/ic.png)

* **Entrega continua (EC)**: Es el siguiente paso de IC, y consiste en preparar la aplicación web para su puesta en producción. El paso a producción se hace de forma manual.
* **Despliegue continuo (DC)**: Es similar a la anterior pero en este caso también se automatiza el despliegue final en producción.

**Herramientas**

* [Jenkins](https://jenkins.io/)
* [Travis](https://travis-ci.com/)
* [gitlab](https://about.gitlab.com/product/continuous-integration/)
* [github actions](https://github.com/features/actions)
* [CircleCi](https://circleci.com/)
* ...


## Enlaces

* [Introducción a la integración continua](https://code2read.com/2015/11/04/ci-integracion-continua-introduccion/)
* [Instalación de Jenkins en debian](http://red-orbita.com/?p=6622)
* [QUÉ ES TDD - Test-driven development](https://www.youtube.com/watch?v=q6z3jFZl8oI)
* [Integración continúa, entrega continúa y despliegue continuo](https://www.youtube.com/watch?v=REMAgB7m1ig)


## Ejercicios

* [Ejercicio 1: Corrector ortográfico de documentos markdown (test)](ejercicio1.html)
* [Ejercicio 2: Comprobación de html5 válido y despliegue en surge.sh (test y deploy)](ejercicio2.html)


## Práctica

* [Práctica: Introducción a la integración continua](ic.html)
