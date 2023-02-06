---
title: Ejecución de un pipeline en varios runner
---

Podemos ejecutar un conjunto de stages en un runner, y otro conjunto en otros. Por ejemplo, podemos hacer el build, y el test de la aplicación utilizando un runner que sea un contenedor docker, y el stage deploy, o la construcción de un contenedor docker lo podemos hacer desde la máquina donde tenemos instalado jenkins.

Veamos un ejemplo:

```grovy
pipeline {
    agent none
    stages {
        stage("build and test the project") {
            agent {
                docker "python:2"
            }
            stages {
                stage('En el contenedor') {
            
                steps {
                    sh 'python --version'
                    }
                }
            }
        }
        stage("deploy in prodcution") {
            agent any
            stages {
                stage('En la máquina') {
                
                steps {
                    sh 'python3 --version'
                    }
                }
            }
        }
    }
}
```

En este caso:

* El stage `En el contenedor` se ejecuta en un contenedor `debian`.
* El stage `En la máquina` se ejecuta en la máquina de jenkins.

---

## Índice

* [Instalación de Jenkins en docker](instalacion_docker.html)
* [Introducción a los Pipelines de Jenkins](pipelines.html)
* [Instalación de docker como runner de Jenkins](runner_docker.html)
* [Creación, testeo y publicación de imágenes docker desde Jenkins](gendocker.html)
* Ejecución de un pipeline en varios runner
