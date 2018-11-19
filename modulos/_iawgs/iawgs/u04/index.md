---
title: Introducción a la integración continúa y despliegue continuo
permalink: /iawgs/u04/index.html
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

* Entrega continua (EC): Es el siguiente paso de IC, y consiste en preparar la aplicación web para su puesta en producción. El paso a producción se hace de forma manual.
* Despliegue continuo (DC): Es similar a la anterior pero en este caso también se automatiza el despliegue final en producción.

**Herramientas**

* [CloudBees (jenkins)](http://www.cloudbees.com/dev)
* [Cloud Foundry](http://www.cloudfoundry.com/)
* [CircleCi](https://circleci.com/)
* [Semaphore](https://semaphoreapp.com/)
* [Travis](https://travis-ci.com/)
* [Codeship](https://www.codeship.io/)
* [tddium](https://www.solanolabs.com/)
* [Wercker](http://wercker.com/)
* [Shippable](http://www.shippable.com/)
* [Go-Ci](http://www.thoughtworks.com/products/go-continuous-delivery)
* [snap-ci](http://snap-ci.com)
* [appveyor](http://www.appveyor.com/)
* [gilab](https://about.gitlab.com/product/continuous-integration/)

## Enlaces

* [Introducción a la integración continua](https://code2read.com/2015/11/04/ci-integracion-continua-introduccion/)
* [Instalación de Jenkins en debian](http://red-orbita.com/?p=6622)
* [QUÉ ES TDD - Test-driven development](https://www.youtube.com/watch?v=q6z3jFZl8oI)

## Prácticas

* [Introducción a la integración continua](ic.html)