---
title: Instalación de docker como runner de Jenkins
---

Como vimos en el apartado anterior, las tareas que se realizan sal ejucutan el pileline se hacen sobre el mismo nodo.

En este apartado vamos a configurar jenkins para que use contenedores docker como runner, es decir cuando ejecutemos un pipeline **se creará un contenedor docker** donde se realizarán las tareas. Esto tiene muchas ventajas, ya que no necesito instalar en la máquina de jenkins las herramientas que necesito para ejecutar las tareas, y además podemos usar cualquier imagen docker para que ejecute dichas tareas.

Para realizar dicha configuración realizamos los siguientes pasos.

Instalamos docker, y añadimos el usuario `jenkins` al grupo `docker`:

```
apt install docker.io
usermod -aG docker jenkins
```

Si estamos trabajando en una instancia de OpenStack, hay que tener en ceunta de configurar el MTU de la red de docker con el mismo valor con el que trabaja la instancia. Siguiendo el artículo [Contenedores en instancias de OpenStack](https://www.josedomingo.org/pledin/2022/12/contenedores-instancias-openstack/), hay que crear el fichero `/etc/docker/daemon.json` con el siguinte contenido:

```
{
  "mtu": 1442
}
```

Y reiniciamos el demonio de docker:

``` 
systemctl daemon-reload
systemctl restart docker
```

## Configuración de docker como runner

Instalamos dos nuevos plugins: **Docker** y **Docker Pipeline**. (**Administrar Jenkins -> Administrar Plugins**). Y reiniciamos Jenkins. (Si no se reinicia desde el panel web podemos ejecutar `systemctl restart jenkins`).

Configuramos una nueva nube: **Administrar Jenkins -> Clouds -> New cloud**.

Y configuramos el acceso a docker: 

* **Cloud name** = docker
* **Type** = Docker
* **Docker Cloud details** -> **Docker Host URI = unix:///var/run/docker.sock
* Activamos la opción **Enabled**
* Pulsamos sobre el botón **Test Connection** y si todo está bien configurado, aparecerá la versión de docker.



Y ya podemos hacer una prueba, creando un pipeline con las siguientes instrucciones:

```
pipeline {
    agent {
        docker { image 'python:3' }
    }
    stages {
        stage('Test') {
            steps {
                sh 'python --version'
            }
        }
    }
}
```

Al ejecutar el pipeline podemos observar como se ha descargado la imagen, ha creado un contenedor, ha ejecutado la instrucción indicada y finalmente borra el contenedor.


