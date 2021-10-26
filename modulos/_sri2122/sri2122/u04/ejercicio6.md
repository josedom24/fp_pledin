---
title: "Ejercicio 7: Instalación y configuración de un servidor DNS dinámico"
---

### DNS dinámico

Instala un servidor DHCP que configure de forma automática a los clientes. Este servidor DHCP debe mandar a los clientes los servidores DNS que deben utilizar.

Configura el servidor DHCP y el DNS maestro para que cada vez que se asigne o modifique una ip a un cliente se actulice de forma automática las zonas del servidor DNS.

{% capture notice-text %}
* Documenta en redmine el proceso que has realizado para configurar un DNS dinámico. Muestra una prueba de funcionamiento.
**Enseña al profesor el funcionamiento del servidor DNS dinámico.**
{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>