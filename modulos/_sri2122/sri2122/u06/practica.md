---
title: "Práctica: Aumento de rendimiento en servidores web"
---

## HAProxy: Balanceador de carga

1. Crea y configura el escenario usando el repositorio [vagrant_ansible_haproxy](https://github.com/josedom24/vagrant_ansible_haproxy).
2. Configura la resolución estática y accede a wordpress.
3. Vamos a calcular el rendimiento con el balanceo de carga a dos nodos. Para ello haz varias pruebas y quedate con la media de peticiones/segundo:
		
		ab -t 10 -c 100 -h http://www.example.org/wordpress/

4. Accede con `hatop` y deshabilita un nodo. Vuelve a hacer las pruebas de rendimiento. ¿Se nota la diferencia entre balancear y no balancear?. (Al terminar este ejercicio habilita de nuevo el nodo).
5. Modifica el vagrant y el ansible e introduce un nuevo nodo `backend3` donde se instalale wordpress. Modifica la configuración de HAProxy para que balancee entre los tres nodos. Vuelve a hacer las pruebas de rendimiento. ¿Se nota la diferencia entre balancear a dos nodos o a tres?

## Memcached

Vamos a utilizar el repositorio [vagrant_ansible_wordpress](https://github.com/josedom24/vagrant_ansible_wordpress) que te crea un servidor `servidorweb` con wordpress instalado. Para acceder a la zona de adminsitarción (`admin`/`admin`). Para acceder al Wordpress usamos la url `http://www.example.org/wordpress/`.

Para realizar este ejercicio puedes basarte en el artículo [Optimizar WordPress con Memcached](https://www.rjcardenas.com/optimizar-wordpress-con-memcached/).

1. Instala memcahced en el servidor. Comprueba con un `info.php` que está instalado.
2. Configura en wordpress un plugin que le permita trabajar con memcached.
3. Realiza el calculo de rendimiento. Para ello haz varias pruebas y quedate con la media de peticiones/segundo:

	ab -t 10 -c 100 -h http://www.example.org/wordpress/

	¿Se ha aumentado el rendimiento de forma significativa?


## Varnish

Utiliza el mismo repositorio para crea un servidor con wordpress. Siguiendo la introducción a varnish realiza los siguientes pasos:

1.  Configura un proxy inverso - caché Varnish escuchando en el puerto 80 y que se comunica con el servidor web por el puerto 8080. Entrega y muestra una comprobación de que varnish está funcionando con la nueva configuración.
2. Realiza pruebas de rendimiento (quedate con el resultado del parámetro `Requests per second`) y comprueba si hemos aumentado el rendimiento. 
3. Si hacemos varias peticiones a la misma URL, ¿cuantas peticiones llegan al servidor web? (comprueba el fichero `access.log` para averiguarlo).