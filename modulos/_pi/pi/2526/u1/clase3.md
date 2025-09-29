---
title: "Clase 3:  Ansible. Playbook con roles"
---

## ¿Qué vas a aprender en esta clase?

* El concepto de Rol.
* El uso de roles en los playbooks para realizar tareas en nodos concretos.
* El uso de handlers para gestionar los servicios que instalamos.
* Vas a seguir utilizando variables para realizar playbooks lo más generales posible.
* Seguimos aprendiendo otros módulos de ansible.
* La posibilidad de reutilizar roles para futuros playbooks.

## Teoria

* **Roles**: Normalmente dividimos los playbooks por cada servicio que quiero configurar.
	* Ejemplo: Rol “apache2”: Permite la instalación y configuración de apache2,. . .
	* Nos permite la reutilización de código.

* Un **handler (manejadores)** es una tarea especial que solo se ejecuta cuando es notificada por otra tarea. Por ejemplo, sólo se ejecuta la tarea de reiniciar un servicio, si la configuración del servicio ha cambiado. Esta tarea solo se ejecuta una vez, al terminar la ejecución del playbook.

## Recursos

* [Presentación: Infraestructura como código. Ansible y Vagrant](https://fp.josedomingo.org/sri/pdf/iac.pdf). 

## Ejercicio

En este taller vamos a trabajar con dos servidores. Cada uno va a jugar un papel: uno será el servidor web y el otro será el servidor de base datos.

Tal como hemos definido las tareas en el taller anterior, no puedo indicar que tareas hay que realizar para nodos distintos que estén agrupados en distintos grupos. Para solucionarlo vamos a usar los **roles**, que nos permiten organizar las tareas para ejecutarlas en todos los nodos, o en un grupo de nodos en concreto. Además los roles me dan la posibilidad de reutilización de código. Si hago un rol para instalar un servidor web apache, ese rol lo puedo volver a usar en otro proyecto en que tenga que hacer la misma operación.

Realiza los siguientes pasos:

1. Crear dos máquinas virtuales (con las características indicadas en el taller anterior). 
2. Vamos a trabajar con el directorio **Taller2** del repositorio.
3. Rellena el inventario de forma adecuada para definir los dos equipos que vamos a configurar. Debes indicar los nombres de tus máquinas y los parámetros de acceso.
4. Prueba de conectividad. Ejecuta el comando `ansible -m ping all` para asegurarte que puedes conectar con las máquinas.
5. Vamos a estudiar la nueva definición del playbook, en el fichero `site.yaml`:
	* El campo `hosts`: es el nombre del grupo o máquina en la que se van a ejecutar las tareas del rol.
	* El campo `roles/role` es el nombre del rol que se va a ejecutar. Este nombre debe coincidir con el nombre del directorio que encontramos dentro del directorio `roles`.

	**Modifica el fichero `site.yaml`** para conseguir que se ejecuten los roles como se indica a continuación:

	* El rol `commons` (tareas comunes a todos los nodos) para todos los nodos (grupo `all`).
	* El rol `apache2` (instalación y configuración de apache2) para todos los nodos del grupo `servidores_web`.
	* El rol `mariadb` (instalación y configuración de mariadb) para todos los nodos del grupo `servidores_bd`.
6. Los roles se van a definir en el directorio `roles`. Se creará un directorio para cada rol, que se llamará igual al nombre del rol utilizado en el fichero `site.yaml` y contendrá las tareas, ficheros, templates, manejadores,... necesarios para llevar a cabo este rol.

	Por lo tanto dentro de la carpeta del rol, podremos tener algunas de estas carpetas:
	
	* `tasks`: Contiene el yaml con las tareas.
	* `files`: Contiene los ficheros que vamos a copiar a los nodos con el módulo `copy`.
	* `templates`: Contiene las plantillas que vamos a copiar a los nodos con el módulo `template`.
	* `handlers`: Contiene los **manejadores**, qué son las tareas para gestionar los servicios que se han instalado.
	* ...
7. El rol `commons` se ejecuta en todos los nodos. Sólo tiene la carpeta `tasks` donde encontramos el fichero `main.yaml` con las tareas que se van a ejecutar. **Modifica la tarea que está definida para que se actualice el sistema de todas las máquinas.**

8. El rol `apache2` instala apache2 y copia algunos ficheros al servidor. Uno de los ficheros que copia es un fichero de configuración de apache2, por lo tanto debemos reiniciar apache2 cada vez que copiamos ese fichero. 

	En ocasiones es necesario sólo ejecutar unas tareas si ocurre algo. Por ejemplo, si cambiamos el fichero de configuración de un servicio, habrá que ejecutar una tarea para reiniciar el servicio. Este compartimento se consigue usando los **handlers (manejadores)**.

	Para cambiar la configuración de un servicio, tenemos dos alternativas:
	
    * Copiar el fichero de configuración con el módulo `copy`, aunque en las mayoría de las ocasiones tendremos el fichero de configuración parametrizado, por lo que usaremos una plantilla y el módulo `template`.
    * Usar el módulo `lineinfile` que nos permite hacer modificaciones en un fichero remoto.

	En la tarea **Copiar fichero de configuración y reiniciar el servicio** hemos copiado al servidor web un fichero de configuración y tenemos que indicar que queremos reiniciar el servicio, para ello usamos el parámetro `notify`. Si se ejecuta una tarea con el parámetro `notify`, se ejecutará la tarea indicada, también llamado **handler** (normalmente reinicio del servicio) al finalizar la ejecución de todas las tareas del playbook.

	**Debes poner en el parámetro `notify` el nombre de la tarea que se encuentra en el fichero `main.yaml` del directorio `handlers`, que será el encargado de reiniciar el servicio.**
	
9. El rol `mariadb` instala el servidor de base de datos mariadb, crea una base de datos y un usuario y modifica la configuración del servicio. Vamos a utilizar algunos nuevos módulos: [mysql_db](https://docs.ansible.com/ansible/2.9/modules/mysql_db_module.html) para crear una base de datos, [mysql_user](https://docs.ansible.com/ansible/2.9/modules/mysql_user_module.html) para gestionar usuarios de la base de datos y [lineinfile](https://docs.ansible.com/ansible/2.9/modules/lineinfile_module.html) para modificar líneas en ficheros de texto.
	
	Otra cosa que puedes aprender, es como realizamos los bucles en ansible. Usamos el parámetro `with_items:` y la variable que cambia en cada iteración se llama `item`.

	* **Modifica las variables `cambia_nombre_variable` por la variables correctas. ¿En qué fichero tienes que buscar el nombre de la variables correctas?**.
	* **Debes poner en el parámetro `notify` el nombre de la tarea que se encuentra en el fichero `main.yaml` del directorio `handlers`, que será el encargado de reiniciar el servicio.**
10. Ejecuta el playbook:

	```
	ansible-playbook site.yaml
	```

	* **Si tienes errores, repasa las modificaciones que has realizado para corregirlos.** 
	* **Cuando funcione la ejecución de la receta, cambia una de las tareas que notifican un reinicio para comprobar que se produce de nuevo el reinicio del servicio.**
	* **Comprobación del funcionamiento: Accede desde el navegador web y comprueba los ficheros que hemos subido al servidor. Accede a la base de datos.**

{% capture notice-text %}
## ¿Qué tienes que entregar?

1. Entrega una captura de pantalla donde se vea que se ha finalizado la ejecución del playbook.
2. Captura de pantalla donde se vea el acceso desde el navegador al servidor web, y se vea el contenido del fichero `index.html`.
3. Captura de pantalla donde se vea el acceso a la base de datos.
4. Realiza un cambio en la receta que necesite ejecutar el reinicio del servicio. Ejecuta de nuevo el playbook y comprueba que se ha ejecutado el handler correspondiente. 
5. Entrega la URL de tu repositorio con el que estás trabajando.
{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>