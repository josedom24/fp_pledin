# Implantación y despliegue de una aplicación web estática

La forma tradicional de crear un sitio web estático sería de la siguiente forma:

1. Crear las distintas páginas html en el entorno de desarrollo.
2. Podemos añadir alguna funcionalidad añadiendo código javascript, que se ejecutará en el cliente.
3. El entorno de producción necesita sólo un servidor web.
4. El despliegue podemos hacer usando un servidor ftp para subir los ficheros al servidor.

Ventajas de las páginas estáticas:

* Portabilidad, funcionan en cualquier servidor.
* Tiempos de acceso óptimos, tardan muy poco en cargarse.
* Facilitan el posicionamiento.
* Costos de alojamiento menores.
* Mínimos requerimientos técnicos para su operación.

Desventajas de las páginas estáticas:

* Funcionalidad muy limitada
* El visitante no tiene ninguna posibilidad de seleccionar, ordenar o modificar los contenidos o el diseño de la página a su gusto.
* El administrador web debe acceder al servidor donde está alojada la página para cambiar los contenidos de la página.
* El proceso de actualización es lento, tedioso y esencialmente manual.
* No se accede a bases de datos (esto puede ser también una ventaja)

## Generadores de páginas estáticas

En los últimos años se han desarrollado programas de ordenador que nos permiten de forma sencilla generar sitios web estáticos.

* Están programados en distintos lenguajes
* Incluyen un motor de plantillas para facilitar la generación del código html.
* Por lo tanto es fácil encontrar distintos temas (ficheros de hojas de estilos) para cambiar el aspecto de las páginas generadas.
* El usuario final sólo se debe preocupar del contenido.
* Normalmente el contenido se escribe en un lenguaje de marcas sencillo como es Markdown. La [sintaxis de este lenguaje de marcas](https://guides.github.com/features/mastering-markdown/) es muy sencilla y fácilmente convertible a html.
* Una vez generada el sitio estático sólo tenemos que desplegar el sitio en nuestro servidor en producción.

Tenemos muchos generados de páginas estáticas: Jekyll, Hugo, Pelican,... Puedes encontrar una lista completa en: [StaticGen](https://www.staticgen.com/)


## Despliegue de nuestro sitio web

Una vez generada nuestra página podemos desplegarla en nuestro servidor en producción. Podemos tener un servicidor web propio (que administramos nosotros), o utilizar servicios de hosting para implantar nuestras páginas.

Los servicios modernos para alojar páginas estáticas pueden proporcionar métodos de despliegues automáticos o semiautomética, y suelen usar repositorios git (el uso de servidores FTP está desapareciendo).

Ejemplos de servicios de despliegue de páginas estáticas: Netlify, Surge, GitHub Pages, GitLab Pages, Neocities,... Puedes enontras más opciones [aquí](https://stackshare.io/netlify/alternatives), [aquí](https://alternativeto.net/software/netlify/) o [aqui](https://siftery.com/netlify/alternatives).


## Ejercicios

1. Selecciona una combinación entre generador de página estático y servicio donde desplegarlo. Escribe tu propuesta en redmine, cada propuesta debe ser original.
2. Comenta la instalación del generador de página estática. Recuerda que el generador tienes que instalarlo en tu entorno de desarrollo. (2 puntos)
3. Configura el generador de página para cambiar el nombre de tu página, el tema o estilo de la página,... Indica cualquier otro cambio de configuración que hayas hecho. (1 punto)
4. Genera un sitio web estático con al menos 3 páginas. Deben estar escritas en Markdown y deben tener los siguientes elementos: títulos, listas, párrafos, enlaces e imágenes. El código generado debe estar en un repositorio Git. (3 puntos).
5. Explica el proceso de despliegue utilizado por el servicio de hosting que vas a utilizar. (2 puntos)
6. Piensa algún método (script, scp, rsync, git,...) que te permita automatizar la integración continua y el despliegue de la página en el entorno de desarrollo, después de realizar un cambio de la página en el entorno de desarrollo. Entrega un vídeo donde expliques el proceso. (3 puntos).

