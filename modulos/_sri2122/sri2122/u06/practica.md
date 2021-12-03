---
title: Práctica
---

frontend servidores_web
	bind *:80 #aquí pon la dirección ip del balanceador
	mode http
	stats enable
	stats uri /ha_stats
	stats auth  cda:cda
	default_backend servidores_web_bakend

backend servidores_web_bakend
	mode http
	balance roundrobin
	server uno 10.0.0.10:80 check
	server dos 10.0.0.11:80 check


ab -t 10 -c 100 -h http://www.example.org/wordpress/

hatop -s /run/haproxy/admin.sock