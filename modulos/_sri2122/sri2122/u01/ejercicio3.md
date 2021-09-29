---
title: Ejercicio configuración del escenario router-nat
---

Queremos configurar el escenario para que cumpla lo siguiente:

* La máquina `router` debe acceder a internet por `eth1`. `eth0` sólo se utiliza para acceder a la máquina con `vagrant ssh`.
* La máquina `cliente` debe tener acceso a internet. Para ello debe salir por `eth1` y la máquina `router` debe estar configurada para enrutar las peticiones de `cliente`. del mismo modo, `eth0` sólo se utiliza para acceder con `vagrant ssh`. Debes pensar que configuración debe tener la máquina `cliente`: puerta de enlace, configuración dns,...

Crea un playbook en ansible con los siguientes roles:

* common: Estas tareas se deben ejecutar en los dos nodos. La única tarea es actualizar los paquetes.
* router: Todas las tareas necesarias para configurar `router` cómo router-nat y que salga a internet por eth1. Las configuraciones deben ser permanente.
* cliente: Todas las tareas necesarias para que el cliente salga a internet pot eth1.


## Entrega

1. Comprobacion que `cliente` tiene acceso a internet haciendo ping a un nombre de una página web. Asegurate que no está saliendo por `eth0` (muestra las rutas).
2. Configura el sistema para que podamos acceder acceder a las máquinas por ssh. Te doy algunas ideas:

  * Puedes usar las claves privadas generadas para cada una de las máquinas, o puedes generar nuevas claves que introduces en las máquinas.
  * A lo mejor te viene bien la opción `-A ` de `ssh`.
  * Estudia el fichero `~/.ssh/config`. Configurando de forma adecuada el fichero de configuración de ssh en tu equipo hasta puedes hacer que se conecte directamente con `cliente`.
  * Las conexiones ssh nuncan las tienes que realizar por `eth0`.

    Entrega una captura de pantalla accediendo por ssh a las dos máquinas.
3. Estudia la forma de integrar la receta ansible en vagrant, de tal manera que una vez se cree el escenario se ejecuta la configuración. Enseñale el funcionamiento al profesor.
