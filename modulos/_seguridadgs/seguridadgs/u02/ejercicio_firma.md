---
title: "Firma digital con gpg"
permalink: /seguridadgs/u02/ejercicio_firma.html
---

Una firma digital certifica un documento y le añade una marca de tiempo. Si posteriormente el documento fuera modificado en cualquier modo, el intento de verificar la firma fallaría. La utilidad de una firma digital es la misma que la de una firma escrita a mano, sólo que la digital tiene una resistencia a la falsificación. Por ejemplo, la distribución del código fuente de GnuPG viene firmada con el fin de que los usuarios puedan verificar que no ha habido ninguna manipulación o modificación al código fuente desde que fue archivado.

Sigue el manual de gpg: [Firmar y verificar firmas](https://www.gnupg.org/gph/es/manual/x154.html) para realizar este ejercicio.

{% capture notice-text %}
## Ejercicios

1. Selecciona un documento pdf y encríptalo y fírmalo(opción `--sign`). Envíalo a un compañero, que debe en primer lugar verificar la firma y posteriormente descifrar el documento.

2. Realiza el mismo ejercicio pero obteniendo una firma ASCII.

3. Ahora sólo queremos firmar un documento. Firma un documento (opción `--detach-sign`). A continuación envía el documento original y la firma a un compañero para que verifique que el documento está firmado por tí.

{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>
