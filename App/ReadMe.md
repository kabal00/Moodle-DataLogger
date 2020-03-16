In Java ist die WebSocket Programmierung unendlich kompliziert. Man muss ein SDK installieren, die keinen Installer hat und es ist total bescheuert gelöst. 
Besser und viel einfacher ist die Umsetzung mit Python. Da muss einfach über pip install websocket nachinstalliert werden und dann ein sehr einfaches Script gestartet werden

Folgende Struktur muss umgesetzt werden:

Moodle muss als WebSocket Client laufen --> Eine in Python/Java programmierte App ist der Server und sendet die Daten an den Client

Große Herausforderung mit Zeitverzögerungen. Anfangs habe ich mit einem time.sleep(1) gearbeitet. Das hat mir alles zerschossen. Die Daten wurden irgendwie gesendet und das Timing wird nicht beachtet. Die Lösung ist ein anderer Befehl: await asyncio.sleep(1). Dazu muss allerdings der Funktion ein async am Anfang angefügt werden und import asyncio.


