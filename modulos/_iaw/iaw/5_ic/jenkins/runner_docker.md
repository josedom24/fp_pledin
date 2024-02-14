---
title: Instalación de docker como runner de Jenkins
---

Hasta ahora hemos estado trabajando con una instalación de jenkins sobre docker y hemos comprobado que las tareas que se realizan se hacen sobre el mismo nodo.

En este apartado vamos a configurar jenkins para que use contenedores docker como runner, es decir cuando ejecutemos un pipeline se creará un contenedor docker donde se realizarán las tareas. Esto tiene muchas ventajas, ya que no necesito instalar en la máquina de jenkins las herramientas que necesito para ejecutar las tareas, y además podemos usar cualquier imagen docker para que ejecute dichas tareas.

Para realizar la configuración necesitamos instalar docker en la máquina de jenkins, es por ello que vamos a hacer una nueva instalación usando la paquetería que nos proporciona jenkins:

## Instalación de jenkins con apt

Según el [manual de instalación](https://www.jenkins.io/doc/book/installing/linux/#debianubuntu). ejecutamos los siguientes comandos:

```
apt install openjdk-11-jre
curl -fsSL https://pkg.jenkins.io/debian-stable/jenkins.io.key | sudo tee   /usr/share/keyrings/jenkins-keyring.asc > /dev/null
echo deb [signed-by=/usr/share/keyrings/jenkins-keyring.asc]   https://pkg.jenkins.io/debian-stable binary/ | sudo tee   /etc/apt/sources.list.d/jenkins.list > /dev/null
apt-get update
apt-get install jenkins

apt install docker.io
usermod -aG docker jenkins
```

Accedemos a jenkins y tenemos que obtener la clave de administración:

```
cat /var/lib/jenkins/secrets/initialAdminPassword
```

## Configuración de docker como runner

Instalamos dos nuevos plugins: **Docker** y **Docker Pipeline**. (**Administrar Jenkins -> Administrar Plugins**). Y reiniciamos Jenkins. (Si nmo se reinicia desde el panel web podemos ejecutar `systemctl restart jenkins`).

![docker](img/docker0.png)

Configuramos una nueva nube: **Administrar Jenkins -> Administrar Nodos -> Configure Clouds**.

![docker](img/docker1.png)

Y configuramos el acceso a docker:

![docker](img/docker2.png)

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

![docker](img/docker3.png)

---

## Índice

* [Instalación de Jenkins en docker](instalacion_docker.html)
* [Introducción a los Pipelines de Jenkins](pipelines.html)
* Instalación de docker como runner de Jenkins
* [Creación, testeo y publicación de imágenes docker desde Jenkins](gendocker.html)
* [Ejecución de un pipeline en varios runner](runner.html)
