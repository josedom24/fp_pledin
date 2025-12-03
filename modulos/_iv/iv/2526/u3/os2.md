---
title: "Clase 4: Creación de una instancia desde el CLI"
---

## Conceptos previos

* **Imagen**: Plantilla cloud con un sistema operativo con la configuración mínima para poder operar adecuadamente dentro de una nube de infraestructura.
* **Instancia**: Servidor virtual que se ejecuta dentro de la nube de infraestructura y que se basa en una imagen, de hecho una instancia es inicialmente un clon de una imagen.
* **Tipo de instancia o sabor**: Define las características de la instancia, como el número de cores virtuales (vCPU), cantidad de memoria RAM o tamaño del disco duro del sistema operativo.
* **IP fija**: Dirección IP interna de la instancia y que se define en el momento de la creación de la instancia. La dirección IP fija se utiliza para la comunicación interna de la instancia y su valor no varía durante la vida de la instancia, de ahí que reciba el nombre de IP fija.
* **IP flotante**: Dirección IP que se asigna a una instancia después de crearla y que se utiliza para la comunicación desde el exterior. No todas las instancias tienen por qué tener una IP flotante.
* **Grupo de Seguridad (Cortafuegos)**: Conjunto de reglas de iptables que actúan como cortafuegos a nivel de la instancia.

## Gestión de instancias con OpenStack client 

Para crear una instancia podemos ejecutar:

```
openstack server create --flavor m1.normal \
--image "Debian 13 Trixie" \
--security-group default \
--key-name clave_jdmr \
--network "Red de josedom" \
instancia_prueba
```

Para trabajar con IP flotantes, podemos ejecutar las siguientes instrucciones:

* Para ver las IP flotantes reservadas: `openstack floating ip list`.
* Para solicitar otra ip flotante: `openstack floating ip create ext-net`.
* Para asignar una ip flotante a nuestra instancia: `openstack server add floating ip instancia_prueba 172.22.201.111`
* Quitar IP flotante de una instancia: `openstack server remove floating ip instancia_prueba 72.22.201.111`

## Gestión de la instancia

Los comandos más importantes son:

* Listar todas las instancias: `openstack server list`.
* Ver información detallada de la instancia: `openstack server show instancia_prueba`.
* Iniciar la instancia (si está detenida): `openstack server start instancia_prueba`.
* Detener la instancia: `openstack server stop instancia_prueba`.
* Reiniciar la instancia (soft reboot): `openstack server reboot instancia_prueba`.
* Reinicio forzado (hard reboot): `openstack server reboot --hard instancia_prueba`.
* Suspender la instancia: `openstack server suspend instancia_prueba`.
* Reanudar una instancia suspendida: `openstack server resume instancia_prueba`.
* Poner la instancia en hibernación: `openstack server shelve instancia_prueba`.
* Reactivar una instancia hibernada: `openstack server unshelve instancia_prueba`.
* Eliminar la instancia: `openstack server delete instancia_prueba`.


## Configuración de instancias con cloud-init

**cloud-init**: cloud instance initialization**, es un programa que permite realizar la configuración de la instancia al crearse a partir de una imagen. Es el estándar de facto en nube pública o privada, está desarrollado en python y es un proyecto liderado por Canonical.

El paquete `cloud-init` está instalado habitualmente en las imágenes para IaaS. [Documentación cloud-init](https://cloudinit.readthedocs.io).

Una instancia que se inicia o reinicia, puede obtener diferentes tipos de datos, en función del origen de estos:
* **Metadatos**: Obtenidos del **servidor de metadatos** del proveedor de nube (típicamente a través de dirección de enlace local `http://169.254.169.254`). Incluye las características propias de la instancia: nombre, configuración de red, tamaño de los discos, etc.
* **Datos de usuario (opcional)**: Datos adicionales de configuración que proporciona el usuario de la instancia (**user-data**).
* **Datos del proveedor (opcional)**: Datos adicionales de configuración proporcionados por el proveedor (**vendor-data**).

Veamos un ejemplo de un script cloud-config guardado en un fichero `cloud-config.yaml`:

```yaml
#cloud-config
# Actualiza los paquetes
package_update: true
package_upgrade: true
# Instala el paquete apache2
packages:
  - apache2
# Configura el hostname y el fqdn
fqdn: maquina.example.org
hostname: maquina
manage_etc_hosts: true
# Crear dos usuarios, configura el acceso por sudo y añade clave pública ssh
users:
  - name: debian
    sudo: ALL=(ALL) NOPASSWD:ALL
    groups: users, admin
    shell: /bin/bash
    ssh-authorized-keys:
      - ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCmjoVIoZCx4QFXvljqozXGqxxlSvO7V2aizqyPgMfGqnyl0J9YXo6zrcWYwyWMnMdRdwYZgHqfiiFCUn2QDm6ZuzC4Lcx0K3ZwO2lgL4XaATykVLneHR1ib6RNroFcClN69cxWsdwQW6dpjpiBDXf8m6/qxVP3EHwUTsP8XaOV7WkcCAqfYAMvpWLISqYme6e+6ZGJUIPkDTxavu5JTagDLwY+py1WB53eoDWsG99gmvyit2O1Eo+jRWN+mgRHIxJTrFtLS6o4iWeshPZ6LvCZ/Pum12Oj4B4bjGSHzrKjHZgTwhVJ/LDq3v71/PP4zaI3gVB9ZalemSxqomgbTlnT jose@debian
# Cambia las contraseña a los usuarios creados
chpasswd:
  expire: False
  users:
    - name: debian
      password: asdasd
      type: text
    - name: root
      password: password
      type: text
```

Usando la línea de comandos, se indica el fichero de configuración en el parámetro `--user-data`:

```
openstack server create --flavor m1.normal \
    --image "Debian 13 Trixie" \
    --security-group default \
    --key-name clave_jdmr \
    --network "Red de josedom" \
    --user-data cloud-config.yaml
instancia_prueba
```

**IMPORTANTE**: Si conectamos una instancia a una red sin DHCP, no tendrá direccionamiento y no podrá conectarse al servidor de metadatos, por lo que no se podrá configurar con **cloud-init**. En este caso debemos usar otra estrategia: guardar el fichero `cloud-config.yaml` en un CDROM para que lo lea la instancia, para ello en la creación de la instancia usaremos el parámetro: `--config-drive True`.

{% capture notice-text %}
## Ejercicio

1. Crea una instancias Linux, con las siguientes características configuradas con cloud-init:
    * Al iniciarse se deben actualizar los paquetes.
    * Se debe instalar Apache2.
    * Se debe crear un usuario (con tu nombre) y contraseña.
    * Se debe configurar el fqdn a maquina1.example.org.
2. Muestra tus ips flotantes. Solicita una nueva y asígnala a la instancia.
3. Accede por ssh a la instancia que has creado.
4. Para la instancia, arrancala de nuevo y finalmente elimínala.
{% endcapture %}<div class="notice--warning">{{ notice-text | markdownify }}</div>


## Snapshot de instancias

En OpenStack, las *instantáneas de instancias* se gestionan principalmente desde **Nova (Compute)**. Cuando haces un snapshot de una instancia:

* Nova detiene brevemente la VM (o sincroniza el disco en caliente si lo permite).
* Crea una **imagen nueva en Glance** con el contenido del disco raíz.

Es decir: el snapshot **es una imagen en Glance**, no una copia “incremental” ni un backup directo de los volúmenes.

* Para crea una instantánea de una instancia: `openstack server image create --name snapshot-instancia instancia_prueba`
* Para ver la instantánea creada: `openstack image list`.
    *  En la columna `Status` verás `active` cuando esté lista para usar.
* Ver detalles de un snapshot: `openstack image show snapshot-instancia`
* Eliminar un snapshot: `openstack image delete snapshot-instancia`

Si queremos crear una nueva instancia a partir de un snapshot:

```bash
openstack server create --flavor m1.normal \
    --image "snapshot-instancia" \
    --security-group default \
    --network "Red de josedom" \
instancia_prueba2
```

{% capture notice-text %}
## Ejercicio

1. Crea una instantánea de la máquina que has creado.
2. Crea una nueva máquina a partir de la instantánea y comprueba que tiene la misma configuración (apache2, usuario,...).
{% endcapture %}<div class="notice--warning">{{ notice-text | markdownify }}</div>
