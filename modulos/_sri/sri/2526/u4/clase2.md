---
title: "Protocolo iSCSI"
---

iSCSI (Internet Small Computer Systems Interface) es un protocolo que permite enviar comandos SCSI a través de una red TCP/IP. En la práctica, permite acceder a discos remotos como si fueran dispositivos de bloque locales. El objetivo principal de iSCSI es ofrecer **almacenamiento en red (SAN)** utilizando una red Ethernet estándar, sin necesidad de hardware especializado.

En una arquitectura iSCSI existen dos roles principales:

* **Servidor iSCSI (Target)**: equipo que ofrece dispositivos de almacenamiento.
* **Cliente iSCSI (Initiator)**: equipo que se conecta a esos dispositivos y los usa como si fueran discos locales.

iSCSI utiliza el **puerto TCP 3260** para la comunicación entre el iniciador y el target.

El funcionamiento general es:

1. El servidor define uno o varios **targets**, cada uno de los cuales puede contener una o más unidades lógicas (**LUNs**).
2. El cliente se conecta al target utilizando su **IQN** (*iSCSI Qualified Name*), descubre los recursos disponibles y los monta.
3. Una vez conectado, el cliente verá los LUNs como dispositivos de bloque estándar (por ejemplo, `/dev/sdb`), que podrá formatear y montar normalmente.

## Instalación del servidor iSCSI

En el servidor (que dispone del disco o dispositivo que se desea compartir):

```bash
sudo apt update
sudo apt install tgt
```

El servicio principal se llama **tgtd** y gestiona los targets iSCSI.

## Configuración manual de un target

Creamos un target llamado `target1` con el identificador IQN `iqn.2021-11.org.example:target1`:

```bash
sudo tgtadm --lld iscsi --op new --mode target --tid 1 -T iqn.2021-11.org.example:target1
```

Asociamos un dispositivo físico (por ejemplo `/dev/vdb`) como LUN:

```bash
sudo tgtadm --lld iscsi --op new --mode logicalunit --tid 1 --lun 1 -b /dev/vdb
```

Permitimos el acceso al target desde todas las interfaces de red:

```bash
sudo tgtadm --lld iscsi --op bind --mode target --tid 1 -I ALL
```

Para verificar la configuración:

```bash
sudo tgtadm --lld iscsi --op show --mode target
```

## Hacer la configuración persistente

Por defecto, las configuraciones hechas con `tgtadm` no son persistentes. Podemos guardarlas con `tgt-admin` para que se carguen automáticamente al iniciar el servicio:

```bash
sudo tgt-admin --dump > /etc/tgt/conf.d/example.conf
```

Al reiniciar el servidor, el target se creará automáticamente a partir de este archivo.

## Instalación del cliente iSCSI

En el cliente (que accederá al disco remoto):

```bash
sudo apt update
sudo apt install open-iscsi
```

Durante la instalación se crea automáticamente un identificador único para el iniciador en el archivo `/etc/iscsi/initiatorname.iscsi`. Este nombre se utiliza para identificar el cliente frente al servidor.

## Descubrimiento y conexión al target

Primero descubrimos los targets que ofrece el servidor (en este ejemplo, `10.0.0.1`):

```bash
sudo iscsiadm --mode discovery --type sendtargets --portal 10.0.0.1
```

Conectamos al target mostrado (por ejemplo `iqn.2021-11.org.example:target1`):

```bash
sudo iscsiadm --mode node -T iqn.2021-11.org.example:target1 --portal 10.0.0.1 --login
```

Una vez conectado, el cliente verá un nuevo dispositivo de bloque, por ejemplo `/dev/sdb`. Podemos formatearlo y montarlo como cualquier otro disco local.

## Conexión automática tras reinicio

Para que el cliente se conecte automáticamente al arrancar:

```bash
sudo iscsiadm -m node -T iqn.2021-11.org.example:target1 -p 10.0.0.1 --op update -n node.startup -v automatic
```

## Gestión de sesiones y desconexión

Ver las sesiones activas:

```bash
sudo iscsiadm -m session
```

Desconectarse de un target:

```bash
sudo iscsiadm -m node -T iqn.2021-11.org.example:target1 -p 10.0.0.1 -u
```

Desconectarse de todos los targets:

```bash
sudo iscsiadm -m node -p 10.0.0.1 --logout
```

## Autenticación

Si el servidor requiere autenticación **CHAP**, se configura en el cliente después de la conexión:

```bash
sudo iscsiadm --mode node -T iqn.2021-11.org.example:target1 --portal 10.0.0.1 -o update \
  -n node.session.auth.username -v usuario

sudo iscsiadm --mode node -T iqn.2021-11.org.example:target1 --portal 10.0.0.1 -o update \
  -n node.session.auth.password -v contraseña
```
