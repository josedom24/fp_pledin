# Ejercicio: Temperaturas municipios de Sevilla

Realiza un programa que te pida el nombre de un municipio de la provincia de Sevilla, y si existe te muestre la temperatura máxima y mínima actuales. Para realizar este ejercicio tienes que tener en cuenta los siguiente:

* Para encontrar la temperatura máxima y mínima de un municipio vas a leer el fichero XML que te proporciona la página de la AEMET, por ejemplo el pronostico para Dos Hermanas estaría disponible en la siguiente URL:

		http://www.aemet.es/xml/municipios/localidad_41038.xml
        
* Si te das cuenta para acceder al pronostico de un municipio en partícular debe ir variando el código del municipio, por ejemplo el de Dos Hermanas es el 41038.
* Tienes a tu disposición un fichero [sevilla.xml](http://josedom24.github.io/mod/lm/fich/sevilla.xml) donde tienes la información de todos los municipios con sus respectivos códigos.
* Cuando introduzcas un municipio, deberás buscarlo en ese fichero, si lo encuentras tendrás que obtener el código que te permitirá abrir el fichero xml del pronostico y buescar en él la temperatura máxima y mínima del día actual. Si el municipio no se encuentra dará un mensaje de error.
