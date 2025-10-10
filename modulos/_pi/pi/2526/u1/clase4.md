---
title: "Clase 4: Introducción a terraform + libvirt"
---

## ¿Qué vas a aprender en esta clase?

* El concepto de orquestador de escenarios.

## Teoría

* [Despliegue automatizado de máquinas virtuales usando cloud-init](https://github.com/josedom24/curso_kvm_ow/blob/main/curso2/contenidos/unidad07/clase3.md)

## Recursos

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


* **Flujo típico**:

  ```bash
  terraform init
  terraform plan
  terraform apply
  terraform destroy
  ```

### Ficheros de un proyecto Terraform

| Archivo          | Propósito principal          | Ejemplo                          |
| ---------------- | ---------------------------- | -------------------------------- |
| **provider.tf**  | Conexión con el entorno      | Configura `libvirt`, `aws`, etc. |
| **variables.tf** | Parámetros configurables     | Memoria, CPU, nombre, etc.       |
| **main.tf**      | Define los recursos a crear  | Máquinas, redes, volúmenes       |
| **output.tf**    | Muestra información al final | IP, nombre, rutas, etc.          |


## Ejemplo completo con backing store

Estructura:

```
terraform-debian13-linkedclone/
├── provider.tf
├── main.tf
├── cloud-init.cfg
└── output.tf
```

---

### `provider.tf`

```hcl
terraform {
  required_providers {
    libvirt = {
      source  = "dmacvicar/libvirt"
      version = "0.7.6"
    }
  }
}

provider "libvirt" {
  uri = "qemu:///system"
}
```

---

### `main.tf`

```hcl
# Imagen base: Debian 13 Trixie (cloud image oficial)
resource "libvirt_volume" "debian13_base" {
  name   = "debian13-base.qcow2"
  pool   = "default"
  source = "https://cloud.debian.org/images/cloud/trixie/daily/latest/debian-13-genericcloud-amd64-daily.qcow2"
  format = "qcow2"
}

# Clon ligero (backing store)
# El disco resultante apunta al volumen base y solo guarda cambios diferenciales
resource "libvirt_volume" "debian13_clone" {
  name            = "debian13-linked.qcow2"
  pool            = "default"
  base_volume_id  = libvirt_volume.debian13_base.id
  format          = "qcow2"
}

# Disco cloud-init con configuración del sistema
resource "libvirt_cloudinit_disk" "cloudinit" {
  name           = "debian13-cloudinit.iso"
  pool           = "default"
  user_data      = file("${path.module}/cloud-init.cfg")
  network_config = ""
}

# Dominio (VM)
resource "libvirt_domain" "debian13_vm" {
  name   = "debian13-vm"
  memory = 2048
  vcpu   = 2

  network_interface {
    network_name = "default"
  }

  disk {
    volume_id = libvirt_volume.debian13_clone.id
  }

  cloudinit = libvirt_cloudinit_disk.cloudinit.id

  console {
    type        = "pty"
    target_port = "0"
  }

  graphics {
    type        = "spice"
    listen_type = "none"
  }

  boot_device {
    dev = ["hd"]
  }
}
```



### `cloud-init.cfg`

```yaml
#cloud-config
hostname: debian13-vm
users:
  - name: debian
    sudo: ALL=(ALL) NOPASSWD:ALL
    groups: users, admin
    shell: /bin/bash
    ssh-authorized-keys:
      - ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQ...TU_CLAVE_SSH...
package_update: true
packages:
  - qemu-guest-agent
runcmd:
  - echo "Bienvenido a Debian 13 (Trixie) con Terraform (clon ligado)" > /etc/motd
```



### `output.tf`

```hcl
data "libvirt_domain" "debian13_info" {
  name = libvirt_domain.debian13_vm.name
}

output "vm_info" {
  value = <<EOT
✅ Máquina Debian 13 (Trixie) creada con clonación ligada (backing store)

Nombre: ${libvirt_domain.debian13_vm.name}
Disco:  ${libvirt_volume.debian13_clone.name} (ligado a ${libvirt_volume.debian13_base.name})
Memoria: ${libvirt_domain.debian13_vm.memory} MB
vCPUs:   ${libvirt_domain.debian13_vm.vcpu}

Para conectarte:
  virsh domifaddr ${libvirt_domain.debian13_vm.name}
  ssh debian@<IP_mostrada>

EOT
}
```



## 📦 Verificación del *backing store*

Cuando Terraform termine, puedes comprobar que la clonación es **ligada** (no copia completa):

```bash
qemu-img info /var/lib/libvirt/images/debian13-linked.qcow2
```

Deberías ver algo así:

```
image: /var/lib/libvirt/images/debian13-linked.qcow2
file format: qcow2
virtual size: 2G (2147483648 bytes)
backing file: /var/lib/libvirt/images/debian13-base.qcow2
```

Eso confirma que la VM usa un **backing file**, igual que las “linked boxes” de Vagrant.




## Ejercicio