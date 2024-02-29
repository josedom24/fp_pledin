---
title: "Taller 1: Desarrollo y despliegue de una aplicación Java simple"
---

## ¿Qué vas a aprender en este taller?

* A instalar un servidor de aplicaciones Tomcat y configurarlo de forma correcta.
* A instalar la herramienta maven.
* A generar un proyecto maven, configurarlo y crear una aplicación java simple.
* A generar un fichero war al compilar la aplicación.
* A desplegar la aplicación en Tomcat.

## ¿Qué tienes que hacer?

Realiza los siguientes pasos para realizar este taller:

1. Instala tomcat10 como hemos visto en la documentación. Configura el panel de administración `Tomcat-Manager` y configúralo para su acceso.
2. Instala la aplicación `maven` que nos va a ayudar a compilar aplicaciones java.
3. A continuación vamos a generar un proyecto, que será el esqueleto de nuestra aplicación Java, para ello ejecuta:

```
mvn archetype:generate -DgroupId=com.example -DartifactId=my-webapp -DarchetypeArtifactId=maven-archetype-webapp -DinteractiveMode=false
```

La estructura de directorio que hemos creado será:

```
my-webapp
├── src
│   └── main
│       ├── resources
│       └── webapp
│           ├── WEB-INF
│           │   └── web.xml
│           └── index.jsp
└── pom.xml
```

POM es la unidad fundamental de trabajo en Maven. Es un archivo XML que contiene información sobre el proyecto y los detalles de configuración utilizados por Maven para construir el proyecto. 
A continuación configuramos la aplicación, modificando el fichero `pom.xml` con el siguiente contenido:

```xml
<project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
  xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/maven-v4_0_0.xsd">
  <modelVersion>4.0.0</modelVersion>
  <groupId>com.example</groupId>
  <artifactId>my-webapp</artifactId>
  <packaging>war</packaging>
  <version>1.0-SNAPSHOT</version>
  <name>my-webapp Maven Webapp</name>
  <url>http://maven.apache.org</url>
  <dependencies>
    <dependency>
      <groupId>javax.servlet</groupId>
      <artifactId>javax.servlet-api</artifactId>
      <version>4.0.1</version>
      <scope>provided</scope>
    </dependency>
  </dependencies>
<build>
    <finalName>${project.artifactId}</finalName>
    <plugins>
      <plugin>
        <groupId>org.apache.maven.plugins</groupId>
        <artifactId>maven-compiler-plugin</artifactId>
        <version>3.8.1</version>
        <configuration>
          <source>1.8</source>
          <target>1.8</target>
        </configuration>
      </plugin>
      <plugin>
        <groupId>org.apache.maven.plugins</groupId>
        <artifactId>maven-war-plugin</artifactId>
        <version>3.3.1</version>
      </plugin>
    </plugins>
  </build>
</project>
```



A continuación vamos a construir la aplicación, para ello crea el directorio `src/main/java/com/example/` y dentro crea el fichero `HelloServlet.java` con el siguiente contenido:

```java
package com.example;

import java.io.IOException;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

@WebServlet(name = "HelloServlet", urlPatterns = {"/hello"})
public class HelloServlet extends HttpServlet {

    @Override
    protected void doGet(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {
        response.setContentType("text/html;charset=UTF-8");
        response.getWriter().println("<h1>Hola, Mundo!</h1>");
    }
}
```

Finalmente construimos la aplicación con el comando:

```
mvn clean package
```

El resultado del paso anterior es una aplicación distribuida con extensión `.war` llamada `my-webapp.war` almacenada en la carpeta `target`. Esa aplicación `.war` se desplegará posteriormente en el servicio Tomcat.

Despliega la aplicación utilizando la aplicación de administración `Tomcat-Manager`. También se puede hacer un despliegue manual, ¿qué tendrías que hacer para realizar este tipo de despliegue?

Finalmente accede a la aplicación desde un navegador web de tu máquina cliente.


{% capture notice-text %}
## ¿Qué tienes que entregar?

1. Entrega una captura de la aplicación de administración `Tomcat-Manager` una vez que la aplicación está desplegada, donde se comprueba que la aplicación está desplegada.
2. Entrega una captura de pantalla accediendo a la aplicación web.

{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>

