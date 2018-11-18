---
title: "Ejercicio: Instalación de proFTPd y uso de clientes FTP"
permalink: /serviciosgs/u05/ejercicio1.html
---

Instala el servidor proFTPd y comprueba su funcionamiento desde un cliente FTP gráfico: filezilla, y un cliente FTP de texto: ftp.

**Guía de comandos FTP**::

        Comando y argumentos	Acción que realiza
        open servidor 		Inicia una conexión con un servidor FTP.
        close o disconnect 	Finaliza una conexión FTP sin cerrar el programa cliente.
        bye o quit 		Finaliza una conexión FTP y la sesión de trabajo con el programa cliente.
        cd directorio 		Cambia el directorio de trabajo en el servidor.
        delete archivo 		Borra un archivo en el servidor
        mdelete patrón 		Borra múltiples archivos basado en un patrón que se aplica al nombre.
        dir 			Muestra el contenido del directorio en el que estamos en el servidor.
        get archivo 		Obtiene un archivo
        noop No Operation 	Se le comunica al servidor que el cliente está en modo de no operación, el servidor usualmente responde con un «ZZZ» y refresca el contador de tiempo inactivo del usuario.
        mget archivos 		Obtiene múltiples archivos
        hash 			Activa la impresión de caracteres # a medida que se transfieren archivos, a modo de barra de progreso.
        lcd directorio 		Cambia el directorio de trabajo local.
        ls 			Muestra el contenido del directorio en el servidor.
        prompt 			Activa/desactiva la confirmación por parte del usuario de la ejecución de comandos. Por ejemplo al borrar múltiples archivos.
        put archivo 		Envía un archivo al directorio activo del servidor.
        mput archivos 		Envía múltiples archivos.
        pwd 			Muestra el directorio activo en el servidor.
        rename archivo 		Cambia el nombre a un archivo en el servidor.
        rmdir directorio 	Elimina un directorio en el servidor si ese directorio está vacío.
        status 			Muestra el estado actual de la conexión.
        bin o binary 		Activa el modo de transferencia binario.
        ascii 			Activa el modo de transferencia en modo texto ASCII.
        ! 			Permite salir a línea de comandos temporalmente sin cortar la conexión. Para volver, teclear exit en la línea de comandos.
        ? nombre de comando 	Muestra la información relativa al comando.
        ? o help 		Muestra una lista de los comandos disponibles.
        append archivo 		Continua una descarga que se ha cortado previamente.
        bell 			Activa/desactiva la reproducción de un sonido cuando ha terminado cualquier proceso de transferencia de archivos.
        glob 			Activa/desactiva la visualización de nombres largos de nuestro PC.
        literal 		Con esta orden se pueden ejecutar comandos del servidor de forma remota. Para saber los disponibles se utiliza: literal help.
        mkdir 			Crea el directorio indicado de forma remota.
        quote 			Hace la misma función que literal.
        send archivo 		Envía el archivo indicado al directorio activo del servidor.
        user 			Para cambiar nuestro nombre de usuario y contraseña sin necesidad de salir de la sesión ftp.

Modifica la configuración del servidor para que los usuarios sólo puedan entrar en su directorio "Documentos".

{% capture notice-text %}
Todos los accesos al servidor FTP lo vamos a hacer utilizando su nombre, por ejemplo `ftp.iesgn.org`, por lo tanto debes configurar el servidor BIND9 en el servidor para que todos los clientes conozcan este nombre.

Siguiendo las indicación de la documentación suministrada, configura el servidor proFTPd para crear un servidor FTP anónimo de sólo lectura.

Cuando termines, aunque no sea recomendable, configura el servidor proftpd para hacerlo anónimo y de lectura y escritura.
{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>