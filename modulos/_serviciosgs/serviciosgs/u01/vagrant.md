---
title: Introducción a vagrant
permalink: /serviciosgs/u01/vagrant.html
---

Vagrant es una aplicación libre desarrollada en ruby que nos permite crear y personalizar entornos de desarrollo livianos, reproducibles y portables. Vagrant nos permite automatizar la creación y gestión de máquinas virtuales. Las máquinas virtuales creadas por vagrant se pueden ejecutar con distintos gestores de máquinas virtuales (oficialmente VirtualBox, VMWare e Hyper-V), en nuestro ejemplo vamos a usar máquinas virtuales en VirtualBox.

El objetivo principal de vagrant es aproximar los entornos de desarrollo y producción, de esta manera el desarrollador tiene a su disposición una manera  muy sencilla de desplegar una infraestructura similar a la que se va a tener en entornos de producción. A los administradores de sistemas les facilita la creación de infraestructuras de prueba y desarrollo.

[Presentación: Vagrant y ansible. Una combinación explosiva (1ª parte)](http://iesgn.github.io/cloud/curso/u2/presentacion_vagrant)

## Práctica con vagrant

### Práctica 1: Instalación de vagrant

Instalar virtualbox y vagrant (en Debian Buster lo podemos instalar de repositorios, si queremos la última versión lo podemos descargar desde la [página oficial](https://www.vagrantup.com/downloads.html).):

```bash
root@maquina:~$ apt install virtualbox-6.0 vagrant
```

### Práctica 2: Instalación de un "box" debian/buster

Nos descargamos desde el repositorio oficial el box de Debian buster de 64 bits, esto lo hacemos un usuario sin privilegios:

```bash
usuario@maquina:~$ vagrant box add debian/buster64
```

Si el box lo tenemos en la *nas* de nuestro instituto (o en otro servidor web):

```bash
usuario@maquina:~$ vagrant box add debian/buster64 http://nas.gonzalonazareno.org/...
```

**Es importante fijarnos que lo estamos haciendo con usuarios sin privilegios. Cada usuario tendrás sus box propios.**
{: .notice--warning}        

Puedo ver la lista de boxes que tengo instalada en mi usuario ejecutando la siguiente instrucción:
    
```bash
usuario@maquina:~$ vagrant box list
```

### Práctica 3: Creación de una máquina virtual

1. Nos creamos un directorio y dentro vamos a crear el fichero Vagrantfile, podemos crear uno vacío con la instrucción:
        
    ```bash
    usuario@maquina:~/vagrant$ vagrant init
    ```
        
2. Modificamos el fichero Vagrantfile y los dejamos de la siguiente manera:

    ```ruby
    # -*- mode: ruby -*-
    # vi: set ft=ruby :
    Vagrant.configure("2") do |config|
                config.vm.box = "debian/buster64"
                config.vm.hostname = "mimaquina"
                config.vm.network :public_network,:bridge=>"eth0"
    end    
    ```
    
3. Iniciamos la máquina:

    ```bash
    usuario@maquina:~/vagrant$ vagrant up
    ```
        
4. Para acceder a la instancia:
  	
    ```bash
    usuario@maquina:~/vagrant$ vagrant ssh default
    ```
    	      
5. Suspender, apagar o destruir:
    	
    ```bash
    usuario@maquina:~/vagrant$ vagrant suspend
    usuario@maquina:~/vagrant$ vagrant halt
    usuario@maquina:~/vagrant$ vagrant destroy
    ```
{% capture notice-text %}
## Ejercicios

1. Entra en virtualbox y comprueba las características de la máquina que se ha creado.
2. ¿Qué usuario tiene creado por defecto el sistema?¿Cómo se ejecutan instrucciones de superusuario?
3. ¿Cuantas tarjetas de red tiene?¿Para qué sirve la eth0?
4. Investiga el funcionamiento de la instrucción ``vagrant ssh``. ¿Por que interfaz se conecta? ¿Qué certificado se utiliza para acceder?
{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>

### Práctica 4: Creación de varias máquinas virtuales

En esta ocasión vamos a crear otro directorio y dentro un fichero Vagrantfile con el siguiente contenido:

```ruby
# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|

  config.vm.define :nodo1 do |nodo1|
    nodo1.vm.box = "debian/buster64"
    nodo1.vm.hostname = "nodo1"
    nodo1.vm.network :private_network, ip: "10.1.1.101"
  end
  config.vm.define :nodo2 do |nodo2|
    nodo2.vm.box = "debian/buster64"
    nodo2.vm.hostname = "nodo2"
    nodo2.vm.network :public_network,:bridge=>"eth0"
    nodo2.vm.network :private_network, ip: "10.1.1.102"
  end
end
```

Cuando iniciemos el escenario veremos que hemos creado dos máquinas virtuales: nodo1 y nodo2. 
nodo1 tendrá una red interna con ip 10.1.1.101, y nodo2 tendrá una interfaz de red "modo puente" y una interfaz de red del tipo red interna con ip 10.1.1.102.

Si accedemos por ssh a nodo1 podremos hacer ping a nodo2.


### Práctica 5: Añadir un dico duro adicional y modificar la RAM a una máquina virtual

Por últimos vamos a crear un nuevo Vagranfile en un nuevo directorio con este contenido:

```ruby
# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|

  config.vm.define :nodo1 do |nodo1|
    nodo1.vm.box = "debian/buster64"
    nodo1.vm.hostname = "nodo1"
    nodo1.vm.network :private_network, ip: "10.1.1.101"
    nodo1.vm.provider :virtualbox do |v|
                    v.customize ["modifyvm", :id, "--memory", 768]
            end

  end

  disco = '.vagrant/midisco.vdi'
  config.vm.define :nodo2 do |nodo2|
    nodo2.vm.box = "debian/buster64"
    nodo2.vm.hostname = "nodo2"
    nodo2.vm.network :public_network,:bridge=>"eth0"
    nodo2.vm.network :private_network, ip: "10.1.1.102"
    nodo2.vm.provider :virtualbox do |v|
                    v.customize ["createhd", "--filename", disco, "--size", 1024]
                    v.customize ["storageattach", :id, "--storagectl", "SATA Controller",
                     "--port", 1, "--device", 0, "--type", "hdd",
                     "--medium", disco]
                    end
    end
end
```

Como podemos ver al `nodo1` le hemos modificado el tamaño de la memoria RAM y en el `nodo2` hemos añadido un disco duro de 1GB. Para que estos cambios tengan efecto debes ejecutar la instrucción:

```bash
usuario@maquina:~/vagrant$ vagrant reload
```

Para terminar, indicar que tenemos más parámetros de configuración que nos permiten configurar otros aspectos de la máquina virtual. Puedes encontrar más información en la [documentación oficial de vagrant](https://www.vagrantup.com/docs/)

## Enlaces interesantes

* [Página oficial de Vagrant](http://www.vagrantup.com/)
* [Curso de vagrant (Alberto Molina)](https://github.com/albertomolina/curso-vagrant)
* [PLEDIN: Gestionando máquinas virtuales con Vagrant](http://www.josedomingo.org/pledin/2013/09/gestionando-maquinas-virtuales-con-vagrant/)
* [Boxes oficiales para Vagrant](https://atlas.hashicorp.com/boxes/search)
