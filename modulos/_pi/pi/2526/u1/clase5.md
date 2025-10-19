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

1. Configura tu escenario de forma adecuada para crear las máquinas virtuales del ejemplo 5. Accede a la primera por ssh y comprueba que puedes hacer ping a la segunda. Accede de forma adecuada por ssh a la primera máquina para desde ella acceder a la segunda. Destruye el escenario.
2. Modifica lo necesario para crear otra máquina conectada a la red muy aislada. Comprueba que todo funciona de manera adecuada. Destruye el escenario.


## Ejemplo 6: Generados de escenarios con módulos

Para solucionar el problema del ejemplo anterior. en este ejemplo vamos a usar **módulos** de OpenTofu para generar máquinas virtuales y redes.
Los módulos se encuentra en el directorio fuera del directorio de trabajo, de esta forma podremos **reutilizarlos** en distintos proyectos. En nuestro ejemplo, los módulos están guardaos en el directorio `/terraform/modules/`. Tenemos dos módulos:

* `/terraform/modules/vm`: Contendrá todos los ficheros necesarios para crear máquinas virtuales según los parámetros que le mandemos.
* `/terraform/modules/network`: Contendrá todos los ficheros necesarios para crear redes según los parámetros que le mandemos.

Estudiemos lo ficheros más importantes:

* En el fichero `main.tf` vemos como utilizamos los dos módulos:
    * El módulo `network` crea una red, por tanto se recorre la declaración de las variables (`for_each = local.networks`) donde definimos las redes que queremos crear y se van creando cada una de ellas.
  * El módulo `mv` crea una máquina virtual, por tanto se recorre la declaración de las variables (`for_each = local.servers`) donde definimos las máquinas virtuales que queremos crear y se van creando cada una de ellas.
  Por ejemplo para usar el módulo `modules/mv`:
    ```
    module "server" {
    source   = "../../terraform/modules/vm"
    ```
* En el fichero `escenario.tf` definimos las variables de las redes y de las máquinas virtuales que queremos crear:
  * `local.networks` es una lista de diccionario, en cada uno de ellos se definen las variables necesarias para crear una red:
    * `name`: El nombre de la red que se crea en libvirt.
    * `mode`: Tipo de red. El valor para la red de tipo nat, es `nat`, para las redes aisladas y muy aisladas, `none` y para la red pública `bridge`.
    * `domain`: El nombre de dominio que envía el servidor DHCP.
    * `adresses`: Si es necesario, el direccionamiento de la red.
    * `bridge`: El nombre del bridge que se crea.
    * `dhcp`: `true` o `false` según activemos el servidor DHCP.
    * `dns`: `true` o `false` según activemos el servidor DNS.
    * `autostart`: `true` o `false` según activemos el inicio automática de la red.
  * `local.servers` es una lista de diccionarios donde definimos las variables necesarias para crear cada máquina virtual:
    * `name`: El nombre de la máquina virtual que se crea en libvirt.
    * `memory`: Memoria de la máquina.
    * `vcpu`: Número de núcleos virtuales de la máquina.
    * `base_image`: Nombre de la imagen base desde la que se crea el volumen de la máquina virtual.
    * `network`: Es un diccionario donde se definen las redes a las que está conectada la máquina. Para cada red se indica:
      * `network_name`: Nombre de la red a la que está conectada.
      * `wait_for_lease = true`: Esta opción se indica si la red tiene activo el servidor DHC.
    * `disks`: Es un diccionario donde se definen los discos que tiene la máquina. Para cada disco se indica:
      * `name`: Nombre del disco.
      * `size`: Tamaño del disco.
    * `user_data`: Directorio donde se encuentra el fichero de configuración `user_data.yaml`.
    * `network_config`: Directorio donde se encuentra el fichero de configuración `network-config.yaml`.



{% capture notice-text %}
## ¿Qué tienes que entregar?
1. Configura tu escenario de forma adecuada para crear las máquinas virtuales del escenario del ejeemplo6. Accede a la primera por ssh y comprueba que puedes hacer ping a la segunda. Accede de forma adecuada por ssh a la primera máquina para desde ella acceder a la segunda. Destruye el escenario.
2. Crea una nueva red de tipo NAT y crea un nuevo servidor con Ubuntu que esté conectado a esa red y a la red aislada. Accede a esa máquina y comprueba qsu direccionamiento y que puede hacer ping a las otras dos máquinas. Destruye el escenario.

{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>
