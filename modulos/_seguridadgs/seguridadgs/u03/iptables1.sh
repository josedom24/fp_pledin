iptables -F
iptables -X
iptables -Z
iptables -t nat -F
## Establecemos politica por defecto
iptables -P INPUT ACCEPT
iptables -P OUTPUT ACCEPT

# El localhost se deja (por ejemplo conexiones locales a mysql)
iptables -A INPUT -p tcp -s 127.0.0.1 --dport 3360 -j ACCEPT

#A nuestra IP le dejamos todo, por lo que podrá mandar los paquetes respuesta a las peticiones FTP y MySQL que generan el colega y el diseñador de las reglas siguientes
iptables -A INPUT -s 172.23.0.30 -j ACCEPT

# A un compañero le dejamos entrar al mysql para que mantenga la BBDD
iptables -A INPUT -s 172.22.2.2 -p tcp --dport 3306 -j ACCEPT

# El puerto 80 de www debe estar abierto, es un servidor web (http).
iptables -A INPUT -p tcp --dport 80 -j ACCEPT


# Cerramos rango de los puertos privilegiados. Cuidado con este tipo de
# barreras, antes hay que abrir a los que si tienen acceso.
iptables -A INPUT -p tcp --dport 1:1024 -j DROP
iptables -A INPUT -p udp --dport 1:1024 -j DROP
iptables -A INPUT -p tcp --dport 3306 -j DROP

