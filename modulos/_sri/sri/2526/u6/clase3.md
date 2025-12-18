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

* **SPF**: autoriza qué servidores pueden enviar correo en nombre de un dominio.
* **DKIM**: garantiza la integridad del mensaje mediante firma criptográfica.
* **DMARC**: indica al servidor receptor qué hacer si SPF o DKIM fallan (rechazar, marcar como spam, etc.).

Estos mecanismos añaden capas adicionales de seguridad, aumentan la confianza en el servidor emisor y reducen la probabilidad de que los correos sean rechazados o marcados como spam.

## La cola de correo en Postfix

Cuando un servidor de correo no puede entregar un mensaje de forma inmediata, este se almacena temporalmente en la **cola de correo** (*mail queue*). Postfix utiliza la cola para gestionar reintentos de entrega y evitar la pérdida de mensajes.

Un correo puede quedar en la cola por distintos motivos:
* el servidor de destino no está disponible,
* existe un error temporal en la conexión,
* se ha producido un fallo momentáneo en la resolución DNS,
* el servidor remoto ha respondido con un error temporal (códigos 4xx).

Postfix intenta reenviar automáticamente los mensajes que se encuentran en la cola durante un periodo de tiempo configurable. Si tras varios intentos el correo no puede entregarse, se genera un mensaje de error para el remitente.

### Consultar la cola de correo

Para visualizar el contenido de la cola de correo se puede utilizar el comando:

```
mailq
```

o de forma equivalente:

```
postqueue -p
```

Estos comandos muestran los mensajes pendientes de entrega, indicando información como el identificador del mensaje, el destinatario y el motivo por el que sigue en la cola.

### Forzar el reintento de envío

Si se desea forzar un nuevo intento de entrega de los correos en cola, se puede utilizar:

```
postqueue -f
```

Este comando ordena a Postfix que reintente inmediatamente el envío de todos los mensajes pendientes.

### Eliminación de mensajes de la cola

En situaciones excepcionales, un administrador puede eliminar mensajes de la cola de correo, por ejemplo cuando existen correos atascados, mensajes no deseados o errores persistentes que impiden su entrega. Esta operación debe realizarse con **precaución**, ya que implica la **pérdida definitiva del mensaje**.

Antes de eliminar mensajes, es recomendable consultar el contenido de la cola para identificar qué correos están pendientes. Para eliminar **un mensaje concreto** de la cola, se utiliza su identificador (ID):

```
postsuper -d ID_DEL_MENSAJE
```

Si se desea eliminar **todos los mensajes de la cola**, se puede ejecutar:
```
postsuper -d ALL
```

También es posible eliminar únicamente los mensajes **diferidos** (pendientes por errores temporales):

```
postsuper -d ALL deferred
```

La gestión de la cola es una tarea habitual en la administración de servidores de correo y resulta fundamental para **diagnosticar y resolver problemas de entrega**, ya que la cola suele ser un síntoma de un problema de configuración o de conectividad con otros servidores.


