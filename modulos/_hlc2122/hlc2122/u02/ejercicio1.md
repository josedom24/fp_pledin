---
title: "Ejercicio 1: Primeros pasos para el uso de OpenStack"
---

Realiza los siguientes pasos antes de empezar a usar OpenStack en el IES Gonzalo Nazareno:

1. Instala en el navegador donde vayas a acceder a Horizon el certificado de la autoridad de certificación del Gonzalo Nazareno: [Certificado Gonzalo Nazareno](https://dit.gonzalonazareno.org/gestiona/info/documentacion/doc/gonzalonazareno.crt).
2. Accede a `openstack.gonzalonazareno.org` con tu nombre de usuario y contraseña.
3. Sube tu clave pública en **Computación -> Pares de claves -> Importar clave pública**.
4. Abre el puerto 22 en el Grupo de seguridad *default*, en **Red -> Grupos de seguridad -> Administrar reglas**.
5. Prueba ahora a crear una instancia, asignarle una ip flotante y comprobar que puedes acceder por ssh.

Para poder acceder a OpenStack desde casa necesitas configurar una VPN en tu casa.

Para poder acceder a la red local desde el exterior, existe una red privada configurada con OpenVPN que utiliza certificados x509 para autenticar los usuarios y el servidor.

* Genera una clave privada RSA 4096
* Genera una solicitud de firma de certificado (fichero CSR) y súbelo a gestiona
* Descarga el certificado firmado cuando esté disponible
* Instala y configura apropiadamente el cliente openvpn y muestra los registros (logs) del sistema que demuestren que se ha establecido una conexión.
* Cuando hayas establecido la conexión VPN tendrás acceso a la red `172.22.0.0/16` a través de un túnel SSL. Compruébalo haciendo ping a `172.22.0.1`.

Puede seguir la guía que encuentras en la [wiki](https://dit.gonzalonazareno.org/redmine/projects/asir2/wiki/Conexi%C3%B3n_remota_OpenVPN_a_trav%C3%A9s_de_sputnik).

{% capture notice-text %}
## Entrega...

* Una guía de cómo has realizado cada uno de los puntos anteriores.

{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>



