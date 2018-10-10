---
title: "Práctica: Servidor Web Apache 2.4"
permalink: /serviciosgs/u03/practica_web_apache.html
---

**(17 tareas - 21 puntos)(8 tareas obligatorias - 11 puntos)**
{: .notice--warning}
**Muestra al profesor: Tarea 4, Tarea 9 y Tarea 13**
{: .notice--warning}

{% capture notice-text %}
* **Tarea 1 (1 punto)(Obligatorio):** Crea un escenario Vagrant con una máquina con una red pública. Instala el servidor web Apache2 en la máquina. Modifica la página index.html que viene por defecto y accede a ella desde un navegador. Entrega una captura de pantalla accediendo a ella.
{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>

## Virtual Hosting

Queremos que nuestro servidor web ofrezca dos sitios web, teniendo en cuenta lo siguiente:

1. Cada sitio web tendrá nombres distintos.
2. Cada sitio web compartirán la misma dirección IP y el mismo puerto (80).

Los dos sitios web tendrán las siguientes características:

* El nombre de dominio del primero será ``www.iesgn.org``, su directorio base será ``/srv/www/iesgn`` y contendrá una página llamada ``index.html``, donde sólo se verá una bienvenida a la página del Instituto Gonzalo Nazareno.
* En el segundo sitio vamos a crear una página donde se pondrán noticias por parte de los departamento, el nombre de este sitio será ``departamentos.iesgn.org``, y su directorio base será ``/srv/www/departamentos``. En este sitio sólo tendremos una página inicial ``index.html``, dando la bienvenida a la página de los departamentos del instituto.

{% capture notice-text %}
* **Tarea 2 (3 punto)(Obligatorio):** Configura la resolución estática en los clientes y muestra el acceso a cada una de las páginas.
{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>

## Mapeo de URL

Cambia la configuración del sitio web ``www.iesgn.org`` para que se comporte de la siguiente forma:

{% capture notice-text %}
* **Tarea 3 (1 punto)(Obligatorio):** Cuando se entre a la dirección ``www.iesgn.org`` se redireccionará automáticamente a ``www.iesgn.org/principal``, donde se mostrará el mensaje de bienvenida. En el directorio **principal** no se permite ver la lista de los ficheros, no se permite que se siga los enlaces simbólicos y no se permite negociación de contenido. Muestra al profesor el funcionamiento.
* **Tarea 4 (1 punto)(Obligatorio):** Si accedes a la página ``www.iesgn.org/principal/documentos`` se visualizarán los documentos que hay en /srv/doc. Por lo tanto se permitirá el listado de fichero y el seguimiento de enlaces simbólicos siempre que sean a ficheros o directorios cuyo dueño sea el usuario. Muestra al profesor el funcionamiento.
* **Tarea 5 (1 punto):** En todo el host virtual se debe redefinir los mensajes de error de objeto no encontrado y no permitido. Para el ello se crearan dos ficheros html dentro del directorio error. Entrega las modificaciones necesarias en la configuración y una comprobación del buen funcionamiento.
{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>


## Autentificación, Autorización, y Control de Acceso

{% capture notice-text %}
* **Tarea 6 (1 punto)(Obligatorio):** Añade al escenario Vagrant otra máquina conectada por una red interna al servidor. A la URL ``departamentos.iesgn.org/intranet`` sólo se debe tener acceso desde el cliente de la red local, y no se pueda acceder desde la anfitriona por la red pública. A la URL ``departamentos.iesgn.org/internet``, sin embargo, sólo se debe tener acceso desde la anfitriona por la red pública, y no desde la red local.
	* **Tarea 7 (1 punto):** Autentificación básica. Limita el acceso a la URL ``departamentos.iesgn.org/secreto``. Comprueba las cabeceras de los mensajes HTTP que se intercambian entre el servidor y el cliente. ¿Cómo se manda la contraseña entre el cliente y el servidor?. Entrega una breve explicación del ejercicio.
* **Tarea 8 (1 punto)(Obligatorio):** Cómo hemos visto la autentificación básica no es segura, modifica la autentificación para que sea del tipo *digest*, y sólo sea accesible a los usuarios pertenecientes al grupo *directivos*. Comprueba las cabeceras de los mensajes HTTP que se intercambian entre el servidor y el cliente. ¿Cómo funciona esta autentificación?
* **Tarea 9 (1 punto):** Vamos a combinar el control de acceso (tarea 6) y la autentificación (tareas 7 y 8), y vamos a configurar el virtual host para que se comporte de la siguiente manera: el acceso a la URL ``departamentos.iesgn.org/secreto`` se hace forma directa desde la intranet, desde la red pública te pide la autentificación. Muestra el resultado al profesor.
{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>

## Configuración con .htaccess

Date de alta en un **proveedor de hosting**. ¿Si necesitamos configurar el servidor web que han configurado los administradores del proveedor?, ¿qué podemos hacer? Explica la directiva ``AllowOverride`` de apache2. Utilizando archivos .htaccess realiza las siguientes configuraciones:

{% capture notice-text %}
* **Tarea 10 (1 punto)(Obligatorio):** Habilita el listado de ficheros en la URL  ``http://host.dominio/nas``.
* **Tarea 11 (1 punto):** Crea una redirección permanente: cuando entremos en ``ttp://host.dominio/google`` salte a ``www.google.es``.
* **Tarea 12 (1 punto):** Pedir autentificación para entrar en la URL ``http://host.dominio/prohibido``. (No la hagas si has elegido como proveedor CDMON, en la plataforma de prueba no funciona.)
{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>

## Módulos

{% capture notice-text %}
* **Tarea 13 (2 puntos)(Obligatorio):** Módulo *userdir*: Activa y configura el módulo *userdir*, que permite que cada usuario del sistema tenga la posibilidad de tener un directorio (por defecto se llama ``public_html``) donde alojar su página web. Publica una página de un usuario, y accede a la misma. Esta tarea la tienes que hacer en tu servidor.
* **Tarea 14 (2 puntos):** En tu servidor crea una carpeta ``php`` donde vamos a tener un fichero ``index.php`` con el siguiente contenido::

		<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
		<html xmlns="http://www.w3.org/1999/xhtml">
		<head>
		<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
		<title>Conversor de Monedas</title>
		</head>

		<body>
		<form action="index.php" method="get">
		   	<input type="text" size="30" name="monto" /><br/>
			<select name="pais">
				<option name="Dolar">Dolar</option>
				<option name="Libra">Libra</option>
				<option name="Yen">Yen</option>
			</select>
		    <input type="submit" value="convertir" />
		   </form>
		<?php
			// averiguamos si se ha introducido un dinero
			if (isset($_GET['monto'])) {
			  define ("cantidad", $_GET['monto']);
			} else {
		 	  define ("cantidad", 0);
			}
			if($_GET){
			// definimos los países
			$tasacambios = array ("Libra"=>0.86,"Dolar"=>1.34,"Yen"=>103.56);
			// imprimimos el monto ingresado
			echo "<b>".cantidad." euros</b><br/> ".$_GET["pais"]." = ".cantidad*$tasacambios[$_GET["pais"]]." <br><br>";
			// por cada país imprimimos el cambio
			}
		   ?>

		</body>
		</html>

	Prueba la página utilizando parámetros en la URL (parámetros GET), por ejemplo: ``http://nombre_página/php/index.php?monto=100&pais=Libra``

	Configura mediante un fichero ``.htaccess``, la posibilidad de acceder a la URL **http://nombre_página/php/moneda/cantidad**, donde moneda indica el nombre de la moneda a la que queremos convertir (Dolar,Libra,Yen) y cantidad indica los euros que queremos convertir.
{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>

## IPv6

{% capture notice-text %}
* **Tarea 15 (1 punto)**: Comprueba que el servidor web con la configuración por defecto está escuchando por el puerto 80 en ipv6.
* **Tarea 16 (1 punto)**: Configura la máquina para que tenga una ipv6 global. Activa el virtualhost por defecto y accede a la página principal utilizando la ipv6 global que tiene asignada.
* **Tarea 17 (1 punto)**: Configura la resolución estática para acceder a los virtualhost utilizando ipv6.
{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>