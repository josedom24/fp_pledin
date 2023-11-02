---
title: "Práctica: Creación y configuración de un servidor LAMP"
---

![escenario](img/practica.png)

## 1ª Tarea: Vagrant

Queremos automatizar la creación de un servidor LAMP usando Vagrant, el esquema que queremos desarrollar, que vemos en la imagen, tiene las siguientes características:

Es escenario tiene tres máquinas:

* `router`: que está conectada a una red pública (**br0**) y a una red privada (muy aislada). La máquina `router` debe salir por la red pública. **Esta máquina no va a utilizar eth0 para acceder al exterior**.
* `web`: En este servidor se instalará un servidor web. Esta máquina está conectada a la misma red privada que la máquina anterior. Y esta conectada por otra red muy aislada a la máquina `bd`.
* `bd`: En este servidor se instalará un gestor de bases de datos. Está conectada a la máquina `web` por la segunda red privada muy aislada.

## 2ª Tarea: Ansible

Vamos a usar la interfaz eth0 de las máquinas que están conectadas a la **red de mantenimiento** para conectarnos con ansible y configurar las máquinas. Cuando termine el ejercicio, no usaremos `vagrant ssh` para conectarnos por ssh a las máquinas (está conexión utiliza eth0), usaremos las otras interfaces para realizar las conexiones ssh.

Queremos configurar el escenario con ansible, para que cumpla lo siguiente:

* Las máquinas conectadas a la red privada muy aislada a la que está conectada el `router` deben tener acceso a internet. Para ello, la máquina `router` debe estar configurada para enrutar las peticiones de las máquinas conectadas a la red privada. 
* La máquina `web` tendrá un servidor web apache2 instalado. La máquina `router` hará DNAT para que podamos acceder a la página usando su IP pública.
* La máquina `bd` tendrá un servidor de base de datos mariadb.

La receta ansible debe tener al menos 5 roles:

### commons

Estas tareas se deben ejecutar en **todos** los nodos: actualizar los paquetes y añadir tu clave pública a la máquinas para poder acceder a ellas con ssh. ¿Existe algún módulo de ansible que te permita copiar claves públicas?.

### router

Todas las tareas necesarias para configurar `router`: está máquina tiene que hacer snat, y salir a internet por eth1 (la red pública). Las configuraciones deben ser permanentes. ¿Existe algún módulo de ansible que te permita ejecutar `sysctl`?.

### redinterna

Todas las tareas que hay ejecutar en las máquinas conectadas al `router` por la red privada muy aislada.
--------------------
* `cliente`: Todas las tareas necesarias para que **las máquinas conectadas a la red privada** salgan a internet por `eth1`.
* `web`: Las tareas necesarias para instalar y configurar un servidor web con una página estática en la máquina `cliente`.

{% capture notice-text %}
## Entrega

1. Entrega la URL del repositorio GitHub donde has alojado todos los ficheros.
2. Entrega una captura de pantalla accediendo por ssh a las dos máquinas (**sin utilizar `vagrant ssh`, es decir sin hacer conexiones a `eth0`**). Usa la opción `-A`  de ssh para acceder al `cliente`.
3. Entrega capturas de pantalla donde se vean las puertas de enlaces de los dos equipos.
4. Entrega capturas de pantalla donde se vean las máquinas haciendo ping al exterior.
5. Entrega una captura de pantalla donde se vea un acceso a la página web alojada en la máquina `cliente`.
6. Estudia la forma de integrar la receta ansible en vagrant, de tal manera que una vez se cree el escenario se ejecuta la configuración. 
{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>


