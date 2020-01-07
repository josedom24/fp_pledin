
---
title: "Ejercicio 2: Comprobación de html5 válido y despliegue en surge.sh (test y deploy)"
permalink: /iawgs/u04/ejercicio2.html
---

En este ejercicio queremos desplegar una página html5 en el servicio surge.sh, además queremos comprobar si el código html5 es válido. Estas dos operaciones: comprobar si el html5 es válido (test) y el despliegue en surge.sh (deploy) lo vamos a hacer con travis de forma automática (IC y DC).

Antes de empezar vamos a aprender a trabajar con [surge.sh](http://surge.sh/):

* Siguiendo las instrucciones de esta [página](https://linuxconfig.org/how-to-install-nodejs-on-debian-9-stretch-linux) instala NodeJS y npm.
* Instala surge.sh
* Despliega una pequeña página web en el dominio `tunombre.surge.sh`.

Vamos a añadir la funcionalidad de IC y DC con travis, para ello:

* Realiza un fork del repositorio de GitHub: [https://github.com/josedom24/ic-travis-html5](https://github.com/josedom24/ic-travis-html5)
* Activa la IC en travis de tu repositorio.
* Comprueba la prueba y el despliegue que vamos a realizar estudiando el fichero `.travis.yml`.
* Modifica el fichero `.travis.yml` para poner el nombre de dominio que vas a utilizar.
* Para que travis pueda hacer el despliegue en surge le tenemos que indicar un TOKEN. Genera el token:
	
		surge token

* Crea dos variables de entorno en *settings* del proyecto travis:
	
    * `SURGE_LOGIN`: Indica el correo electrónico que has utilizado como lógin en surge
    * `SURGE_TOKEN`: Indica el TOKEN que has obtenido en el paso anterior.

* Realiza cambios en el fichero `index.html` del directorio `_build` y comprueba, que si el código html5 es válido se despliega y puedes acceder a la página web. Si el código html5 no es válido no se realiza el despliegue y te mandan un correo informando de la incidencia.

Para seguir profundizanod en la integración continúa investiga y realiza el mismo ejercicio usando [gitlab](https://about.gitlab.com/product/continuous-integration/) o [github actions](https://github.com/features/actions).
