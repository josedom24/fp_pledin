---
title: Instalación de Jenkins en docker
---

Tenemos muchos métodos para realizar la instalación de Jenkins: [Installing Jenkins](https://www.jenkins.io/doc/book/installing/).

Nosotros vamos a usar la imagen docker `jenkins/jenkins` para realizar la instalación de jenkins en un contenedor docker. Podemos ver la [documentación de la imagen](https://github.com/jenkinsci/docker/blob/master/README.md) y realizamos los siguientes pasos:

```
docker run -d -p 8080:8080 -p 50000:50000 --name jenkins -v jenkins_home:/var/jenkins_home jenkins/jenkins:lts-jdk11
```

Para obtener la la contraseña de administración que nos pregunta al principio ejecutamos:

```
docker exec jenkins cat /var/jenkins_home/secrets/initialAdminPassword
```

Para terminar instalamos los plugins que nos recomiendan y creamos un usuario administrador.

---

## Índice

* Instalación de Jenkins en docker
* [Introducción a los Pipelines de Jenkins](pipelines.html)
* [Instalación de docker como runner de Jenkins](runner_docker.html)
* [Creación, testeo y publicación de imágenes docker desde Jenkins](gendocker.html)
* [Ejecución de un pipeline en varios runner](runner.html)
