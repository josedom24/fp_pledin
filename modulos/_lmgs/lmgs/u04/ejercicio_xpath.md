---
title: "Ejercicio de introducción a xpath"
permalink: /lmgs/u04/ejercicio_xpath.html
---

Para hacer estos ejercicios puedes utilizar la página: [Code Beauty - XPath Tester](https://codebeautify.org/Xpath-Tester)

## Ejercicio 1

Dado el siguiente documento XML, escriba las expresiones XPath que devuelvan la respuesta deseada:

    <?xml version="1.0" encoding="UTF-8"?>
    <ies>
      <nombre>IES Gonzalo Nazareno</nombre>
      <web>http://www.gonzalonazareno.org</web>
      <ciclos>
        <ciclo id="ASIR">
          <nombre>Administración de Sistemas Informáticos en Red</nombre>
          <grado>Superior</grado>
          <decretoTitulo año="2009" />
        </ciclo>
        <ciclo id="DAW">
          <nombre>Desarrollo de Aplicaciones Web</nombre>
          <grado>Superior</grado>
          <decretoTitulo año="2010" />
        </ciclo>
        <ciclo id="SMR">
          <nombre>Sistemas Microinformáticos y Redes</nombre>
          <grado>Medio</grado>
          <decretoTitulo año="2008" />
        </ciclo>
      </ciclos>
    </ies>

1. Nombre del instituto:

        <nombre>IES Gonzalo Nazareno</nombre>

2. Página web del Instituto:

        http://www.iesabastos.org

3. Nombre de los Ciclos Formativos:

        Administración de Sistemas Informáticos en Red
        Desarrollo de Aplicaciones Web
        Sistemas Microinformáticos y Redes

4. Siglas por las que se conocen los Ciclos Formativos:

        id="ASIR"
        id="DAW"
        id="SMR"

5. Años en los que se publicaron los decretos de título de los Ciclos Formativos:

        año="2009"
        año="2010"
        año="2008"

6. Ciclos Formativos de Grado Medio (se trata de obtener el elemento <ciclo> completo):
    Nota: Resuelva este ejercicio de dos formas distintas, en un único paso de búsqueda y en dos pasos de búsqueda.

        <ciclo id="SMR">
          <nombre>Sistemas Microinformáticos y Redes</nombre>
          <grado>Medio</grado>
          <decretoTitulo año="2008"/>
        </ciclo>

7. Nombre de los Ciclos Formativos de Grado Superior:
    Nota: Resuelva este ejercicio de dos formas distintas, en un único paso de búsqueda y en dos pasos de búsqueda.

        <nombre>Administración de Sistemas Informáticos en Red</nombre>
        <nombre>Desarrollo de Aplicaciones Web</nombre>

8. Nombre de los Ciclos Formativos anteriores a 2010:
    Nota: Resuelva este ejercicio de dos formas distintas, en un único paso de búsqueda y en dos pasos de búsqueda.

        Administración de Sistemas Informáticos en Red
        Sistemas Microinformáticos y Redes

9. Nombre de los Ciclos Formativos de 2008 o 2010:
    Nota: Resuelva este ejercicio de dos formas distintas, en un único paso de búsqueda y en dos pasos de búsqueda.

        Desarrollo de Aplicaciones Web
        Sistemas Microinformáticos y Redes

## Ejercicio 2

Dado el siguiente documento XML, escriba las expresiones XPath que devuelvan la respuesta deseada:

    <?xml version="1.0" encoding="UTF-8"?>
    <ies>
      <modulos>
        <modulo id="0228">
          <nombre>Aplicaciones web</nombre>
          <curso>2</curso>
          <horasSemanales>4</horasSemanales>
          <ciclo>SMR</ciclo>
        </modulo>
        <modulo id="0372">
          <nombre>Gestión de bases de datos</nombre>
          <curso>1</curso>
          <horasSemanales>5</horasSemanales>
          <ciclo>ASIR</ciclo>
        </modulo>
        <modulo id="0373">
          <nombre>Lenguajes de marcas y sistemas de gestión de información</nombre>
          <curso>1</curso>
          <horasSemanales>3</horasSemanales>
          <ciclo>ASIR</ciclo>
          <ciclo>DAW</ciclo>
        </modulo>
        <modulo id="0376">
          <nombre>Implantación de aplicaciones web</nombre>
          <curso>2</curso>
          <horasSemanales>5</horasSemanales>
          <ciclo>ASIR</ciclo>
        </modulo>
      </modulos>
    </ies>


1. Nombre de los módulos que se imparten en el Instituto:

        Aplicaciones web
        Gestión de bases de datos
        Lenguajes de marcas y sistemas de gestión de información
        Implantación de aplicaciones web

2. Nombre de los módulos del ciclo ASIR:
    Nota: Resuelva este ejercicio de dos formas distintas, en un único paso de búsqueda y en dos pasos de búsqueda.

        Gestión de bases de datos
        Lenguajes de marcas y sistemas de gestión de información
        Implantación de aplicaciones web

3. Nombre de los módulos que se imparten en el segundo curso de cualquier ciclo:
    Nota: Resuelva este ejercicio de dos formas distintas, en un único paso de búsqueda y en dos pasos de búsqueda.

        Aplicaciones web
        Implantación de aplicaciones web

4. Nombre de los módulos de menos de 5 horas semanales:
    Nota: Resuelva este ejercicio de dos formas distintas, en un único paso de búsqueda y en dos pasos de búsqueda.

        Aplicaciones web
        Lenguajes de marcas y sistemas de gestión de información

5. Nombre de los módulos que se imparten en el primer curso de ASIR:
    Nota: Resuelva este ejercicio de dos formas distintas, en un único paso de búsqueda y en dos pasos de búsqueda.

        Gestión de bases de datos
        Lenguajes de marcas y sistemas de gestión de información

6. Horas semanales de los módulos de más de 3 horas semanales:
    Nota: Resuelva este ejercicio de dos formas distintas, en un único paso de búsqueda y en dos pasos de búsqueda.

        4
        5
        5

## Ejercicio 3

Dado el siguiente documento XML, escriba las expresiones XPath que devuelvan la respuesta deseada:

    <?xml version="1.0" encoding="UTF-8"?>
    <ies>
      <nombre>IES Gonzalo Nzareno</nombre>
      <web>http://www.gonzalonzareno.org</web>
      <ciclos>
        <ciclo id="ASIR">
          <nombre>Administración de Sistemas Informáticos en Red</nombre>
          <grado>Superior</grado>
          <decretoTitulo año="2009" />
        </ciclo>
        <ciclo id="DAW">
          <nombre>Desarrollo de Aplicaciones Web</nombre>
          <grado>Superior</grado>
          <decretoTitulo año="2010" />
        </ciclo>
        <ciclo id="SMR">
          <nombre>Sistemas Microinformáticos y Redes</nombre>
          <grado>Medio</grado>
          <decretoTitulo año="2008" />
        </ciclo>
      </ciclos>
      <modulos>
        <modulo id="0228">
          <nombre>Aplicaciones web</nombre>
          <curso>2</curso>
          <horasSemanales>4</horasSemanales>
          <ciclo>SMR</ciclo>
        </modulo>
        <modulo id="0372">
          <nombre>Gestión de bases de datos</nombre>
          <curso>1</curso>
          <horasSemanales>5</horasSemanales>
          <ciclo>ASIR</ciclo>
        </modulo>
        <modulo id="0373">
          <nombre>Lenguajes de marcas y sistemas de gestión de información</nombre>
          <curso>1</curso>
          <horasSemanales>3</horasSemanales>
          <ciclo>ASIR</ciclo>
          <ciclo>DAW</ciclo>
        </modulo>
        <modulo id="0376">
          <nombre>Implantación de aplicaciones web</nombre>
          <curso>2</curso>
          <horasSemanales>5</horasSemanales>
          <ciclo>ASIR</ciclo>
        </modulo>
      </modulos>
    </ies>

1. Nombre de los módulos del ciclo "Sistemas Microinformáticos y Redes" (en la expresión final no deben aparecer las siglas SMR):

        Aplicaciones web

2. Nombre de los ciclos que incluyen el módulo "Lenguajes de marcas y sistemas de gestión de información":

        Administración de Sistemas Informáticos en Red
        Desarrollo de Aplicaciones Web

3. Nombre de los módulos de ciclos de Grado Superior:

        Gestión de bases de datos
        Lenguajes de marcas y sistemas de gestión de información
        Implantación de aplicaciones web

4. Nombre de los módulos de ciclos cuyo título se aprobó en 2008:

        Aplicaciones web

5. Grado de los ciclos con módulos de primer curso:

        Superior
        Superior
        
