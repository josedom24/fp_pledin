---
title: Introducción a la integración continúa, entrega continúa y despliegue continúo
---

* **Integración continua**: La integración continua requiere que cada vez que alguien haga un commit se construya la aplicación entera y que se ejecuten una serie de tareas automatizados: Las pruebas y el despliegue se automatizan.
* **Integración continua**: Práctica de desarrollo software donde los miembros del equipo integran su trabajo frecuentemente, al menos una vez al día. Cada integración se verifica con un build automático (que incluye la ejecución de pruebas) para detectar errores de integración tan pronto como sea posible.

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
