---
title: "Clase 1: Introducción a ansible"
---

## ¿Qué vas a aprender en esta clase?

* El concepto de infraestructura como código.
* El concepto de Software de gestión de la configuración (CMS)
* Para qué sirve ansible y vamos a comenzar a trabajar con este software.

## Teoría

**Infraestructura como Código (IaC)** es la práctica de **definir y gestionar la infraestructura de TI (servidores, redes, bases de datos, etc.) mediante archivos de configuración legibles por máquina**, en lugar de configurarla manualmente. Dos tipos de programas:

* **Software de Orquestación**: Nos permiten **programar la creación de escenarios**. Por ejemplo: **vagrant**.
* **Software de gestión de la configuración (CMS)**: Nos permiten **programar la gestión de la configuración que va a tener los servidores**. Por ejemplo, **ansible**.

**Ansible** es una herramienta de **gestión de configuración y automatización** que permite definir, en archivos de texto (YAML), el estado deseado de servidores y aplicaciones, y aplicarlo sin necesidad de instalar agentes en los nodos (usa SSH). Nos permite: configurar servidores, desplegar aplicaciones, orquestar tareas en múltiples máquinas,...


## Recursos

* [Presentación: Infraestructura como código. Ansible y Vagrant](https://fp.josedomingo.org/sri/pdf/iac.pdf). 

## Ejercicio

1. Realiza la instalación de ansible. Puedes usar los repositorios oficiales de Debian, o realizar una instalación con `pip` en un entorno virtual python.
2. Crea una máquina virtual que vamos a configurar con ansible. Esta máquina debe tener las siguientes características:

    * Debe tener creado un usuario sin privilegios con el que podamos acceder a la máquina usando claves ssh. 
    * Debe tener instalado `sudo` y el usuario que estamos usando para acceder debe estar configurado para poder usar `sudo` sin que le pida la contraseña.

3. El **inventario** es el fichero donde definimos los equipos que vamos a configurar. Crea un directorio y dentro un fichero llamado `hosts`, con el siguiente contenido:

    ```
    all:
      children:
        servidores:
          hosts:
            nodo1: 
              ansible_ssh_host: 
              ansible_ssh_user:  
              ansible_ssh_private_key_file: 
    ```


    En el inventario se clasifican los equipos por grupos:

    * El grupo `all` (se puede llamar como queráis, pero se suele llamar de esta forma) corresponde a todos los equipos definidos.
    * En este ejemplo hemos creado un grupo `servidores`, donde hemos definido nuestra máquina.
    * A la máquina la hemos llamado `nodo1` (**cambia el nombre y pon el de tu máquina**), además **debes rellenar la siguiente información del nodo**:
        * `ansible_ssh_host`: Dirección IP del equipo que queremos configurar.
        * `ansible_ssh_user`: Usuario sin privilegios con el que vamos a acceder por ssh (lo hemos creado en el equipo en el punto 2).
        * `ansible_ssh_private_key_file`: Fichero con la clave privada que vamos a usar para el acceso.

4. Vamos a crear un **fichero de configuración**, en el directorio crearemos un fichero llamado `ansible.cfg`, con el siguiente contenido:

    ``` 
    [defaults]
    inventory = hosts
    host_key_checking = False
    ``` 
    Donde **ponemos el nombre del fichero de inventario en el parámetro `inventory`** y el parámetro `host_key_checking = False`, que impide que se haga la comprobación del equipo cada vez que se hace la conexión ssh.

5. Vamos a comprobar si tenemos conectividad con el nodo. Para ello vamos a usar el módulo `ping` de ansible. Un **módulo de ansible** me permite ejecutar una acción en un servidor remoto o en un conjunto de servidores.
    
    Ejecuta alguna de estas instrucciones:

    * `ansible all -m ping`: Comprueba la conectividad con **todos** los equipos del inventario.
    * `ansible servidores -m ping`: Comprueba la conectividad con  los equipos del **grupo servidores**.
    * `ansible nodo1 -m ping`: Comprueba la conectividad con el equipo **nodo1** (Cambia el nombre con el que has configurado en el fichero).
    
    Debe salir el mensaje "pong" en verde.

6. Hay muchos módulos que podemos usar ([All modules](https://docs.ansible.com/ansible/2.9/modules/list_of_all_modules.html)). Veamos algún ejemplo:

    * **command**: Ejecutas comandos en el nodo remoto o en un conjunto de nodos. Con `-a` indicamos los **parámetros del módulo**, en este caso indicamos la instrucción a ejecutar. 

        Por ejemplo, para ejecutar `uptime` en todos los nodos.

          ansible all -m command -a "uptime"
          
        El módulo **shell** es igual que `command`, pero permite redirecciones, pipes y variables, y que usa una shell. Por ejemplo:
        
          ansible all -m shell -a "echo $HOME | wc -c"
          
    * **copy**: Permite copiar ficheros desde nuestro ordenador al nodo remoto o grupo de nodos. Los parámetros principales son:
          * `src`: archivo origen en el nodo de control.
          * `dest`: ruta de destino en el nodo remoto.
          * `mode`: permisos opcionales.

        Ejemplo:

          ansible all -m copy -a "src=./index.html dest=/tmp/index.html mode=0644"
          
        [Documentación de copy](https://docs.ansible.com/ansible/2.9/modules/copy_module.html#copy-module)

    * **file**: Gestiona archivos, directorios y permisos. Parámetros principales:
        * `path`: ruta del archivo/directorio en el nodo remoto.
          * `state`: qué debe existir (`file`, `directory`, `absent`, `link`).
          * `mode`: permisos.
    
        Ejemplo, crea un directorio: 

          ansible all -m file -a "path=/tmp/ansible_demo state=directory mode=0755"
          

        [Documentación de file](https://docs.ansible.com/ansible/2.9/modules/file_module.html#file-module)

    * **apt**: Instala, actualiza o elimina paquetes. Parámetros principales:
        * `name`: paquete a instalar.
          * `state`: `present` (instalado), `absent` (eliminado), `latest` (última versión).

        Ejemplo, instalamos el servidor web Apache:

          ansible nodo1 -m apt -a "name=apache2 state=present" --become
          
        `--become` se utiliza para que la acción se ejecute como `root` en la máquina remota.	
    
        [Documentación de apt](https://docs.ansible.com/ansible/2.9/modules/apt_module.html#apt-module)

    * **service**: Gestiona servicios del sistema. Parámetros principales:

        * `name`: nombre del servicio.
          * `state`: `started`, `stopped`, `restarted`, `reloaded`.
          * `enabled`: `yes`/`no` (si debe arrancar con el sistema).

        Ejemplo, iniciar el servidor apache2:

          ansible nodo1 -m service -a "name=apache2 state=started enabled=yes" --become
          
        [Documentación de service](https://docs.ansible.com/ansible/2.9/modules/service_module.html#service-module)

    * **user**: Crea, modifica o elimina usuarios. Parámetros principales:

        * `name`: nombre del usuario.
          * `state`: `present` (crear/asegurar que existe), `absent` (eliminar).
          * `shell`: shell por defecto.
          * `groups`: grupos a los que pertenece.

        Ejemplo, creación de un usuario:

          ansible all -m user -a "name=demo shell=/bin/bash groups=sudo state=present" --become
          

        [Documentación de user](https://docs.ansible.com/ansible/2.9/modules/user_module.html#user-module)

4. Realmente no estamos usando un esquema **imperativo** (por ejemplo: **instala apache en el servidor**). Ansible utiliza un esquema **declarativo**, indicamos el **estado** en que queremos tener el servidor (por ejemplo, **me gustaría que el servidor tenga instalado apache**).

    ansible **hará todas las operaciones necesarias para que el estado declarado se cumpla de forma exitosa.** Si el estado que deseamos alcanzar ya lo tiene el servidor **no se ejecutará ninguna operación** (**Idempotencia**).


{% capture notice-text %}	 
## ¿Qué tienes que entregar?

1. Entrega el contenido del fichero de inventario y la configuración de tu proyecto ansible.
2. Prueba la conectividad con el servidor remoto y muestra la salida.
3. Ejecuta en el servidor remoto la instrucción `hostname`.
4. Responde: ¿Cómo se llama la propiedad que permite que las tareas que ya se han realizado no se vuelvan a ejecutar?
5. Copia un fichero desde tu ordenador al servidor remoto. ¿Qué pone la primera línea de la salida de la ejecución del comando? ¿De qué color se muestra la salida?
6. Vuelve a ejecutar la copia del fichero. ¿Qué pone la primera línea de la salida de la ejecución del comando? ¿De qué color se muestra la salida? ¿Por qué?
7. Modifica el fichero en tu ordenador o en el servidor remoto y vuelve a ejecutar la copia. ¿Qué sucede ahora?
8. Crea un directorio en el servidor remoto y comprueba que se ha creado.
9. Instala el servidor nginx en el servidor remoto. Comprueba que se ha realizado la instalación.
10. Intenta volver a ejecutar nginx en el servidor remoto. ¿Qué ocurre?
11. ¿Qué módulo de ansible tienes que usar para gestionar el servicio que acabas de instalar? Para el servicio nginx. Comprueba que has parado el servicio.
12. Desinstala el servidor nginx. Comprueba la desinstalación.
13. Crea un usuario en el servicio remoto. Comprueba que el usuario se ha creado.
14. Elimina el usuario que has creado. Comprueba que se ha eliminado de forma correcta.

{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>
