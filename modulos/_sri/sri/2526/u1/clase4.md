---
title: "Clase 4: Configuración básica de un servidor"
---

## ¿Qué vas a aprender en esta clase?

* Configurar el acceso por SHH con clave pública.
* Configuración de la herramienta `sudo`.
* Configuración del hostname y el FQDN del sistema. 

## Teoría

* **Acceso por SSH con clave pública**

    * **Objetivo:** Establecer conexión segura sin necesidad de contraseña, usando un par de claves pública/privada.
    * Pasos en el cliente (máquina desde la que te conectas):
        1. **Generar un par de claves (si no tienes):**
           ```bash
           ssh-keygen
           ```
           * Guarda por defecto en `~/.ssh/id_rsa` (clave privada) y `~/.ssh/id_rsa.pub` (clave pública).

        2. **Copiar la clave pública al servidor:**

           ```bash
           ssh-copy-id usuario@servidor
           ```

           * Alternativa manual: copiar el contenido de `~/.ssh/id_rsa.pub` al archivo `~/.ssh/authorized_keys` del usuario en el servidor.

* **Configuración de `sudo`**

    * **Objetivo:** Permitir a ciertos usuarios ejecutar comandos como superusuario (`root`) sin iniciar sesión como tal.

    * Añadir un usuario al grupo `sudo` (Debian/Ubuntu):

        1. Agregar usuario al grupo:

           ```bash
           sudo usermod -aG sudo nombre_usuario
           ```

        2. Cerrar sesión y volver a iniciar para que el cambio surta efecto.

    * Editar configuración avanzada de `sudo`:

        1. **Editar el archivo de configuración:**

           ```bash
           sudo visudo
           ```

           * Ejemplos dentro de visudo:

             ```plaintext
             nombre_usuario ALL=(ALL) NOPASSWD:ALL   # Ejecuta sudo sin contraseña
             ```

             ```plaintext
             %admin ALL=(ALL) ALL                    # El grupo "admin" puede usar sudo
             ```

        2. **Archivos adicionales:**
            * También se pueden añadir configuraciones personalizadas en `/etc/sudoers.d/`.

* Configuración del `hostname` (nombre del sistema)

    * **Objetivo:** Establecer correctamente el nombre del host para que el sistema se identifique correctamente en la red.
    * Tu máquina tendrá un nombre en tu dominio (FQDN), por ejemplo: `sauron.mordor.com`.
    * Establecer el hostname permanente:

        1. **Editar el archivo `/etc/hostname`:**

           * Contiene solo el nombre del host (una línea):

             ```plaintext
             sauron
             ```

        2. **Editar el archivo `/etc/hosts`:**

            * Para configurar de forma adecuada el FQDN crea una línea en el fichero `/etc/hosts` donde identificas el nombre completo y el nombre corto. Por ejemplo:

    	        ```
    	        127.0.1.1	sauron.mordor.com sauron
    	        ```

        3. **Aplicar el cambio sin reiniciar (temporal):**

                ```bash
                sudo hostnamectl set-hostname sauron.mordor.com
                 ```

        **Recordatorio**: `hostnamectl` cambia el hostname, pero NO actualiza `/etc/hosts`. Es responsabilidad del administrador editarlo manualmente para garantizar la resolución local del FQDN.

    * Comprobar el hostname:
        * `hostname`: Muestra el hostname.
        * `hostname -f`: Ver el nombre de dominio completo (FQDN).
        * `hostnamectl status`: Muestra todos los nombres configurados.

## Ejercicio

1. Crea una clave SSH, si no la tienes ya, y configura un servidor Linux para el acceso con el usuario `admin` con clave SSH para que no te pida la contraseña.
2. Añade el usuario `admin` al sudo para que pueda ejecutarlo sin que te pida la contraseña.
3. Configura de manera adecuada el FQDN para que sea del tipo: `servidor.tunombre.org`.

