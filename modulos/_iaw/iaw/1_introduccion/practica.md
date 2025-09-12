---
title: "Práctica: Despliegue de página web estática"
---

## Generadores de páginas estáticas

En los últimos años se han desarrollado programas de ordenador que nos permiten de forma sencilla generar sitios web estáticos.

* Están programados en distintos lenguajes.
* Incluyen un motor de plantillas para facilitar la generación del código html.
* Por lo tanto es fácil encontrar distintos temas (ficheros de hojas de estilos) para cambiar el aspecto de las páginas generadas.
* El usuario final sólo se debe preocupar del contenido.
* Normalmente el contenido se escribe en un lenguaje de marcas sencillo como es Markdown. 
* Una vez generado el sitio estático sólo tenemos que desplegar el sitio en nuestro servidor en producción.
* Tenemos muchos generadores de páginas estáticas: Jekyll, Hugo, Pelican, ...  

## ¿Qué tienes que hacer?

1. Elige entre alguno de los programas generadores de páginas web estáticas: lo más usados, son **Jekyll** y **Hugo**. Pero puedes elegir cualquier otro.
2. Lee en la documentación e instala el programa en tu ordenador (en tu host o en alguna máquina virtual).
3. Añade una página de contenido a tu página web escrita en Markdown y genera la página estática. ¿En qué directorio guarda el contenido generado tu generador?
4. Configura el generador para cambiar el nombre de tu página, el tema o estilo de la página,...
5. Genera un sitio web estático con al menos 3 páginas. Deben estar escritas en Markdown y deben tener los siguientes elementos HTML: títulos, listas, párrafos, enlaces e imágenes.
6. El proyecto que has generado para tu sitio web (configuración del generador, páginas en markdown,...) debe estar en un repositorio Git (no es necesario que el código generado se guarde en el repositorio, evítalo usando el fichero `.gitignore`).

## Despliegue de nuestro sitio web

Una vez generada nuestra página podemos desplegarla en nuestro servidor en producción. Podemos tener un servidor web propio (que administramos nosotros), o utilizar servicios de hosting para implantar nuestras páginas.

* Vamos a usar un hosting externo para desplegar nuestra página.
* Los servicios modernos para alojar páginas estáticas pueden proporcionar métodos de despliegues automáticos o semiautomáticos, y suelen usar repositorios git (el uso de servidores FTP está desapareciendo).
* Hosting que podemos usar: Netlify, GitHub Pages, GitLab Pages, Render, Vercel, ...
* Algunos de estos servicios te permiten de forma automática generar en ellos la página estática (Integración Continua). En nuestra práctica no vamos a usar esa característica. **La página se genera en nuestro ordenador y posteriormente se despliega al hosting externo**.
* Si nos permite varias formas de subir la página al hosting **siempre elegiremos el uso de repositorio Git**.

## ¿Qué tienes que hacer?

1. Elige un servicio de hosting de páginas web estáticas que te permita el despliegue de tu sitio web generado usando un repositorio Git.
2. Recuerda que los ficheros que vamos a desplegar son los generados por el generado de páginas web estática, por lo tanto necesitas **otro repositorio git** donde se guarde el contenido generado que vamos a desplegar (**el que no guardamos en el repositorio anterior**).
3. Despliega manualmente la página que has desarrollado en el hosting elegido.
4. Realiza un script bash que te permita automatizar la generación de la página (integración continua) y el despliegue automático de la página en el entorno de producción, después de realizar un cambio de la página en el entorno de desarrollo. 




{% capture notice-text %}
## Entrega

1. Indica el generador que vas a utilizar.
2. Entrega una captura de pantalla, donde se vea la página web funcionando en local, con las modificaciones realizadas.
3. Entrega la URL del repositorio donde has guardado tu proyecto.
4. Indica el hosting externo que vas a utilizar.
5. Entrega la URL del repositorio Git donde tienes guardado el contenido estático generado.
6. Entrega el script que has creado, y **muestra al profesor su funcionamiento**.
{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>



 
