**Integrantes:**
- Juan Esteban Valencia Zuluaga
- Luis Alejandro Saraza Marin

-  Archivo: app.py
- Problema: El puerto estaba en 5001 en vez de 5000, el status decia "ok", faltaba tiempo en health, nombre de ruta "metric" incorrecto
- Solución: Cambié `port=5001` por `port=5000`, se cambio status a "running", se  importo llibreria time y se implemento, se cambio nombre de ruta a metrics

- Archivo: requeriments.txt
- problema: faltaban pytest y prometheus, status estaba en 
- solucion: se agregaron a requeriments.txt

- Archivo: docker-compose.yml
- problema: El mapeo de puertos era incorrecto 5000:5001
- solucion: Se corrigió a "5000:5000"

- Archivo: prometheus.yml
- Problema: La ruta de métricas estaba mal escrita /metric, target apuntaba a localhost
- Solución: Se cambió la ruta a /metrics y el target a api:5000 para permitir la comunicación entre contenedores
- 
