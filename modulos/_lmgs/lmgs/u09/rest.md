---
title: "Peticiones a REST API"
permalink: /lmgs/u09/rest.html
---

1. Redmine (sin auth, XML)

		curl "http://dit.gonzalonazareno.org/redmine/projects.xml"

2. Loteria (sin auth,JSON)

		curl "http://api.elpais.com/ws/LoteriaNavidadPremiados?n=12345"

3. Redmine (KEY, XML)

Lo primero que hacemos es guardar nuestra API KEY en una variable de entorno:

		export key="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"

		curl "http://dit.gonzalonazareno.org/redmine/projects.xml?key=$key"

4. Redmine (KEY, JSON)

		curl "http://dit.gonzalonazareno.org/redmine/projects.json?key=$key"

5. Redmine (KEY,XML)

		curl "http://dit.gonzalonazareno.org/redmine/issues.xml?status_id=open&limit=5&project_id=asir1&key=$key"

6. Openweathermap (KEY, XML)

Recuerda guardar tu API KEY en una variable de entorno:

		export open_wheather_key="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"

		curl "http://api.openweathermap.org/data/2.5/weather?q=Sevilla&mode=xml&units=metric&APPID=$open_wheather_key"

7. Openweathermap (KEY, JSON)

		curl "http://api.openweathermap.org/data/2.5/weather?q=Sevilla&mode=json&units=metric&APPID=$open_wheather_key"
