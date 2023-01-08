---
title: Despliegue de aplicaciones Java
---

## Tarea 1: Desarrollo y despliegue de una aplicación Java simple

Realiza los siguientes pasos para realizar esta tarea:

1. Instala tomcat9 como hemos visto en la documentación. Configura el panel de administración `Tomcat-Manager` y configúralo para su acceso.
2. Instala la aplicación `maven` que nos va a ayudar a compilar aplicaciones java.
3. A continuación vamos a generar un proyecto, que será el esqueleto de nuestra aplicación Java, para ello ejecuta:

```
mvn archetype:generate -DgroupId=com.app.example -DartifactId=java-app -DarchetypeArtifactId=maven-archetype-quickstart -DinteractiveMode=false
```

Podéis sustituir los valores de `groupID` y `artifactId` (este será el nombre de la aplicación) por lo que queráis.

La estructura de directorio que hemos creado será:

```
java-app/
├── pom.xml
└── src
    ├── main
    │   └── java
    │       └── com
    │           └── app
    │               └── example
    │                   └── App.java
    └── test
        └── java
            └── com
                └── app
                    └── example
                        └── AppTest.java
```

POM es la unidad fundamental de trabajo en Maven. Es un archivo XML que contiene información sobre el proyecto y los detalles de configuración utilizados por Maven para construir el proyecto. 
A continuación configuramos la aplicación, modificando el fichero `pom.xml` con el siguiente contenido:

```xml
<?xml version = "1.0" encoding = "UTF-8"?>
<project xmlns = "http://maven.apache.org/POM/4.0.0" 
   xmlns:xsi = "http://www.w3.org/2001/XMLSchema-instance"

xsi:schemaLocation = "http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
<modelVersion>4.0.0</modelVersion>

   <groupId>com.tutorialspoint</groupId>
   <artifactId>hello-world</artifactId>
   <version>1</version>
   <packaging>war</packaging>
   
   <parent>
      <groupId>org.springframework.boot</groupId>
      <artifactId>spring-boot-starter-parent</artifactId>
      <version>2.3.0.RELEASE</version>
      <relativePath/> 
   </parent>

   <properties>
      <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
      <project.reporting.outputEncoding>UTF-8</project.reporting.outputEncoding>
      <java.version>1.8</java.version>
      <tomcat.version>9.0.37</tomcat.version>
   </properties>

   <dependencies>
      <dependency>
         <groupId>org.springframework.boot</groupId>
         <artifactId>spring-boot-starter-web</artifactId>
      </dependency>
      <dependency>  
         <groupId>org.springframework.boot</groupId>  
	 <artifactId>spring-boot-starter-tomcat</artifactId>  
	 <scope>provided</scope>  
      </dependency>   
      <dependency>
         <groupId>org.springframework.boot</groupId>
         <artifactId>spring-boot-starter-test</artifactId>
         <scope>test</scope>
      </dependency>
   </dependencies>

   <build>
      <plugins>
         <plugin>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-maven-plugin</artifactId>
         </plugin>
      </plugins>
   </build>
   
</project>
```

Si te fijas verás que nuestra aplicación se va a construir con un framework Java llamado [Spring Framework](https://spring.io/projects/spring-framework).

A continuación vamos a construir la aplicación, para ello modificamos el fichero `src/main/java/com/app/example/App.java` con el siguiente contenido:

```java
package com.app.example;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.boot.builder.SpringApplicationBuilder;
import org.springframework.boot.web.servlet.support.SpringBootServletInitializer;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@SpringBootApplication
@RestController
public class App extends SpringBootServletInitializer {
   @Override
   protected SpringApplicationBuilder configure(SpringApplicationBuilder application) {
      return application.sources(App.class);
   }
   public static void main(String[] args) {
      SpringApplication.run(App.class, args);
   }

   @RequestMapping(value = "/")
   public String hello() {
      return "<center>Hola mundo!!!</center>";
   }
}
```

Finalmente construimos la aplicación con el comando:

```
mvn package
```

El resultado del paso anterior es una aplicación distribuida con extensión `.war` almacenada en la carpeta de destino bajo `java-app`. Esa aplicación `.war` se desplegará posteriormente en el servicio Tomcat, para ello:

cp java-app/target/hello-world-1.war /etc/tomcat/webapps/

Finalmente accede a la aplicación desde un navegador web de tu máquina cliente.

## Tarea 2: Entorno de producción


{% capture notice-text %}
Explica los cambios que has realizado en el entorno de desarrollo y cómo lo has desplegado en producción para cada una de las modificaciones. Entrega pantallazos donde se vean las distintas modificaciones y que todo está funcionando. (3,5 puntos)
{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>
