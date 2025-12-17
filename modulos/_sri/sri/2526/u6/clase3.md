---
title: "Caso 2a: Envío de correo desde usuarios del servidor a correos de internet"
---

## Envío de correo desde usuarios del servidor

Con una configuración básica de Postfix, **técnicamente seríamos capaces de enviar correos al exterior**, sin necesidad de utilizar un servidor relay. Sin embargo, hoy en día esto **no garantiza** que los servidores de destino acepten nuestros mensajes.

Aunque no es estrictamente necesario para el envío, es recomendable que nuestro dominio tenga configurado un **registro MX** apuntando al servidor de correo, ya que algunos MTAs lo tienen en cuenta a la hora de evaluar la legitimidad del servidor emisor.

Para que los servidores de correo de destino **confíen en nuestro servidor**, es necesario cumplir una serie de requisitos técnicos y de reputación.

### Requisitos técnicos mínimos

* Disponer de una **IP pública** asociada al VPS.
* Tener configurado un **nombre de host completo (FQDN)** para el servidor (por ejemplo, `mail.midominio.com`).
* Configurar correctamente el **registro PTR (reverse DNS)** de la IP del VPS, que debe apuntar al FQDN del servidor.
* Asegurar que el **registro A** del FQDN apunta a la misma IP del VPS.
* Verificar que el **puerto 25/tcp** no está bloqueado por el proveedor del VPS.

La configuración del registro PTR **no se realiza en el panel DNS del dominio**, sino en el **panel del proveedor del VPS**, ya que el reverse DNS depende del propietario de la IP.

### Reputación de la IP

Además de la configuración técnica, es fundamental que la **IP del servidor tenga buena reputación**. En muchos casos, los correos enviados desde IPs sin reputación o incluidas en listas de bloqueo son rechazados por servidores como Gmail, Hotmail o Yahoo.

Este problema puede darse incluso en VPS con IP estática, especialmente si la IP ha sido utilizada previamente para el envío de spam.

Tenemos muchos sitios para ver la reputación de nuestra dirección IP o si está en alguna lista negra:

* [dnsbl.info](https://www.dnsbl.info/dnsbl-database-check.php)
* [mxtoolbox ](http://mxtoolbox.com/blacklists.aspx)
* [Spamhaus Block List ](http://www.spamhaus.org/sbl/index.lasso)

### Asegurar que el correo llegue

Incluso cumpliendo los requisitos anteriores, es posible que los servidores de destino no acepten nuestros correos como válidos. Para ello, es necesario implementar una serie de mecanismos que permiten **verificar la legitimidad del correo**.

A partir del 1 de febrero de 2024, proveedores como Google y Yahoo exigen que los correos cumplan con los estándares **SPF, DKIM y DMARC**:

- **SPF**: autoriza qué servidores pueden enviar correo en nombre de un dominio.
- **DKIM**: garantiza la integridad del mensaje mediante firma criptográfica.
- **DMARC**: indica al servidor receptor qué hacer si SPF o DKIM fallan (rechazar, marcar como spam, etc.).

Estos mecanismos añaden capas adicionales de seguridad, aumentan la confianza en el servidor emisor y reducen la probabilidad de que los correos sean rechazados o marcados como spam.


