---
title: "Ejercicio 2: Comprobación de HTML5 válido y despliegue en surge.sh (test y deploy)"
---

En este ejercicio queremos desplegar una página HTML5 en el servicio *surge.sh*, además queremos comprobar si el código HTML5 es válido. Estas dos operaciones: comprobar si el HTML5 es válido (test) y el despliegue en surge.sh (deploy) lo vamos a hacer con GitHub Actions de forma automática (IC y DC).

Antes de empezar vamos a aprender a trabajar con [surge.sh](http://surge.sh/):

* Instala surge con la instrucción: `npm install -g surge`.
* Despliega una pequeña página web en el dominio `tunombre.surge.sh`.

Vamos a añadir la funcionalidad de IC y DC con GitHub Actions, para ello:

* Realiza un fork del repositorio de GitHub: [https://github.com/josedom24/ic-html5](https://github.com/josedom24/ic-html5).
* Comprueba la prueba y el despliegue que vamos a realizar estudiando el fichero `.github/workflows\ic.yaml`.
* Modifica el fichero `.github/workflows\ic.yaml` para poner el nombre de dominio que vas a utilizar.
* Para que GiHub Actions pueda hacer el despliegue en surge le tenemos que indicar un TOKEN. Genera el token:
	
		surge token

* Crea una variable de entorno en **Settings->Secrets->Actions**:
	
    * `SURGE_TOKEN`: Indica el TOKEN que has obtenido en el paso anterior.

* Realiza cambios en el fichero `index.html` del directorio `_build` y comprueba, que si el código HTML5 es válido se despliega y puedes acceder a la página web. Si el código HTML5 no es válido no se realiza el despliegue y te mandan un correo informando de la incidencia.

