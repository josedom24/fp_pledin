---
title: "Clase 4: Introducción a OpenTofu + libvirt"
---

## ¿Qué vas a aprender en esta clase?

* El concepto de orquestador de escenarios
* El uso básico de OpenTofu + libvirt
* Creación de recursos virtualizados con OpenTofu.
* Configuración de máquinas virtuales con cloud-init

## Teoría

### Imágenes Cloud

Podemos crear máquinas virtuales de forma automática es el uso de **imágenes cloud** (plantillas) junto con **cloud-init**, una herramienta diseñada para la inicialización y configuración automática de instancias en su primer arranque. Puedes ver un ejemplo en el apartado:

* [Despliegue automatizado de máquinas virtuales usando cloud-init](https://github.com/josedom24/curso_kvm_ow/blob/main/curso2/contenidos/unidad07/clase3.md)

### ¿Qué es OpenTofu?

**OpenTofu** es un *fork* de **Terraform 1.5.x**, creado por la comunidad (liderado por la *Linux Foundation*) después de que HashiCorp cambiara la licencia de Terraform a **BUSL 1.1** en 2023.
OpenTofu conserva el **modelo declarativo de infraestructura como código (IaC)**, totalmente compatible con los ficheros `.tf` y los *providers* existentes de Terraform.
Su objetivo es mantener una herramienta **100 % libre y abierta**, compatible con el ecosistema de Terraform, pero sin restricciones de uso.

Permite **definir, crear y administrar infraestructura** (máquinas virtuales, redes, contenedores, etc.) usando archivos de texto declarativos (`.tf`).
En lugar de crear recursos manualmente, describes **qué infraestructura quieres**, y OpenTofu se encarga de **construirla, modificarla o destruirla** de forma reproducible.

* OpenTofu está licenciado bajo **MPL 2.0** (*Mozilla Public License*), reconocida como licencia libre y open source.
* Está gobernado por la **Linux Foundation**, no por una empresa.
* Todo el desarrollo es abierto y las decisiones se discuten públicamente.


### ¿Qué es un *provider*?

Un **provider** (proveedor) es un **plugin** que permite a OpenTofu interactuar con una plataforma o tecnología concreta.
Cada provider sabe cómo crear, leer, actualizar y eliminar recursos.

Ejemplos:

* `aws` → Amazon Web Services
* `azurerm` → Microsoft Azure
* `libvirt` → Máquinas virtuales locales con KVM
* `docker` → Contenedores Docker

En el caso de **libvirt**, el provider permite a OpenTofu crear y gestionar VMs en tu sistema KVM local.

### Comandos más importantes de OpenTofu

| Comando              | Descripción                                                                     |
| -------------------- | ------------------------------------------------------------------------------- |
| `tofu init`     | Inicializa el proyecto, descarga los *providers* y prepara el entorno.          |
| `tofu plan`     | Muestra qué acciones realizará OpenTofu (sin aplicar cambios).                 |
| `tofu apply`    | Aplica los cambios: crea, modifica o elimina recursos según los archivos `.tf`. |
| `tofu destroy`  | Elimina todos los recursos gestionados por el proyecto.                         |
| `tofu validate` | Verifica que la sintaxis de los archivos `.tf` sea correcta.                    |
| `tofu show`     | Muestra el estado actual de los recursos creados.                               |
| `tofu output`   | Muestra los valores definidos en bloques `output`.                              |

### Instalación de OpenTofu

Puedes ver los detalles en la página [Installing OpenTofu on .deb-based Linux (Debian, Ubuntu, etc.)](https://opentofu.org/docs/intro/install/deb/).

## Ejercicios

1. Vamos a descargar la imágenes cloud con la que vamos a trabajar. La vamos a copiar en el directorio correspondiente al pool `default`:

  ```
  cd /var/lib/libvirt/images
  sudo wget https://cloud.debian.org/images/cloud/trixie/daily/latest/debian-13-genericcloud-amd64-daily.qcow2 -O debian13-base.qcow2
  sudo wget https://cloud-images.ubuntu.com/noble/20251001/noble-server-cloudimg-amd64.img -O ubuntu2404-base.qcow2
  ```

  Las imágenes bases se llaman `debian13-base.qcow2` y `ubuntu2404-base.qcow2`.

2. Instala OpenTofu y haz un fork del repositorio de ejemplos: [https://github.com/josedom24/opentofu-libvirt/](https://github.com/josedom24/opentofu-libvirt/).

### Ejemplo 1: Máquina virtual conectada a la red "default"

Empezamos a trabajar en el directorio`ejemplo1`. En este ejemplo vamos a crear un máquina virtual conectada a la red `default`. OpenTofu trabaja con fichero **tf** que se pueden llamar como queremos. Veamos los ficheros con los que vamos a trabajar:

* `provider.tf`: Configura el provider que vamos a usar y lo configura. El plugin del provider se instala en el directorio `.terraform` cuando ejecutamos `tofu init`. Este comando **sólo se ejecuta una vez**. Este fichero **noo hay que modificarlo**.
* `variables.tf`: Se declaran variables globales, que podemos usar en nuestras definiciones. En este caso se definen:
  * `var.libvirt_pool_name`: donde guardamos el nombre del pool en el que queremos crear la máquina virtual. Su valor por defecto es `default`.
  * `var.libvirt_pool_path`: donde se guarda el directorio correspondiente al pool `default`, normalmente es `/var/lib/libvirt/images`. 
  Este fichero **se modifica una vez** indicando vuestros datos particulares.
* `cloud-init/base.yaml`: Fichero para configurar la máquina instalando los paquetes y configurando lo necesario para que el teclado este en español cuando accedemos a la máquina. **No hay que modificarlo**.
* `cloud-init/server1/user-data.yaml`: Fichero para configurar la máquina virtual con el mecanismo de cloud-init. En este ejemplo:
  * Se indica el hostname.
  * Se configura el usuario `debian` y se lo pone una contraseña.
  * Se ejecuta una `apt update`.
* `cloud-init`: Se crea la variable local `local.merged` con la unión de los dos ficheros de configuración cloud-init: `cloud-init/base.yaml` y `cloud-init/server1/user-data.yaml`. Esta variable se usará posteriormente para crear la imagen ISO donde esta la configuración cloud-init.
* `main.tf`: Aquí está la definición de los recursos con los que queremos trabajar. Los recursos se definen con el parámetro `resource "<tipo del recurso>" "<nombre del recurso>"`. El nombre del recurso debe ser único. Cada tipo de recurso tiene un conjunto de parámetros. En este fichero se definen los siguiente recursos:
  * `resource "libvirt_volume" "server1-disk"`: Un volumen creado con clonación enlazada cuya imagen base está indicado con el parámetro `base_volume_id`. Este volumen se crea en el pool indicado en la variable `var.libvirt_pool_name`.
  * `resource "libvirt_cloudinit_disk" "server1-cloudinit"`: Un disco con formato ISO donde se guarda el fichero de configuración de cloud-init.
  * `resource "libvirt_domain" "server1"`: Una máquina virtual, donde se indica el nombre, la memoria, el número de CPUs, la red a la que está conectada y los discos que tiene.
      * Cuando la red a la que está conectada tiene un servidor DHCP, se indica el parámetro `wait_for_lease = true` que indica que se considera que la máquina está funcionando cuando recibe direccionamiento del servidor DHCP. 
* `output.tf`: Se define la información que se mostrará al terminar de crear el escenario. En este caso nos muestra el nombre y la dirección IP de la máquina. Este fichero **no tienes que modificarlo**.

Realiza los cambios que creas convenientes en los siguientes ficheros: `variables.tf` para ajustar las variables, `cloud-init/server1/user-data.yaml` para cambiar la configuración de la máquina, por ejemplo **indicar tu clave pública** y `main.tf` por si quieres cambiar la imagen base, cambiar la memoria o cpus o conectarlo a otra red.

Una vez hecho los cambios, **los comandos se ejecutan en el directorio del proyecto**:

* Ejecutamos **una sola vez** el comando `tofu init` para instalar el plugin del provider.
* Ahora podemos ejecutar el comando `tofu plan` para ver las acciones que se van realizar: creaciones, modificaciones, ...
* Para indicar que aplique el escenario descrito ejecutamos `tofu apply`, nos muestra las acciones que va a realizar y espera que le indiquemos `yes` para continuar.
* Una vez creado el escenario os saldrá la información que definimos en el fichero `output.tf`. Esta información siempre se puede mostrar ejecutando `tofu output`.
* Ya está funcionando el escenario, podemos ver el estado de los recurso ejecutando `tofu show`.
* Una vez que termine de trabajar con el escenario puede eliminar todos los recursos creados, ejecutando `tofu destroy`.

{% capture notice-text %}
## ¿Qué tienes que entregar?

1. Configura tu escenario de forma adecuada para crear una máquina virtual con debian13. Conecta por ssh con la máquina. Destruye el escenario.
2. Modifica los ficheros necesarios para crear una máquina virtual con ubuntu: `cloud-init/server1/user-data.yaml` y `main.tf`. Conecta por ssh con la máquina. Destruye el escenario.
{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>

## Ejemplo 2: Máquina virtual con disco adicional

Este ejemplo es similar al anterior, pero en esta ocasión la máquina virtual tiene un disco adicional de 1Gb. En este caso en el fichero `main.tf` se declaran 4 recursos:

* El disco principal de la máquina virtual creado con clonación enlazada.
* El disco ISO con el fichero para configurar el cloud-init.
* Un disco adicional de 1Gb que se conectará con la máquina virtual
* La máquina virtual que tiene dos parámetros `disk` donde se especifican los dos discos: el principal y el extra.

{% capture notice-text %}
## ¿Qué tienes que entregar?

1. Modifica el fichero `main.tf` para crear otro disco de 5Gb y añadirlo a la máquina virtual.
2. Acceder a la máquina virtual por ssh y comprobar con `lsblk` los discos que se han añadido.
3. Destruye el escenario.
{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>


## Ejemplo 3: Máquina virtual conectada a dos redes con DHCP

En este ejemplo vamos a comenzar a trabajar con las redes. En los dos ejemplos anteriores habíamos conectado la máquina virtual a una red no gestionada por OpenTofu. En este ejemplo vamos a crear redes gestionadas por OpenTofu, que se crearan con `tofu apply` y de eliminaran con `tofu destroy`.

Hemos añadido el fichero `networks.tf` donde se van a definir las redes. En este caso:

* Se crea una red NAT con DHCP con el recurso `resource "libvirt_network" "nat_dhcp"`. Estudia los distintos parámetros que hemos indicado.
* Tienes comentado la definición de otros tipos de redes por si en otro ejercicio las quieres definir.
* recuerda que en un escenario puedes crear las redes que quieras.

A continuación estudia la definición del recurso de la máquina virtual en el fichero `main.tf` y comprueba que la máquina está conectada a dos redes. Recuerda que cuando conectamos a un red con servidor DHCP indicamos el parámetro `wait_for_lease = true`.

* Cuando la red no es creada por OpenTofu, por ejemplo `default` indicamos el nombre con el parámetro `network_name`.
* Cuando la red es gestionada por OpenTofu, indicamos su id con el parámetro ` network_id`, por ejemplo: `network_id = libvirt_network.nat-dhcp.id`

El hecho de que conectemos una máquina virtual a dos redes **no significa que netplan configure las dos interfaces**. Tenemos que configurarlo nosotros, para ello:

* Creamos el fichero `cloud-init/server1/network-config.yaml` donde guardaremos la configuración netplan de la máquina.
* Añadimos este fichero en la imagen ISO junto al fichero `cloud-init/server1/user-data.yaml`. Esto se hace con el parámetro `network_config` del recurso `resource "libvirt_cloudinit_disk" "server1-cloudinit"` en el fichero `main.tf`.

Finalmente hemos modificado el fichero `output.tf`para que muestre las dos ip.


{% capture notice-text %}
## ¿Qué tienes que entregar?

1. Configura tu escenario de forma adecuada y créalo. Conecta por ssh con la máquina. Comprueba con `ip a` que está conectado a dos redes. Destruye ekl escenario.
2. Crea una nueva red de tipo NAT con servidor DHCP. Modifca la definición de la máquina para conectarla a esta nueva red. Modifca la configuraciónd e red (fichero `cloud-init/server1/network-config.yaml`) para configurar la tercera interfaz y finalmente modifica el fichero `output.tf` para que salga información de la tercera IP. 
3. Crea el escenario, comprueba que la máquina tiene 3 interfaces configuras. Destruye el escenario.
{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>


