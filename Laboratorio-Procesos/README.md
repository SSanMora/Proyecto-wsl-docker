# Laboratorio de Administración de Procesos y Señales del Kernel

Este directorio contiene exclusivamente las herramientas, scripts y guías de ejecución desarrolladas para la simulación de alta contención de hardware, optimización del planificador de Linux y mitigación de hilos críticos en el contenedor.

## 👥 Integrantes del Grupo
* **Integrante 1 (Líder):** [Tu Nombre Completo] - GitHub: [@SSanMora]
* **Integrante 2:** [Nombre de tu compañero] - GitHub: [@usuario2]
* **Integrante 3:** [Nombre de tu compañero] - GitHub: [@usuario3]

## 📁 Contenido de este Módulo
* **script.py:** Generador de caos matemático programado en Python para forzar la saturación de los núcleos de procesamiento.
* **Zombi.java:** Script experimental concurrente en Java diseñado para inducir descriptores huérfanos en estado Z sin recolección de llamadas wait().

## 🚀 Instrucciones de Ejecución de las Pruebas

### 1. Monitoreo e Inyección de Caos (Python)
Para desplegar el bucle infinito que satura los núcleos lógicos del sistema, ejecute dentro del contenedor:
```bash
python3 Laboratorio-Procesos/script.py &
```

### 2. Generación del Estado Zombi (Java)
Para evaluar el comportamiento de los descriptores huérfanos del sistema operativo sin recolección de estado de salida, compile y corra el daemon concurrente:
```bash
javac Laboratorio-Procesos/Zombi.java
java -cp Laboratorio-Procesos Zombi &
```

## 🛠️ Herramientas de Intervención Documentadas
* **htop:** Telemetría e inspección visual en tiempo real de prioridades.
* **nice / renice:** Alteración dinámica del índice estático de cortesía en el planificador CFS.
* **cpulimit:** Contención rígida mediante el envío asíncrono de señales de suspensión (`SIGSTOP` / `SIGCONT`).
* **kill:** Depuración y terminación forzada utilizando señales asíncronas de Kernel (`SIGTERM` / `SIGKILL`).
