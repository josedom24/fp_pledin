## FLUSH de reglas
iptables -F
iptables -X
iptables -Z
iptables -t nat -F

## Establecemos politica por defecto: DROP
iptables -P INPUT DROP
iptables -P OUTPUT DROP
iptables -P FORWARD DROP

## Empezamos a filtrar? no! empezamos a abrir! porque ahora esta TODO denegado.
## Debemos decir de manera explicita qué es lo que queremos abrir

# Operar en localhost sin limitaciones
iptables -A INPUT -i lo -j ACCEPT
iptables -A OUTPUT -o lo -j ACCEPT

# A nuestra IP le dejamos todo
iptables -A INPUT -s 172.23.0.30 -j ACCEPT
iptables -A OUTPUT -d 172.23.0.30 -j ACCEPT

# Permitimos el acceso a la web
iptables -A INPUT -p tcp -m tcp --dport 80 -j ACCEPT
iptables -A OUTPUT -p tcp -m tcp --sport 80 -m state --state RELATED,ESTABLISHED -j ACCEPT


# A un compañero le dejamos entrar al mysql para que mantenga la BBDD

iptables -A INPUT -s 10.0.0.6 -p tcp --dport 3306 -j ACCEPT
iptables -A OUTPUT -d 10.0.0.6 -p tcp --sport 3306 -m state --state RELATED,ESTABLISHED -j ACCEPT

# Permitir hacer consultas dns

iptables -A INPUT -s 192.168.202.2 -p udp -m udp --sport 53 -j ACCEPT
iptables -A OUTPUT -d 192.168.202.2 -p udp -m udp --dport 53 -j ACCEPT

# Permitimos que la maquina pueda salir a la web
iptables -A INPUT -p tcp -m tcp --sport 80 -m state --state RELATED,ESTABLISHED -j ACCEPT
iptables -A OUTPUT -p tcp -m tcp --dport 80 -j ACCEPT

# Ya tambien a webs seguras (https en el puerto 443)
iptables -A INPUT -p tcp -m tcp --sport 443 -m state --state RELATED,ESTABLISHED -j ACCEPT
iptables -A OUTPUT -p tcp -m tcp --dport 443 -j ACCEPT

