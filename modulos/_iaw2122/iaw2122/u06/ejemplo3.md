---
title: "Ejemplo 3: Corrector ortográfico de documentos markdown (test)"
---

Imaginemos que estamos escribiendo documentos markdown y lo guardamos en un repositorio de github. Queremos que cada vez que hagamos una modificación (commit - push) queremos probar (test) si tienes alguna falta de ortografía. Ese proceso lo vamos a hacer de forma automática y continua con Jenkins. Recuerda que el repositorio es [https://github.com/josedom24/ic-diccionario](https://github.com/josedom24/ic-diccionario)

## Definición del pipeline

Hasta ahora al definir un pipeline lo hemos escrito directamente en la configuración. Otra forma de hacerlo es tener definido el pipeline en un fichero llamado `Jenkinsfile` que estará en un repositorio. Al crear el pipeline lo indicaremos de la siguiente forma:

![pipe](img/pipe6.png)

El fichero `Jenkinfile` tiene el siguiente contenido:

```groovy
pipeline {
    agent {
        docker { image 'debian'
        args '-u root:root'
        }
    }
    stages {
        stage('Clone') {
            steps {
                git branch:'master',url:'https://github.com/josedom24/ic-travis-diccionario.git'
            }
        }
        stage('Install') {
            steps {
                sh 'apt-get update && apt-get install -y aspell-es ' 
            }
        }
        stage('Test')
        {
            steps {
                sh '''
                export LC_ALL=C.UTF-8
                OUTPUT=`cat doc/*.md | aspell list -d es -p ./.aspell.es.pws`; if [ -n "$OUTPUT" ]; then echo $OUTPUT; exit 1; fi'''
            }
        }
    }
}
```

1. Vamos a crear un contenedor con debian, y vamos a usar el usuario root en la imagen.
2. Hemos clonado el repositorio con el comando `git` en el stage `Clone`.
3. En el stage `Install` actualizamos e instalamos la herramienta que vamos a utilizar. Podríamos partir de una imagen construida por nosotros donde tuviéramos ya esta herramienta instalada, y no haría falta este paso.
4. En el stage `Test` hacemos la comprobación, hemos configurado el contenedor para que use UTF8.

## Disparador del pipeline

Tenemos varias formas de activar de forma automática la ejecución del pipeline:

![pipe](img/pipe7.png)

En este ejercicio vamos a usar la opción **Consultar repositorio (SCM)**. Esta opción no es exactamente cuando se hace un push en el repositorio, sino que se pone un programador cron indicando cada cuanto tiempo se mira el repositorio, si ha cambiado el repositorio se lanza el pipeline. Nosotros vamos a poner: `* * * * *`, miraremos el repositorio cada minuto:

![pipe](img/pipe8.png)

## Notificaciones del pipeline

Vamos a aprender como podemos hacer que el pipeline mande un correo al finalizar. Para ello lo primero instala un servidor de correo de forma adecuada en la máquina que tiene Jenkins. Lo siguiente es configurar Jenkins en **Administrar Jenkins -> Configurar el sistema**: 

![pipe](img/pipe9.png)

Y al pileline le añadimos las siguientes líneas:

```groovy
...
    stages {
    ...
    }
    post {
         always {
          mail to: 'usuario@example.com',
          subject: "Status of pipeline: ${currentBuild.fullDisplayName}",
          body: "${env.BUILD_URL} has result ${currentBuild.result}"
        }
      }
}
```