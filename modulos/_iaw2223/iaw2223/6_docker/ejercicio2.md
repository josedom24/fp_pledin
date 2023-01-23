---
title: "Ejercicio 2: Imágenes Docker"
---

1. Descarga las siguientes imágenes: `ubuntu:20.04`, `tomcat:9.0.70-jdk11`, `jenkins/jenkins:lts`, `php:7.4-apache`.
2. Muestras las imágenes que tienes descargadas.
3. Crea un contenedor demonio con la imagen `php:7.4-apache`.
4. Comprueba el tamaño del contenedor en el disco duro.
5. Con la instrucción `docker cp` podemos copiar ficheros a o desde un contenedor. Puedes encontrar información es esta [página](https://docs.docker.com/engine/reference/commandline/cp/). 
    Crea un fichero en tu ordenador, con el siguiente contenido:

    ```php
    <?php
    echo phpinfo();
    ?>
    ```
    Copia un fichero `info.php` al directorio `/var/www/html` del contenedor con `docker cp`.
6. Vuelve a comprobar el espacio ocupado por el contenedor.
7. Accede al fichero `info.php` desde un navegador web.
