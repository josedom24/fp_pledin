---
title: "Ejemplo 3: Integración continua de aplicación django (Test)"
---

## Pipeline para realizar un test automático

Sabiendo como se ejecutan los test, es fácil hacer un pipeline que lo haga por nosotros de forma automática:

```groovy
pipeline {
    agent {
        docker { image 'python:3.12-slim'
        args '-u root:root'
        }
    }
    stages {
        stage('Clone') {
            steps {
                git branch:'master',url:'https://github.com/josedom24/django_tutorial.git'
            }
        }
        stage('Install') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }
        stage('Test')
        {
            steps {
                sh 'python3 manage.py test'
            }
        }
    }
}
```

1. Para poder instalar los paquetes con pip necesitamos ejecutar las instrucciones en el contenedor como root (`args '-u root:root'`).
2. Clonamos el repositorio.
3. Instalamos los requerimientos.
4. Realizamos los test.

Prueba a cambiar el código para que un test falle y comprueba como el pipeline falla.



