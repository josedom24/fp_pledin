---
title: "Clase 4: Introducción a terraform + libvirt"
---

## ¿Qué vas a aprender en esta clase?

* El concepto de orquestador de escenarios.

## Teoría

### Imágenes Cloud

Podemos crear máquinas virtuales de forma automática es el uso de **imágenes cloud** (plantillas) junto con **cloud-init**, una herramienta diseñada para la inicialización y configuración automática de instancias en su primer arranque. Puedes ver un ejemplo en el apartado:

* [Despliegue automatizado de máquinas virtuales usando cloud-init](https://github.com/josedom24/curso_kvm_ow/blob/main/curso2/contenidos/unidad07/clase3.md)

### ¿Qué es Terraform?

**Terraform** es una herramienta de **Infraestructura como Código (IaC)** desarrollada por HashiCorp.
Permite **definir, crear y administrar infraestructura** (máquinas virtuales, redes, contenedores, etc.) usando archivos de texto declarativos (`.tf`).

En lugar de crear recursos manualmente, describes **qué infraestructura quieres**, y Terraform se encarga de **construirla, modificarla o destruirla** de forma reproducible.

### ¿Qué es un *provider*?

Un **provider** (proveedor) es un **plugin** que permite a Terraform interactuar con una plataforma o tecnología concreta.
Cada provider sabe cómo crear, leer, actualizar y eliminar recursos.

Ejemplos:

* `aws` → Amazon Web Services
* `azurerm` → Microsoft Azure
* `libvirt` → Máquinas virtuales locales con KVM
* `docker` → Contenedores Docker

En el caso de **libvirt**, el provider permite a Terraform crear y gestionar VMs en tu sistema KVM local.

### Comandos más importantes de Terraform

| Comando              | Descripción                                                                     |
| -------------------- | ------------------------------------------------------------------------------- |
| `terraform init`     | Inicializa el proyecto, descarga los *providers* y prepara el entorno.          |
| `terraform plan`     | Muestra qué acciones realizará Terraform (sin aplicar cambios).                 |
| `terraform apply`    | Aplica los cambios: crea, modifica o elimina recursos según los archivos `.tf`. |
| `terraform destroy`  | Elimina todos los recursos gestionados por el proyecto.                         |
| `terraform validate` | Verifica que la sintaxis de los archivos `.tf` sea correcta.                    |
| `terraform show`     | Muestra el estado actual de los recursos creados.                               |
| `terraform output`   | Muestra los valores definidos en bloques `output`.                              |

### Instalación de terraform

```
wget -O - https://apt.releases.hashicorp.com/gpg | sudo gpg --dearmor -o /usr/share/keyrings/hashicorp-archive-keyring.gpg
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/hashicorp-archive-keyring.gpg] https://apt.releases.hashicorp.com $(grep -oP '(?<=UBUNTU_CODENAME=).*' /etc/os-release || lsb_release -cs) main" | sudo tee /etc/apt/sources.list.d/hashicorp.list
sudo apt update && sudo apt install terraform
```

## Ejercicios

1. Vamos a descargar la imágenes cloud con la que vamos a trabajar. La vamos a copiar en el directorio correspondiente al pool `default`:

  ```
  cd /var/lib/libvirt/images
  sudo wget https://cloud.debian.org/images/cloud/trixie/daily/latest/debian-13-genericcloud-amd64-daily.qcow2 -O debian13-base.qcow2
  sudo wget https://cloud-images.ubuntu.com/noble/20251001/noble-server-cloudimg-amd64.img -O ubuntu2404-base.qcow2
  ```

  Las imágenes bases se llaman `debian13-base.qcow2` y `ubuntu2404-base.qcow2`.

2. Instala terraform y haz un fork del repositorio de ejemplos: [https://github.com/josedom24/terraform-libvirt/](https://github.com/josedom24/terraform-libvirt/).

### Ejemplo 1: Máquina virtual conectada a la red "default"

Empezamos a trabajar en el directorio`ejemplo1`. En este ejemplo vamos a crear un máquina virtual conectada a la red `default`. Terraform trabaja con fichero **tf** que se pueden llamar como queremos. Veamos los ficheros con los que vamos a trabajar:

* `provider.tf`: Configura el provider que vamos a usar y lo configura. El plugin del provider se instala en el directorio `.terraform` cuando ejecutamos `terraform init`. Este comando **sólo se ejecuta una vez**. Este fichero **noo hay que modificarlo**.
* `variables.tf`: Se declaran variables globales, que podemos usar en nuestras definiciones. En este caso se definen:
  * `var.libvirt_pool_name`: donde guardamos el nombre del pool en el que queremos crear la máquina virtual. Su valor por defecto es `default`.
  * `var.libvirt_pool_path`: donde se guarda el directorio correspondiente al pool `default`, normalmente es `/var/lib/libvirt/images`. 
  Este fichero **se modifica una vez** indicando vuestros datos particulares.
* `cloud-init/server1/user-data.yaml`: Fichero para configurar la máquina virtual con el mecanismo de cloud-init. En este ejemplo:
  * Se indica el hostnmae.
  * Se configura el usuario `debian` y se lo pone una contraseña.
  * Se ejecuta una `apt update`.
  * Se instalan los paquetes y se hace la configuración necesaria para que el teclado este en español cuando accedemos a la máquina.
* `server1.tf`: Aquí está la definición de los recursos con los que queremos trabajar. Los recursos se definen con el parámetro `resource "<tipo del recurso>" "<nombre del recurso>"`. El nombre del recurso debe ser único. Cada tipo de recurso tiene un conjunto de parámetros. En este fichero se definen los siguiente recursos:
  * `resource "libvirt_volume" "server1-disk"`: Un volumen creado con clonación enlazada cuya imagen base está indicado con el parámetro `base_volume_id`. Este volumen se crea en el pool indicado en la variable `var.libvirt_pool_name`.
  * `resource "libvirt_cloudinit_disk" "server1-cloudinit"`: Un disco con formato ISO donde se guarda el fichero de configuración de cloud-init.
  * `resource "libvirt_domain" "server1"`: Una máquina virtual, donde se indica el nombre, la memoria, el número de CPUs, la red a la que está conectada y los discos que tiene.
      * Cuando la red a la que está conectada tiene un servidor DHCP, se indica el parámetro `wait_for_lease = true` que indica que se considera que la máquina está funcionando cuando recibe direccionamiento del servidor DHCP. 
* `output.tf`: Se define la información que se mostrará al terminar de crear el escenario. En este caso nos muestra el nombre y la dirección IP de la máquina. Este fichero **no tienes que modificarlo**.

Realiza los cambios que creas convenientes en los siguientes ficheros: `variables.tf` para ajustar las variables, `cloud-init/server1/user-data.yaml` para cambiar la configuración de la máquina, por ejemplo **indicar tu clave pública** y `server1.tf` por si quieres cambiar la imagen base, cambiar la memoria o cpus o conectarlo a otra red.

Una vez hecho los cambios, **los comandos se ejecutan en el directorio del proyecto**:

* Ejecutamos **una sola vez** el comando `terraform init` para instalar el plugin del provider.
* Ahora podemos ejecutar el comando `terraform plan` para ver las acciones que se van realizar: creaciones, modificaciones, ...
* Para indicar que aplique el escenario descrito ejecutamos `terraform apply`, nos muestra las acciones que va a realizar y espera que le indiquemos `yes` para continuar.
* Una vez creado el escenario os saldrá la información que definimos en el fichero `output.tf`. Esta información siempre se puede mostrar ejecutando `terraform output`.
* Ya está funcionando el escenario, podemos ver el estado de los recurso ejecutando `terraform show`.
* Una vez que termine de trabajar con el escenario puede eliminar todos los recursos creados, ejecutando `terraform destroy`.

{% capture notice-text %}
## ¿Qué tienes que entregar?

1. Configura tu escenario de forma adecuada para crear una máquina virtual con debian13. Conecta por ssh con la máquina. Destruye el escenario.
2. Modifica los ficheros necesario para crear una máquina virtual con ubuntu. Utiliza el fichero `cloud-init/server1/user-data-ubuntu.yaml` para configurar la máquina. Conecta por ssh con la máquina. Destruye el escenario.
{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>

## Ejemplo 2: Máquina virtual con disco adicional

Este ejemplo es similar al anterior, pero en esta ocasión la máquina virtual tiene un disco adicional de 1Gb. En este caso en el fichero `server1.tf` se declaran 4 recursos:

* El disco principal de la máquina virtual creado con clonación enlazada.
* El disco ISO con el fichero para configurar el cloud-init.
* Un disco adicional de 1Gb que se conectará con la máquina virtual
* La máquina virtual que tiene dos parámetros `disk` donde se especifican los dos discos: el principal y el extra.

{% capture notice-text %}
## ¿Qué tienes que entregar?

1. Modifica el fichero `server1.tf` para crear otro disco de 5Gb y añadirlo a la máquina virtual.
2. Acceder a la máquina virtual por ssh y comprobar con `lsblk` los discos que se han añadido.
3. Destruye el escenario.
{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>


## Ejemplo 3: Máquina virtual conectada a dos redes con DHCP

En este ejemplo vamos a comenzar a trabajar con las redes. En los dos ejemplos anteriores habíamos conectado la máquina virtual a una red no gestionada por terraform. En este ejemplo vamos a crear redes gestionadas por terraform, que se crearan con `terraform apply` y de eliminaran con `terraform destroy`.

Hemos añadido el fichero `networks.tf` donde se van a definir las redes. En este caso:

* Se crea una red NAT con DHCP con el recurso `resource "libvirt_network" "nat_dhcp"`. Estudia los distintos parámetros que hemos indicado.
* Tienes comentado la definición de otros tipos de redes por si en otro ejercicio las quieres definir.
* recuerda que en un escenario puedes crear las redes que quieras.

A continuación estudia la definición del recurso de la máquina virtual en el fichero `server1.tf` y comprueba que la máquina está conectada a dos redes. Recuerda que cuando conectamos a un red con servidor DHCP indicamos el parámetro `wait_for_lease = true`.

El hecho de que conectemos una máquina virtual a dos redes **no significa que netplan configure las dos interfaces**. Tenemos que configurarlo nosotros, para ello:

* Creamos el fichero `cloud-init/server1/network-config.yaml` donde guardaremos la configuración netplan de la máquina.
* Añadimos este fichero en la imagen ISO junto al fichero `cloud-init/server1/user-data.yaml`. Esto se hace con el parámetro `network_config` del recurso `resource "libvirt_cloudinit_disk" "server1-cloudinit"` en el fichero `server1.tf`.

Finalmente hemos modificado el fichero `output.tf`para que muestre las dos ip.


{% capture notice-text %}
## ¿Qué tienes que entregar?

1. Configura tu escenario de forma adecuada y créalo. Conecta por ssh con la máquina. Comprueba con `ip a` que está conectado a dos redes. Destruye ekl escenario.
2. Crea una nueva red de tipo NAT con servidor DHCP. Modifca la definición de la máquina para conectarla a esta nueva red. Modifca la configuraciónd e red (fichero `cloud-init/server1/network-config.yaml`) para configurar la tercera interfaz y finalmente modifica el fichero `output.tf` para que salga información de la tercera IP. 
3. Crea el escenario, comprueba que la máquina tiene 3 interfaces configuras. Destruye el escenario.
{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>
