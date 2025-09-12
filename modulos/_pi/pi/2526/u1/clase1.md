---
title: "Clase 1: Introducción a ansible. Playbook sencillo."
---

## ¿Qué vas a aprender en esta clase?

* El concepto de infraestructura como código.
* El concepto de Software de gestión de la configuración (CMS)
* Para que sirve ansible y vamos a comenzar a trabajar con este software.

## Teoría

### API / API restfull

Una **API** (*Application Programming Interface*) es un conjunto de reglas y funciones que permiten que dos programas se comuniquen entre sí.

Una **API RESTful** es un tipo de API que sigue el estilo **REST** (*Representational State Transfer*), usando el protocolo HTTP (operaciones **GET**, **POST**,...)

Imagina una API RESTful para gestionar libros:

* `GET /libros` → devuelve la lista de libros
* `GET /libros/5` → devuelve el libro con ID 5
* `POST /libros` → crea un nuevo libro
* `PUT /libros/5` → actualiza el libro con ID 5
* `DELETE /libros/5` → elimina el libro con ID 5

La información que devuelve una API restfull viene representada por algún lenguaje de marcas (json, xml, yaml,...)


### Infraestructura como código

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

3. Haz un fork del repositorio [ taller_ansible_vagrant](https://github.com/josedom24/taller_ansible_vagrant) y realiza una clonación en el ordenador donde has instalado ansible. Vamos a trabajar en el directorio **Taller1**.

4. El **inventario** es el fichero donde definimos los equipos que vamos a configurar. En nuestro caso se llama `hosts`. En el inventario se clasifican los equipos por grupos:

	* El grupo `all` corresponde a todos los equipos definidos.
	* En este ejemplo hemos creado un grupo `servidores`, donde hemos definido nuestra máquina.
	* A la máquina la hemos llamado `nodo1` (**cambia el nombre y pon el de tu máquina**), además **debes rellenar la siguiente información del nodo**:
		* `ansible_ssh_host`: Dirección IP del equipo que queremos configurar.
		* `ansible_ssh_user`: Usuario sin privilegios con el que vamos  acceder por ssh (lo hemos creado en el equipo en el punto 2).
		* `ansible_ssh_private_key_file`: Fichero con la clave privada que vamos a usar para el acceso.

5. El **fichero de configuración** lo encontramos en el fichero `ansible.cfg`, donde **tienes que poner el nombre del fichero de inventario en el parámetro `inventory`**. El parámetro `host_key_checking = False` impide que se haga la comprobación del equipo cada vez que se hace la conexión ssh.

6. Vamos a comprobar si tenemos conectividad con el nodo. Para ello vamos a usar el módulo `ping` de ansible. Ejecuta alguna de estas instrucciones:

	* `ansible -m ping all`: Comprueba la conectividad con **todos** los equipos del inventario.
	* `ansible -m ping servidores`: Comprueba la conectividad con  los equipos del **grupo servidores**.
	* `ansible -m ping nodo1`: Comprueba la conectividad con el equipo **nodo1** (Cambia el nombre con el que has configurado en el fichero).
	
	Debe salir el mensaje "pong" en verde.

7. ansible puede trabajar con variables que obtiene de distinta manera:

	* A nivel de **nodo**: definimos variables para cada nodo en el inventario, por ejemplo: `ansible_ssh_host`, `ansible_ssh_user`, ...
	* A nivel de **grupo de nodos**: Hemos creado un directorio que se tiene que llamar `group_vars`, dentro de este directorio podemos crear ficheros con las variables que creamos a nivel del grupo. En este ejemplo hemos creado un fichero `all`, por lo que las variables serán conocidas para todos los nodos. Hemos definido 3 variables para todos los nodos:`bd_name`, `bd_user` y `bd_pass`.
	* **Gathering Facts**: Variables que obtiene ansible de los nodos que está configurando. La primera tarea que ejecuta el play es obtener información del nodo que va a configurar. Toda esa información se puede usar al definir las tareas, por ejemplo: `ansible_hostname`, `ansible_distribution`,... Para ver esa información podemos ejecutar:`ansible nodo1 -m setup`.

8. Veamos el playbook que se encuentra en el fichero `site.yml`:

	* Primera línea: `hosts: all`. Significa que las tareas se van a ejecutar en todos los nodos definidos en el inventario. Podríamos haber puesto `hosts: servidores` o `hosts: nodo1`.
	* `become: true`: En las tareas que necesiten ejecutarse como administrador se utilizará `sudo`. 
	* `tasks`: Lista de tareas. Todas las tareas tienen un mensaje en el parámetro `name` y el uso de un módulo.

	Veamos las tareas que están definidas:

	1. **Actualizamos el sistema**: Se utiliza el módulo [apt](https://docs.ansible.com/ansible/latest/collections/ansible/builtin/apt_module.html) para actualizar los paquetes del sistema.
	2. **Instalar paquetes con apt**: **Busca en la documentación del módulo [apt](https://docs.ansible.com/ansible/latest/collections/ansible/builtin/apt_module.html) y termina la segunda tarea para hacer la instalación del paquete `git` y `apache2`.**
	3. **Copiar fichero a la máquina remota**: El módulo [copy](https://docs.ansible.com/ansible/latest/collections/ansible/builtin/copy_module.html) nos permite copiar ficheros desde el equipo donde tenemos ansible instalado hasta la máquina que estamos configurando. Los ficheros se suelen guardar en un directorio llamado `files`. **Modifica la tarea para guardar el fichero `foo.txt` al directorio `/etc` de la máquina remota**.
	4. **Copiar un template a un fichero de la máquina remota**: El módulo [template](https://docs.ansible.com/ansible/latest/collections/ansible/builtin/template_module.html#) nos permite copiar una plantilla jinja2 (que normalmente tenemos en un directorio llamado `template`) a la máquina remota después de cambiar las variables por los valores adecuados. 
		* **Modifica la plantilla `index.j2` para indicar los nombres correctos de las variables. Tienes que cambiar las variables `modifica_el_nombre` por el nombre correcto de las variables.**
		* **Modifica la tarea para guardar el template en el directorio `/var/www/html/index.html` de la máquina que estamos configurando.**

9. Ejecuta el playbook:

	```
	ansible-playbook site.yaml
	```

	* **Si tienes errores, repasa las modificaciones que has realizado para corregirlos.** 
	* **Cuando funcione la ejecución de la receta, cambia el fichero `foo.txt` y ejecuta de nuevo la receta. ¿Se ejecutan todas las tareas?**
	* **¿Cómo se llama la propiedad que permite que las tareas que ya se han realizado no se vuelvan a ejecutar?**
	* **Comprobación del funcionamiento: Comprueba que se ha copiado un fichero `foo.txt` en el servidor, accede desde un navegador al servidor y comprueba que aparece el fichero `index.html` que hemos creado.**

{% capture notice-text %}	 
## ¿Qué tienes que entregar?

1. Entrega los ficheros: `site.yaml`, `hosts` y `template/index.j2`.
2. Entrega una captura de pantalla donde se vea que se ha finalizado la ejecución del playbook.
3. Responde: ¿Cómo se llama la propiedad que permite que las tareas que ya se han realizado no se vuelvan a ejecutar?
4. Captura de pantalla, donde se vea el fichero `foo.txt` en el servidor configurado.
5. Captura de pantalla donde se vea el acceso desde el navegador al servidor web, y se vea el contenido del fichero `index.html`.
6. Entrega la URL de tu repositorio con el que estás trabajando.
{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>