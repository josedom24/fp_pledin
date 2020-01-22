---
title: Introducción a Tomcat 8
permalink: /iawgs/u05/tomcat8.html
---

En el siguiente documento se explicará como implantar un contenedor de servlets Tomcat versión 8 en un sistema Linux Debian Stretch.

## Instalación

Para instalar tomcat8 desde repositorios:
	
	apt install tomcat8

Por dependecia va a instalar el paquete `openjdk-8-jre-headless`, que corresponde a una implementación de la JVM mínima para poder ejecutar nuestros programas java.

Desde este momento tendremos Tomcat ejecutándose y sirviendo en el puerto 8080.

![tomcat](img/tomcat1.png)

Para gestionar el servicio tomcat:

	systemctl stop|start|restart|status tomcat8

Si estamos instalando tomcat8 en una instancia de OpenStack, y por las limitaciones de las máquinas virtuales en la generación pseudoaleatoria, es necesario modificar el fichero `/usr/lib/jvm/java-8-openjdk-amd64/jre/lib/security/java.security`, y cambiar la siguiente línea:

	securerandom.source=file:/dev/./urandom

Trás el cambio reinciamos el servicio.

## Administración

Esta sección la iniciaremos utilizando una herramienta que nos proporciona la fundación Apache y que nos facilita el despliegue de aplicaciones y manejo del servidor, Tomcat-Manager. Para instalarlo:

	# apt install tomcat8-admin

Una vez instalado debemos crear un usuario con el rol manager para acceder a él. Añadimos una línea similar a la siguiente al fichero `/etc/tomcat8/tomcat-users.xml`:

	<role rolename="manager-gui"/>
	<user username="tomcat" password="s3cret" roles="manager-gui"/>

Para acceder a la zona de administración:

![tomcat](img/tomcat2.png)
 
## Despliegue de aplicaciones mediante la interfaz web

Utilizaremos la herramienta anterior para explicar cómo desplegar una aplicación, por ejemplo .war. Simplemente bajamos con el scroll hasta encontrar una sección llamada "WAR file to deploy". Seleccionamos el fichero .war y le damos al botón "Deploy".

Puedes bajarte el fichero war desde el siguiente [enlace](war/RequestDispatcher.war).

![tomcat](img/tomcat3.png)

Automáticamente se creará un nuevo elemento en la sección aplicaciones utilizando el mismo
nombre que el fichero .war subido.

![tomcat](img/tomcat4.png)

Desde aquí podremos controlar la aplicación (Arrancarla, pararla, eliminarla,...)

## Despliegue de aplicaciones mediante la terminal

Implantar una aplicación desde la terminal, tampoco es tan difícil, ya que por defecto cualquier fichero `.war` que se copie o mueva dentro de l directorio `/var/lib/tomcat8/webapps/` se desplegaría automáticamente y dependiendo de nuestra configuración se lanzaría o no.

En mucha documentación sobre tomcat se refiere a la cariable de entorno `$CATALINA_HOME`, en un debian donde hemos instalado tomcat con apt, el valor de esta varibale será `/var/lib/tomcat8`.
{: .notice--warning}

## Administración desde la terminal

Es hora de hablar de los ficheros de configuración. 

### server.xml

El más importante es `/etc/tomcat8/server.xml`, cuyo contenido define cómo está formado nuestro servidor. Las secciones más importante de este fichero son:

* Componente **Server**: es el elemento principal del archivo `server.xml` y todas las demás secciones deben encontrarse entre estos nodos:
		
		<Server port="8005" shutdown="SHUTDOWN"> ... </Server>

	* `port`: Indica el puerto al que se enviaría el comando shutdown.
	* `shutdown`: Indica la cadena de texto que se enviaría al puerto indicado anteriormente para apagar el servidor.

* Componente **Service**: Un servicio es un grupo de conectores.
  
		<Service name="Catalina"> ... </Service>
	
	* `name`: Nombre utilizado en los ficheros de log, administración y gestión, debe ser distínto para cada service.

* Subelemento **Conector**: El elemento `Connector` representa las conexiones (Puertos TCP) que serán abiertas por Tomcat al arranque, se definen diversos atributos los cuales dan más detalles acerca de la conexión.

		<Connector port="8080" protocol="HTTP/1.1" 
               connectionTimeout="20000" 
               URIEncoding="UTF-8" 
               redirectPort="8443" /> 

	* `port`: Puerto en el que recibe las peticiones.
	* `protocol`: 'HTTP/1.1' ó 'AJP/1.3'.
	* `redirectPort`: Si la petición se hace por medio de SSL, se reenvíara a este puerto.

	Como vemos en el fichero el único conector que está descomentado es el conector para HTTP, tambíen podemos enontrar en el fichero el conector para HTTPS:

		<!--
	    <Connector port="8443" protocol="org.apache.coyote.http11.Http11AprProtocol"
	               maxThreads="150" SSLEnabled="true" >
	        <UpgradeProtocol className="org.apache.coyote.http2.Http2Protocol" />
	        <SSLHostConfig>
	            <Certificate certificateKeyFile="conf/localhost-rsa-key.pem"
	                         certificateFile="conf/localhost-rsa-cert.pem"
	                         certificateChainFile="conf/localhost-rsa-chain.pem"
	                         type="RSA" />
	        </SSLHostConfig>
	    </Connector>
	    -->

	Y el conector para el protocolo [AJP (Apache JServ Protocol)](https://es.wikipedia.org/wiki/Apache_JServ_Protocol), que es un protocolo binario que permite enviar solicitudes desde un servidor web a un servidor de aplicaciones que se encuentra detrás del servidor web. Por ejemplo en el servidor web apache2 podemos usar el mósulo `proxy_ajp` para comunicar apache2 con tomat.

		<!--
    	<Connector port="8009" protocol="AJP/1.3" redirectPort="8443" />
    	-->

* Subelemento **Engine**: Todas las peticiones que lleguen a los puertos y usando los protocolos definidos en los elementos conectores, se procesaran por los elementos definidos aquí:

		<Engine name="Catalina" defaultHost="localhost"> 

	* `name`: Nombre utilizado para la administración y ficheros de log.
	* `defaultHost`: Host por defecto que resuelve las peticiones si no se indica otro Host concreto.

	Dentro de este elemento podemos encontrar varios elementos `Host` que nos permiten definir virtual hosts para tomcat:

		<Host name="localhost"  appBase="webapps" 
            unpackWARs="true" autoDeploy="true" 
            xmlValidation="false" xmlNamespaceAware="false"> 
		</Host> 

	* `name`: Nombre del host virtual.
	* `appBase`: Ruta relativa desde `<TOMCAT_HOME>` donde se despliegan las aplicaciones.
	* `unpackWARs`: Indica si se deben desempaquetar o no los .war depositados en appBase.
	* `autoDeploy`: Indica si se desplegarán las aplicaciones automáticamente o no.

### context.xml

Fichero de configuración específico de cada aplicación. Si alguna aplicación se despliega sin fichero `context.xml`, se aplicará la configuración del situado en `/etc/tomcat8/context.xml`.

		<?xml version="1.0" encoding="UTF-8"?>
		<Context>
		    <WatchedResource>WEB-INF/web.xml</WatchedResource>
		    <WatchedResource>${catalina.base}/conf/web.xml</WatchedResource>
		</Context>

Su utilización es similar a la del fichero `.htaccess` de Apache.

### web.xml

Su ruta real es `aplicacion/web-inf/web.xml`, se trata de un descriptor de despliegue. Al igual que con el fichero `context.xml`, Tomcat posee un `web.xml`alojado en `/etc/tomcat8/web.xml` que se ejecuta antes del propio de cada aplicación. Con él se pueden activar y desactivar características como el compilador de JSP.

{% capture notice-text %}
**Ejercicio**

Instala apcahe tomcat en un equipo y despliega la aplicación: [EjemploPruebaCarga.war](war/EjemploPruebaCarga.war) desde la línea de comandos.

{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>