---
title: Introducción a los Pipelines de Jenkins
---

En Jenkins se pueden realizar distintos tipos de tareas automatizadas. Pero nosotros vamos a usar los Pipelines.

Un **Pipeline** es una secuencia de tareas automatizadas que definen el ciclo de vida de la aplicación de nuestro flujo de integración/entrega/despliegue continuo. Podemos decir que un **Pipeline** Un pipeline es un conjunto de instrucciones del proceso que siga una aplicación desde el repositorio de control de versiones hasta que llega a los usuarios.

![pipelines](img/pipelines.png)

* **Disparadores**: Motivo por el cual se comienza la ejecución de tareas automáticas. Puede ser por varios motivos: push en un repositorio github, ejecución cada cierto tiempo, finalización de otra tarea,...
* **Stage**: Son las etapas lógicas en las que se dividen los flujos de trabajo de Jenkins. Es una práctica recomendada dividir nuestro flujo de trabajo en etapas ya que nos ayudará a organizar nuestros pipelines en fases. Ejemplos de fases: build, test, deploy,...
* **Steps**: Son las tareas ó comandos que ejecutados de forma secuencial implementan la lógica de nuestro flujo de trabajo.
* **Node**: Máquina que es parte del entorno de Jenkins y es capaz de ejecutar un Pipeline Jenkins. También llamada agentes de ejecución. Pueden ser la misma máquina donde tenemos instalado Jenkins, o máquinas configuradas para este fin. También podemos usar contenedores docker como agentes de ejecución. Es importante reseñar que el directorio de trabajo (workspace) es compartido por los steps del nodo, de forma que steps de un nodo pueden acceder a ficheros/directorios generados por steps de ese mismo nodo.
* **Notificaciones**: Por ejemplo que envíe un correo electrónico al terminar.

## Creación de pipelines

Creamos una **Nueva Tarea**, y le ponemos un nombre y elegimos el tipo **Pipeline**:

![pipe](img/pipe1.png)

En el apartado **Pipeline**, escribimos nuestro primer pipeline:

```
pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                echo 'Tareas para construir, instalar,...'
            }
        }
        stage('Test') {
            steps {
                echo 'Tareas para realizar test.'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Tareas para desplegar, construir, ...'
            }
        }
    }
}
```

![pipe](img/pipe2.png)

Le damos a **Guardar** y ya podemos **Construir ahora** para ejecutar el pipeline y construir un **Build**:

![pipe](img/pipe4.png)

Y si vemos la **Console Output** vemos la salida del **build**:

![pipe](img/pipe5.png)

---

## Índice

* [Instalación de Jenkins en docker](instalacion_docker.html)
* Introducción a los Pipelines de Jenkins
* [Instalación de docker como runner de Jenkins](runner_docker.html)
* [Creación, testeo y publicación de imágenes docker desde Jenkins](gendocker.html)
* [Ejecución de un pipeline en varios runner](runner.html)
