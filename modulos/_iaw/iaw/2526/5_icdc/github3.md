---
title: "Ejercicio 2: GitHub Actions - Comprobación de HTML5 válido y despliegue en surge.sh (test y deploy)"
---

## Introducción a surge.sh

**surge.sh** es un servicio muy sencillo para **publicar sitios web estáticos**.

Instalación de surge:

```
apt update
apt install -y nodejs npm

npm install -g surge
```

Para crear una cuenta en surge.sh:

```
surge
```

La **primera vez**:

* Te pedirá un email
* Te pedirá una contraseña
* Se crea la cuenta automáticamente

El **token** sirve para:

* Autenticación sin interacción
* Automatizar despliegues (CI/CD)
* Jenkins, GitHub Actions, etc.

Es una **clave privada**, como una contraseña. Para obtenerla:

```
surge token
```
**Guárdalo**, no se vuelve a mostrar igual.

Para publicar  una web estática (manual), desde dentro de un directorio donde tenemos una página web estática:

```bash
surge . mi-web.surge.sh
```

La web queda accesible en `https://mi-web.surge.sh`


Para publicar usando token (modo CI/CD):

```
surge ./public mi-web.surge.sh --token TU_TOKEN
```

Esto es lo que se usa en el sistema de IC/DC.

## Ejercicio

En este ejercicio queremos desplegar una página HTML5 en el servicio *surge.sh*, además queremos comprobar si el código HTML5 es válido. Estas dos operaciones: comprobar si el HTML5 es válido (test) y el despliegue en surge.sh (deploy) lo vamos a hacer con GitHub Actions de forma automática (IC y DC).

Vamos a añadir la funcionalidad de IC y DC con GitHub Actions, para ello:

* Realiza un fork del repositorio de GitHub: [https://github.com/josedom24/ic-html5](https://github.com/josedom24/ic-html5).
* Comprueba la prueba y el despliegue que vamos a realizar estudiando el fichero `.github/workflows/ic.yaml`.
* Modifica el fichero `.github/workflows/ic.yaml` para poner el nombre de dominio que vas a utilizar.
* Crea una variable de entorno en **Settings->Secrets->Actions**:
	
    * `SURGE_TOKEN`: Indica el TOKEN que has obtenido en el paso anterior.

* Realiza cambios en el fichero `index.html` del directorio `_build` y comprueba, que si el código HTML5 es válido se despliega y puedes acceder a la página web. Si el código HTML5 no es válido no se realiza el despliegue y te mandan un correo informando de la incidencia.

