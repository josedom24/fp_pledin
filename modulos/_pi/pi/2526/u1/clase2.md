---
title: "Clase 2: Ansible. Ejecución de Playbooks"
---

## ¿Qué vas a aprender en esta clase?

* Conocer los ficheros fundamentales en la configuración de ansible.
* Trabajar con la estructura de un playbook.
* Trabajar con variables.
* Aprender algunos módulos de ansible.
* Ejecutar un playbook ansible.

## Teoria

* **Jugada (play)**: Declaración en yaml de una acción (se utiliza un módulo) que quiero conseguir. Ejemplo: Quiero que en la máquina este instalado un paquete de una versión determinada.
* **Libro de jugadas (playbooks)**: Conjuntos de jugadas (plays), para conseguir una configuración compleja de la máquina.
* **Variables**: Los plays, normalmente, están parametrizados. Se utilizan variables para concretar la configuración en cada caso. Ansible puede trabajar con variables que obtiene de distinta manera:
	* A nivel de **nodo**: definimos variables para cada nodo en el inventario, por ejemplo: `ansible_ssh_host`, `ansible_ssh_user`, ...
	* A nivel de **grupo de nodos**: Hemos creado un directorio que se tiene que llamar `group_vars`, dentro de este directorio podemos crear ficheros con las variables que creamos a nivel del grupo. Dentro de este directorio suele haber un fichero `all` donde se definen las variables que se pueden utilizar al configurar todos los nodos. Si en el inventario tuviéramos un grupo llamado `servidores`, dentro de este directorio podríamos crear un fichero con el mismo nombre, y en él declararíamos las variables que podemos usar al configurar los nodos del grupo `servidores`. Para simplificar, solemos usar el fichero `all`.
	* **Gathering Facts**: Variables que obtiene ansible de los nodos que está configurando. La primera tarea que ejecuta el play es obtener información del nodo que va a configurar. Toda esa información se puede usar al definir las tareas, por ejemplo: `ansible_hostname`, `ansible_distribution`,... Para ver esa información podemos ejecutar:`ansible nodo1 -m setup`.

## Recursos

* [Presentación: Infraestructura como código. Ansible y Vagrant](https://fp.josedomingo.org/sri/pdf/iac.pdf). 

## Ejercicio

1. Haz un fork del repositorio [ taller_ansible_vagrant](https://github.com/josedom24/taller_ansible_vagrant) y realiza una clonación en el ordenador donde has instalado ansible. Vamos a trabajar en el directorio **Taller1**.

2. Rellena de manera adecuada el inventario y la configuración de ansible.

3. Contesta estas preguntas: ¿Qué variables están definidas a nivel de nodo?. ¿Qué variables están definidas a a nivel de grupos de nodos?, ¿qué fichero has consultado?.

4. Ejecuta el método necesario para obtener las variables del nodo (**Gathering Facts**).

5. Veamos el playbook que se encuentra en el fichero `site.yml`:

	* Primera línea: `hosts: all`. Significa que las tareas se van a ejecutar en todos los nodos definidos en el inventario. Podríamos haber puesto `hosts: servidores` u `hosts: nodo1`.
	* `become: true`: En las tareas que necesiten ejecutarse como administrador se utilizará `sudo`. 
	* `tasks`: Lista de tareas. Todas las tareas tienen un mensaje en el parámetro `name` y el uso de un módulo.

6. Ejecuta el playbook:

	```
	ansible-playbook site.yaml
	```

	* **Si tienes errores, repasa las modificaciones que has realizado para corregirlos.** 
	* **Cuando funcione la ejecución de la receta, cambia el fichero `foo.txt` y ejecuta de nuevo la receta. ¿Se ejecutan todas las tareas?**
	* **¿Cómo se llama la propiedad que permite que las tareas que ya se han realizado no se vuelvan a ejecutar?**
	* **Comprobación del funcionamiento: Comprueba que se ha copiado un fichero `foo.txt` en el servidor, accede desde un navegador al servidor y comprueba que aparece el fichero `index.html` que hemos creado.**

	Veamos las tareas que están definidas:

	1. **Actualizamos el sistema**: Se utiliza el módulo [apt](https://docs.ansible.com/ansible/latest/collections/ansible/builtin/apt_module.html) para actualizar los paquetes del sistema.
	2. **Instalar paquetes con apt**: **Busca en la documentación del módulo [apt](https://docs.ansible.com/ansible/latest/collections/ansible/builtin/apt_module.html) y termina la segunda tarea para hacer la instalación del paquete `git` y `apache2`.**
	3. **Copiar fichero a la máquina remota**: El módulo [copy](https://docs.ansible.com/ansible/latest/collections/ansible/builtin/copy_module.html) nos permite copiar ficheros desde el equipo donde tenemos ansible instalado hasta la máquina que estamos configurando. Los ficheros se suelen guardar en un directorio llamado `files`. **Modifica la tarea para guardar el fichero `foo.txt` al directorio `/etc` de la máquina remota**.
	4. **Copiar un template a un fichero de la máquina remota**: El módulo [template](https://docs.ansible.com/ansible/latest/collections/ansible/builtin/template_module.html#) nos permite copiar una plantilla jinja2 (que normalmente tenemos en un directorio llamado `template`) a la máquina remota después de cambiar las variables por los valores adecuados. 
		* **Modifica la plantilla `index.j2` para indicar los nombres correctos de las variables. Tienes que cambiar las variables `modifica_el_nombre` por el nombre correcto de las variables.**
		* **Modifica la tarea para guardar el template en el directorio `/var/www/html/index.html` de la máquina que estamos configurando.**
        
{% capture notice-text %}	 
## ¿Qué tienes que entregar?

1. Entrega los ficheros: `site.yaml`, `hosts` y `template/index.j2`.
2. Entrega una captura de pantalla donde se vea que se ha finalizado la ejecución del playbook.
3. Vuelve a ejecutar el playbook, ¿se ejecutan todas las tareas?. ¿Cómo se llama la propiedad que permite que las tareas que ya se han realizado no se vuelvan a ejecutar?
4. Comprueba que el fichero `foo.conf` se ha copiado al servidor configurado. Modifica o barra el fichero en el servidor y vuelve a ejecutar el playbook. ¿Qué ocurre?
5. Captura de pantalla donde se vea el acceso desde el navegador al servidor web, y se vea el contenido del fichero `index.html`.
6. Entrega la URL de tu repositorio con el que estás trabajando.
{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>
