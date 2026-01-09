---
tittle: Clase 5: Vistas en bind9
---

Antes de explicas las vistas, vamos a repasar como se controla el acceso a nuestro DNS.

## Control de acceso

Por defecto podemos consultar a un servidor DNS desde clientes que están en la misma red privada. Si preguntamos desde otra red tenemos que configurar en el fichero `/etc/bind/named.conf.options`, los siguientes parámetros:

* **allow-query**: Especifica cuáles hosts tienen permitido consultar este servidor de nombres.
* **allow-recursion**: Parecida a la anterior, salvo que se aplica a las peticiones recursivas. 

En ambos parámetros se puede poner **any;** para indicar todas las direcciones.

## Vistas en bind9

En alguna circunstancia nos puede interesar **que un mismo nombre que resuelve nuestro DNS devuelve direcciones IP distintas según en qué red esté conectada** el cliente que realiza la consulta.

**Ejemplo**
Una máquina a una red interna con direccionamiento 10.0.0.0/24 y a una red externa 172.22.0.0/16. Vamos a configurar bind9 para que cuando se consulte el nombre del servidor desde la red externa devuelva la ip flotante (172.22.0.129) y cuando la consulta se realice desde la red interna se devuelva la ip fija (10.0.0.13).

En este ejemplo tenemos dos vistas: 

* Vista interna 
* Vista externa

## Definición de las vistas. Vista interna.

Fichero `etc/bind/named.conf.local`:

```
view interna {
    match-clients { 10.0.0.0/24; 127.0.0.1; };
    allow-recursion { any; };   

        zone "example.org"
        {
                type master;
                file "db.interna.example.org";
        };
        zone "0.0.10.in-addr.arpa"
        {
                type master;
                file "db.0.0.10";
        };
        include "/etc/bind/zones.rfc1918";
        include "/etc/bind/named.conf.default-zones";
}; 
```
## Definición de las vistas. Vista externa.
Fichero `etc/bind/named.conf.local`:

```
view externa {
    match-clients { 172.22.0.0/16; };
    allow-recursion { any; };   

        zone "example.org"
        {
                type master;
                file "db.externa.example.org";
        };
        zone "22.172.in-addr.arpa"
        {
                type master;
                file "db.22.172";
        };  
        include "/etc/bind/zones.rfc1918";
        include "/etc/bind/named.conf.default-zones";
};
```

* En la zona definida en **db.interna.example.org** y **db.0.0.10** se define el direccionamiento **10.0.0.0/24**.
* En la zona definida en **db.externa.example.org** y **db.22.172** se define el direccionamiento **172.22.0.0/16**.
* El parámetro **match-clients** nos permite diferenciar la vista que se va a ofrecer según la ip de la petición de la consulta.

