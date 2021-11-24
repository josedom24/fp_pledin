---
title: "El comando ab"
---

La utilidad [ab](http://httpd.apache.org/docs/2.4/programs/ab.html) (Apache Benchmark) sirve para hacer pruebas de carga a un servidor apache. Es un programa que forma parte del apaquete ``apache2-utils``.

Veamos un ejemplo::

	ab -n 1000 -c 5 -k http://localhost/

El anterior comando simula 5 usuarios al mismo tiempo ahciendo 1000 peticiones al servidor web del localhost. La opción -k (keep_alive) habilita la opción de no cerrar la sesión HTTP. Veamos los resultados de este comando::

	Benchmarking localhost (be patient)
	Completed 100 requests
	Completed 200 requests
	Completed 300 requests
	Completed 400 requests
	Completed 500 requests
	Completed 600 requests
	Completed 700 requests
	Completed 800 requests
	Completed 900 requests
	Completed 1000 requests
	Finished 1000 requests	
	

	Server Software:        Apache/2.2.16
	Server Hostname:        localhost
	Server Port:            80	

	Document Path:          /
	Document Length:        42587 bytes	

	Concurrency Level:      5
	Time taken for tests:   0.140 seconds
	Complete requests:      1000
	Failed requests:        0
	Write errors:           0
	Keep-Alive requests:    995
	Total transferred:      42903740 bytes
	HTML transferred:       42587000 bytes
	Requests per second:    7124.44 [#/sec] (mean)
	Time per request:       0.702 [ms] (mean)
	Time per request:       0.140 [ms] (mean, across all concurrent requests)
	Transfer rate:          298500.90 [Kbytes/sec] received	

	Connection Times (ms)
	              min  mean[+/-sd] median   max
	Connect:        0    0   0.1      0       3
	Processing:     0    1   0.1      1       3
	Waiting:        0    0   0.2      0       2
	Total:          0    1   0.2      1       3	

	Percentage of the requests served within a certain time (ms)
	  50%      1
	  66%      1
	  75%      1
	  80%      1
	  90%      1
	  95%      1
	  98%      1
	  99%      1
	 100%      3 (longest request)

Tenemos otra opción donde indicamos el tiempo que va a durar la prueba y el nivel de concurrencia, sería de la siguiente forma:

	ab -t 10 -c 5 -k http://localhost/

En este caso se va a realizar la prueba durante 10 segundos.

