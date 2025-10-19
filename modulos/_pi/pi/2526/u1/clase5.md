---
title: "Clase 5: OpenTofu + libvirt - Creación de escenarios"
---

## ¿Qué vas a aprender en esta clase?

* Creación de escenarios con OpenTofu.
* Configuración de máquinas virtuales con cloud-init

## Teoría

En **OpenTofu**, un **módulo** es un conjunto de archivos de configuración que agrupan recursos relacionados, de forma que puedan **reutilizarse, organizarse y parametrizarse** fácilmente.

### Qué es un módulo

Un **módulo** es, esencialmente, una **unidad lógica de infraestructura** que encapsula uno o más recursos de OpenTofu.
El directorio raíz de un proyecto de OpenTofu ya es un módulo implícito (llamado *root module*), y puedes crear módulos adicionales en subdirectorios o reutilizar módulos externos (por ejemplo, del **OpenTofu Registry**).

### Para qué sirve

* **Reutilización:** permite definir una infraestructura una sola vez y usarla en múltiples entornos (desarrollo, pruebas, producción).
* **Organización:** ayuda a estructurar configuraciones grandes en partes más manejables.
* **Estandarización:** garantiza que recursos similares (por ejemplo, una red o una máquina virtual) se creen siempre de forma coherente.

### Variables

Los módulos suelen **definir variables de entrada** (`variable "nombre" { ... }`) que permiten **parametrizar** su comportamiento sin modificar su código interno.
También pueden **exportar valores** mediante **outputs** (`output "nombre" { ... }`) para que otros módulos o el módulo raíz los utilicen.

Las variables permiten que un mismo módulo sirva para múltiples escenarios simplemente cambiando los valores de entrada.

### Analogía con funciones

Sí, **puede asimilarse a una función** en un lenguaje de programación:

* Las **variables** de entrada son como los **parámetros** de la función.
* Los **outputs** son como los **valores de retorno**.
* La **lógica interna** del módulo describe los recursos que se crearán, análogamente al **código del cuerpo de la función**.

Llamar a un módulo desde otro archivo es como **invocar una función** con argumentos específicos.


## Ejercicios

Seguimos trabajando con el repositorio de ejemplos: [https://github.com/josedom24/opentofu-libvirt/](https://github.com/josedom24/opentofu-libvirt/).

### Ejemplo 4: Máquina virtual conectada a dos redes: una con DHCP y otra con direccionamiento estático

En este ejemplo seguimos trabajando con redes. En esta ocasión vamos a aprender a **configurar una interfaz de red de forma estática**.

En el fichero `networks.tf`:

* Se crea una red NAT con DHCP con el recurso `resource "libvirt_network" "nat_dhcp"`. 
* Se crea un red **aislada sin DHCP**, con el recurso `resource "libvirt_network" "aislada-static"`. Estudia los parámetro que hemos indicado.

Recuerda: el hecho de que conectemos una máquina virtual a dos redes **no significa que netplan configure las dos interfaces**. Tenemos que configurarlo nosotros, para ello:

* Creamos el fichero `cloud-init/server1/network-config.yaml` donde guardaremos la configuración netplan de la máquina, en este ejemplo puedes observar como se ha configurado de forma estárica. Si fuera necesario podríamos indicar la puerta de enlace, el servidor DNS o cualquier otra configuración de red que necesitemos.
* Recuerda que añadimos este fichero en la imagen ISO junto al fichero `cloud-init/server1/user-data.yaml`. Esto se hace con el parámetro `network_config` del recurso `resource "libvirt_cloudinit_disk" "server1-cloudinit"` en el fichero `main.tf`.



## ¿Qué tienes que realizar?

1. Configura tu escenario de forma adecuada para crear una máquina virtual con debian13. Ejecuta la configuración terreaform del ejemplo 4 y comprueba que efectivamente las dos interfaces están configuradas. ¿Puedes hacer ping a la dirección que hemos configurado de forma estática?. Razona la respuesta. Destruye el escenario, 
2. Crea una nueva **red muy aislada** y cambia la configuración para conectar la máquina virtual a esta red. Configurala con una dirección en el direccionamiento `172.16.0.0/16`. ¿Puedes hacer ping a esta dirección que hemos configurado?. Razona la respuesta. Destruye el escenario.

## Ejemplo 5: Dos máquinas virtuales conectadas entre sí

En este ejemplo vamos a comenzar a crear escenarios, es decir a crear varias máquinas interconectadas.
En este ejemplo concreto tenemos dos máquinas que están conectadas entre sí, para conseguirlo tenemos los siguientes ficheros:

* `main1.tf` y `main2.tf`: en cada uno de estos ficheros está la definición de una máquina.
* Dentro del directorio `cloud-init` tenemos dos directorios, para guardar el `user-data.yaml` y el `network-config.yaml` para configurar cada una de las máquinas.
* El fichero `output` se ha modificado para que devuelva información de cada máquina.

En este ejemplo, el primer servidor está conectado a una red NAT y una red muy aislada. El segundo servidor se conecta sólo a la red muy aislada.

**Limitación** de esta solución para crear escenarios:

* Es **muy repetitiva**, tenemos que crear los siguientes ficheros según el número de máquinas que queremos. Si queremos crear un escenario con 3 máquinas:
  * Tenemos que crear 3 ficheros `mainX.tf`.
  * Tenemos que crear 3 directorios `cloud-init/serverX` para guardar la configuración cloud-init de cada máquina.
  * Tenemos que modificar el fichero `output.tf` para mostrar información de las 3 máquinas.


## ¿Qué tienes que realizar?

1. Configura tu escenario de forma adecuada para crear las máquinas virtuales del ejemplo 5. Accede a la primera por ssh y comprueba que puedes hacer ping a la segunda. Accede de forma adecuada por ssh a la primera máquina para desde ella acceder a la segunda. Destruye el escenario
2. Modifica lo necesario para crear otra máquina conectada a la red muy aislada. Comprueba que todo funciona de manera adecuada. Destruye el escenario.


## Ejemplo 6: Generados de escenarios con módulos

Para solucionar el problema del ejemplo anterior. en este ejemplo vamos a usar **módulos** de OpenTofu para generar máquinas virtuales y redes.
Los módulos se encuentra en el directorio fuera del directorio de trabajo, de esta forma podremos **reutilizarlos** en distintos proyectos. En nuestro ejemplo, los módulos están guardaos en el directorio `/terraform/modules/`. Tenemos dos módulos:

* `/terraform/modules/vm`: Contendrá todos los ficheros necesarios para crear máquinas virtuales según los parámetros que le mandemos.
* `/terraform/modules/network`: Contendrá todos los ficheros necesarios para crear redes según los parámetros que le mandemos.

Estudiemos lo ficheros más importantes:

* En el fichero `main.tf`
 
* Los datos para crear máquinas virtuales y redes estarán declarados en variables en el fichero `main.tf`.
* En el fichero `main.tf` podré llamar cuantas veces quiera al módulo `mv` para crear las máquinas que necesite. En este ejemplo están definida dos máquina. Cada una empieza con estas líneas:
  ```
  module "server1" {
  source = "./modules/vm"
  ...
  ```
* De cada máquina se especifica:
  * El nombre.
  * La memoria.
  * El número de cpu.
  * El pool de trabajo.
  * El path del pool que estamos usando.
  * La imagen base.
  * Las redes a las que está conectada. Con el parámetro `network` y con el parámetro `depends_on`. recuerda que en las redes con servidor DHCP se indica el parámetro `wait_for_lease = true`.
  * Los discos extras que tiene.
  * El path donde se encuentra el `user-data.yaml` y el `network-config.yaml`.
* Si queremos tener 















{% capture notice-text %}
## ¿Qué tienes que entregar?


{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>
