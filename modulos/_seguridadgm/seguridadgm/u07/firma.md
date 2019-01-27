---
title: "Firma digital con gpg"
permalink: /seguridadgm/u07/firma.html
---

## Firmar y verificar firmas

Una firma digital certifica un documento y le añade una marca de tiempo. Si posteriormente el documento fuera modificado en cualquier modo, el intento de verificar la firma fallaría. La utilidad de una firma digital es la misma que la de una firma escrita a mano, sólo que la digital tiene una resistencia a la falsificación.

Para la creación y verificación de firmas, se utiliza el par público y privado de claves en una operación que es diferente a la de cifrado y descifrado. Se genera una firma con la clave privada del firmante. La firma se verifica por medio de la clave pública correspondiente. 

Puedes seguir el [manual de GPG para firmar y verificas firmas](https://www.gnupg.org/gph/es/manual/x154.html) y realizar los siguientes ejercicios:

{% capture notice-text %}
## Ejercicios

1. Selecciona un documento pdf y encríptalo y fírmalo(opción `--sign`). Envíalo a un compañero, que debe en primer lugar verificar la firma y posteriormente descifrar el documento.
2. Realiza el mismo ejercicio pero obteniendo una firma ASCII.
3. Ahora sólo queremos firmar un documento. Firma un documento (opción `--detach-sig`). A continuación envía el documento original y la firma a un compañero para que verifique que el documento está firmado por tí.
{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>