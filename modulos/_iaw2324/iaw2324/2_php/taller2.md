---
title: "Taller 2: Configuración Apache2 + fpm-php"
---

## ¿Qué vas a aprender en este taller?

* A configurar tu servidor LAMP usando un servidor de aplicaciones `fpm-php`.
* A modificar la configuración básica del servidor `fpm-php`.
* A configurar apache2 como proxy inverso para pasar las peticiones PHP al servidor de aplicación `fpm-php.`

## Recursos para realizar este taller

* Artículo: [Ejecución de PHP con PHP-FPM](fpm.html)

## ¿Qué tienes que hacer?

En el escenario del taller anterior vamos a configurar apache2 + PHP-FPM. Para ello realiza los siguientes pasos:

1. Desinstala el módulo de apache2 que permite la ejecución de PHP.
2. Instala PHP-FPM.
3. Configura apache2 para que utilice PHP-FPM para ejecutar PHP, lo puedes hacer para todos los virtualhost o en cada uno de los virtualhost.
4. Comprueba accediendo a un fichero `info.php`, que los script PHP se están ejecutando con PHP-FPM (parámetro **Server API**). Comprueba que la aplicación *Biblioteca* sigue funcionando.
5. Cambia la configuración de PHP-FPM para que escuche en el puerto tcp/9000. Cambia la configuración de apache2 para que se comunique con PHP-FPM utilizando ese puerto.
6. Comprueba que la aplicación siguen funcionando.
7. Cambia la memoria máxima de uso de un script PHP (parámetro `memory_limit`) a 256Mb.


{% capture notice-text %}
## ¿Qué tienes que entregar?

1. Pantallazo donde se compruebe que tienes corriendo en tu servidor procesos PHP-FPM. 
2. Configuración que has hecho en apache2 para trabajar con PHP-FPM.
3. Pantallazo donde se vea la salida del fichero `info.php` donde se ve que la ejecución de PHP se hace con PHP-FPM.
4. Pantallazos de la aplicación Biblioteca funcionando (después del login).
5. Configuración de PHP-FPM y apache2 para que funcione el punto 5.
6. Indica el fichero que has modificado (con el path completo) para modificar el límite de memoria. Muestra un pantallazo de la salida del fichero `info.php` donde se vea el cambio.
{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>
