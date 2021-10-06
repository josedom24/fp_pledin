---
title: ¿Cómo funciona el servidor DHCP?
---


El protocolo de configuración dinámica de host (Dynamic Host Configuration Protocol – DHCP)  es una extensión de protocolo BOOTP que da más flexibilidad al administrar las direcciones IP.  Este protocolo puede usarse para configurar dinámicamente los parámetros esenciales TCP/IP de los hosts (estaciones de trabajo y servidores)  de una red.  El protocolo DHCP tiene dos elementos:

* Un mecanismo para asignar direcciones IP y otros parámetros TCP/IP. 
* Un protocolo para negociar y transmitir información específica del host. 

El host TCP/IP que solicita la información de configuración TCP/IP se denomina cliente DHCP y el host que provee dicha información se llama servidor DHCP. El DHCP se describe en la norma **RFC 2131** –Protocolo de configuración dinámica de host–.  A continuación, presentamos la operación del DHCP. 

## Administración de direcciones con el DHCP

El protocolo DHCP usa los siguientes 3 métodos para asignar las direcciones IP:

**a) Asignación manual**: El administrador de red pone manualmente la dirección IP del cliente DHCP en el servidor DHCP. El DHCP se usa para dar al cliente DHCP el valor de esta dirección IP configurada manualmente. 

**b) Asignación automática**: No se requiere asignar manualmente direcciones IP.  El servidor DHCP asigna al cliente DHCP, en el primer contacto, una dirección IP permanente que no podrá reutilizar ningún otro cliente DHCP. 
	
**c) Asignación dinámica**: El DHCP asigna una dirección IP al cliente DHCP por un tiempo determinado.  Después que expire este lapso, se revoca la dirección IP y el cliente DHCP tiene que devolverla.  Si el cliente aún necesita una dirección IP para efectuar sus operaciones, deberá solicitarla nuevamente. 

Este protocolo permite la reutilización automática de una dirección IP.  Si un cliente DHCP ya no necesita una dirección IP, como en el caso de un ordenador que apagamos, este libera
su dirección y la entrega al servidor DHCP. Este puede reasignar dicha dirección a otro cliente que la pida. 

El método de asignación dinámica es muy útil para clientes DHCP que necesitan una dirección IP para una conexión temporal a la red. Por ejemplo, consideremos una situación en que 300 usuarios tengan ordenadores portátiles conectados a una red y esta les ha asignado direcciones clase C. Este tipo de dirección permite a la red tener hasta 253 nodos (255 – 2 direcciones especiales = 253). Debido a que los ordenadores que se conectan a una red usando el TCP/IP requieren tener una dirección única IP, entonces los 300 ordenadores no podrían operar simultáneamente. Sin embargo, si solo hay 200 conexiones físicas a la red se puede buscar una dirección de clase C mediante la reutilización de direcciones IP no usadas. Usando el DHCP, en su método de asignación dinámica de direcciones IP, es posible reutilizar direcciones IP. 

Además la asignación dinámica de direcciones IP es un buen método para asignar direcciones IP a ordenadores que van a ser conectados por primera vez y en una red donde escasean las direcciones IP. Si los ordenadores antiguos se retiran, sus direcciones IP pueden ser reutilizadas o reasignadas inmediatamente. Sin importar cuál método se elija, aún puede configurarse los parámetros IP de una sola vez desde un servidor central, en lugar de repetir la configuración TCP/IP para cada ordenador.

## Proceso de configuración de los clientes

Una vez que un cliente DHCP ha contactado con un servidor DHCP, a través de varios estados internos, negocia el uso y la duración de su dirección IP.  La forma de adquisición de la dirección IP por el cliente DHCP se explica mejor en términos de un diagrama de transición de estados (llamado también máquina de estado finito). La figura presenta este diagrama de transición de estados que explica la interacción entre el cliente y el servidor DHCP. 

![dhcp](img/dhcp.png)

### Descubrimiento de un servidor DHCP (SELECTING)

Cuando se inicializa el cliente DHCP, este comienza en el estado de inicialización INIT. El cliente DHCP desconoce sus parámetros IP y por eso envía un broadcast DHCPDISCOVER. El mensaje
DHCPDISCOVER se encapsula en un paquete UDP. Se coloca el número 67 con puerta de destino UDP, el mismo utilizado por el servidor BOOTP, debido a que el protocolo DHCP es una extensión
de este protocolo. El mensaje DHCPDISCOVER usa la dirección IP de broadcast de valor 255. 255. 255. 255.  Si no existe un servidor DHCP en la red local, el router IP debe tener un agente
DHCP relay que soporte la retransmisión de esta petición hacia las otras subredes. El agente DHCP relay se describe en la norma RFC 1542. 

Antes de enviar el mensaje broadcast DHCPDISCOVER, el cliente DHCP espera por un tiempo aleatorio –entre 1 a 10 segundos– para evitar una colisión con otro cliente DHCP, como en el caso
que todos los clientes DHCP se inicialicen al mismo tiempo al recibir todos energía a la vez (como una pérdida o interrupción de la electricidad).

### Aceptación de la asignación recibida (REQUESTING)

Después de enviar el mensaje broadcast DHCPDISCOVER, el cliente DHCP ingresa al estado SELECTING, donde recibe los mensajes DHCPOFFER de los servidores DHCP configurados para
atenderlo. El tiempo que el cliente DHCP esperará por los mensajes DHCPOFFER depende de la implementación.  Si el cliente DHCP recibe varias respuestas DHCPOFFER, elegirá una. En reacción, el cliente DHCP enviará un mensaje DHCPREQUEST para elegir un servidor DHCP, el que contestará con un DHCPACK. 

Como opción, el cliente DHCP controla la dirección IP enviada en el DHCPACK para verificar si está o no está en uso.  En una red con broadcast, el cliente DHCP envía una petición ARP con la dirección IP sugerida para verificar que no esté duplicada. En caso de estarlo, el DHCPACK proveniente del servidor se ignora y se envía un DHCPDECLINE, con lo cual el cliente DHCP ingresa en estado INIT y vuelve a pedir una dirección IP válida que no esté en uso. 

Cuando la petición ARP se difunde sobre la red, el cliente usa su propia dirección de hardware en el campo de dirección fuente de hardware del ARP, pero coloca el valor de 0 en el campo de dirección fuente IP.  Esta dirección de valor 0 se utiliza en lugar de la dirección IP sugerida, para no confundir a las memorias caché ARP de otros hosts. 

### Duración de la concesión (BOUND)

Cuando se acepta el DHCPACK proveniente del servidor DHCP, se colocan tres valores de temporización y el cliente DHCP se mueve al estado BOUND (asociado). 

* T1 es el temporizador de renovación de alquiler. 
* T2 es el temporizador de reenganche. 
* T3 es la duración del alquiler. 

El DHCPACK siempre trae consigo el valor de T3.  Los valores de T1 y T2 se configuran en el servidor DHCP; de no ser así, se usan los valores por defecto siguientes:

* T1 = 0,5 x T3. 
* T2 = 0,875 x T3. 

El tiempo actual en que los temporizadores expiran se calcula añadiendo el valor del temporizador al tiempo en que se envió el mensaje DHCPREQUEST, el cual generó la respuesta DHCPACK. 

Si este tiempo es T0, entonces los valores de expiración se calculan así:

* Expiración de T1 = T0 + T1
* Expiración de T2 = T0 + T2
* Expiración de T3 = T0 + T3

La RFC 2131 recomienda que se debe añadir un factor a T1 y T2 para evitar que varios clientes
DHCP expiren sus temporizadores al mismo tiempo. 

### Renovación de la concesión (RENEWING)

Después de la expiración del temporizador T1, el cliente DHCP se mueve del estado BOUND al estado RENEWING (renovación). En este último estado se debe negociar un nuevo alquiler para la dirección IP designada, entre el cliente DHCP y el servidor DHCP que originalmente le asignó la dirección IP. Si el servidor DHCP original, por algún motivo, no renueva el alquiler, le enviará un mensaje DHCPNACK y el cliente DHCP se moverá al estado INIT e intentará obtener una nueva dirección IP. En el caso contrario, si el servidor DHCP original envía un mensaje DHCPACK, este contendrá la duración del nuevo alquiler. Entonces, el cliente DHCP coloca los valores de sus temporizadores y se moverá al estado BOUND.

### Estado de reenganche (RENEWING)

Si el temporizador T2 (tiempo de reenganche) expira mientras el cliente DHCP está esperando en el estado RENEWING una respuesta sea DHCPACK o DHCPNACK proveniente del servidor DHCP original, el cliente DHCP se moverá al estado REBINDING. El servidor original DHCP podría no haber respondido porque estaría apagado o porque el enlace con la red habría caído. Nótese en las ecuaciones previas que T2 es mayor que T1, de modo que el cliente DHCP espera que el servidor original DHCP renueve el alquiler por un tiempo igual a T2 – T1.

### Extensión de la concesión

Al expirar el temporizador T2 (tiempo de reenganche), el cliente DHCP enviará un DHCPREQUEST a la red para contactar con cualquier servidor DHCP para extender el alquiler, con
lo cual pasará al estado REBINDING. El cliente DHCP envía este mensaje broadcast DHCPREQUEST porque presume que, luego de haber esperado T2 – T1 segundos en el estado RENEWING, el servidor DHCP original no está disponible, por lo cual tratará de contactar con otro servidor DHCP para que le responda.
Si un servidor DHCP responde con un DHCPACK, el cliente DHCP renueva su alquiler (T3), coloca los temporizadores T1 y T2 y retorna al estado BOUND.
Si no hay servidor DHCP disponible para renovar alquiler luego de expirar el temporizador T3, el alquiler cesa y el cliente DHCP pasa al estado INIT.
Nótese que el cliente DHCP intentó renovar el alquiler primero con el servidor original y luego con cualquier otro servidor en la red.

### Expiración de la concesión

Al acabar el alquiler (T3 expira), el cliente DHCP debe devolver su dirección IP y cesar toda acción con dicha dirección IP en la red.
El cliente DHCP no siempre tiene que esperar la expiración del alquiler para terminar el uso de una dirección IP.
Este puede renunciar voluntariamente a una dirección IP, cancelando su alquiler. Por ejemplo, el usuario de un computador portátil podría conectarse a la red para una actividad particular. El servidor DHCP de la red podría colocar la dirección del alquiler por una hora. Suponiendo que el usuario acabe su tarea en 30 minutos, entonces se desconectará de la red al cabo de dicho lapso. Cuando el usuario se libera armoniosamente, el cliente DHCP enviará un mensaje DHCPRELEASE al servidor DHCP para cancelar el alquiler. La dirección IP ahora estará
disponible.

Si los clientes DHCP operan en ordenadores que tienen disco duro, la dirección IP asignada puede ser almacenada en este dispositivo y, cuando la computadora reinicie sus operaciones, puede hacer una nueva petición usando esta dirección IP.
