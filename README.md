## 📝 Descripción del Proyecto
Este proyecto implementa la orquestación automatizada de un entorno de desarrollo multi-servicio aislado dentro de una distribución de Linux (**Ubuntu en WSL2**), utilizando **Docker** y **Docker Compose**. 

Con el fin de mitigar riesgos críticos recientes de seguridad en la cadena de suministro de software (*Supply Chain Security*) y evitar el secuestro de paquetes en repositorios públicos, el servidor de aplicaciones se migró a una arquitectura de **dependencias cero (Zero-Dependencies)**, empleando únicamente los módulos nativos del núcleo de Node.js en lugar de gestores externos como `npm`. El entorno simula un ecosistema completo de producción con capacidades de balanceo/proxy, almacenamiento persistente relacional, administración gráfica y ciencia de datos.

---

## 🏛️ Arquitectura del Entorno
La infraestructura se despliega sobre una red virtual aislada de Docker tipo `bridge` denominada `red-backbone`. Consta de 5 servicios interconectados:

1. **Nginx (Servidor Web / Proxy Inverso):** Recibe las solicitudes en el puerto `8080` de la máquina anfitriona. Sirve contenido estático y redirige el tráfico de la API de forma transparente.
2. **Node.js Application (API Server):** Servidor HTTP nativo corriendo en el puerto interno `3000` (no expuesto directamente a Windows por seguridad). Procesa peticiones sin dependencias de terceros.
3. **PostgreSQL (Base de Datos):** Servidor de base de datos relacional robusto (puerto interno `5432`). Cuenta con un volumen dedicado para garantizar la persistencia de los datos.
4. **pgAdmin4 (Administración de BD):** Interfaz gráfica basada en web accesible desde el puerto `5050` para la gestión y auditoría de la base de datos.
5. **Jupyter Lab (Ciencia de Datos):** Espacio interactivo seguro montado en el puerto `8888` protegido por token para análisis de datos avanzado.

---

## 🚀 Requisitos Previos
Antes de desplegar el entorno, el sistema anfitrión debe contar con las siguientes tecnologías instaladas y configuradas:
* Windows 10/11 con **WSL2** (Windows Subsystem for Linux) habilitado.
* Distribución oficial de **Ubuntu** (20.04 LTS o superior) operativa en WSL2.
* **Docker Desktop** instalado en Windows con la integración de WSL activa (*WSL integration -> Ubuntu*).
* **Git** instalado en la consola de Ubuntu para el control de versiones.

---

## 🛠️ Pasos de Instalación y Despliegue

### 1. Clonar el repositorio dentro de WSL2:
```bash
git clone [https://github.com/](https://github.com/)[SU_USUARIO_DE_GITHUB]/proyecto-wsl-docker.git
cd proyecto-wsl-docker# Entorno Controlado Multi-Servicio con WSL2 y Docker
```
## 🚀 Requisitos Previos e Instalación
1. Clonar el repositorio en WSL2 (Ubuntu).
2. Crear el archivo `.env` local con las credenciales.
3. Desplegar la infraestructura con:
   ```bash
   docker compose up -d

## 🖨️ Comandos de Administración Utilizados
A lo largo de las sesiones del laboratorio, se utilizaron los siguientes comandos en la terminal de Linux para el control del entorno:

Estructura de archivos: tree . -a (Inspección visual del orden del proyecto).

Estado de los servicios: docker ps (Validación de contenedores activos y mapeo de puertos).

Logs del sistema: docker logs [nombre_contenedor] (Depuración de errores en tiempo real).

Apagado del entorno: docker compose down (Detención de servicios liberando memoria RAM).

Control de versiones: git status, git add ., git commit -m "...", y git push origin main.

---
## 📸 Evidencias de Funcionamiento
⚠️ Nota de entrega: Las siguientes capturas fueron tomadas desde el navegador web en el sistema operativo Windows anfitrión, demostrando la correcta redirección de puertos y el óptimo funcionamiento de cada celda del entorno:

1. Servidor Web Nginx (http://localhost:8080)
<img width="1847" height="227" alt="image" src="https://github.com/user-attachments/assets/b8003f84-202a-4f2c-973d-ca15fcd4255e" />
Muestra la página HTML estática de bienvenida servida directamente por el contenedor de Nginx.

2. API Segura de Node.js (Proxy Inverso - http://localhost:8080/api/)
<img width="1863" height="166" alt="image" src="https://github.com/user-attachments/assets/6ec7d059-118d-422d-92d2-723891b0864b" />
Demuestra que Nginx toma la petición en el puerto 8080, reconoce la ruta /api/ y la transfiere internamente al contenedor aislado de Node.js, el cual responde exitosamente con un objeto JSON generado con código nativo y sin librerías externas.

3. Registro de Base de Datos en pgAdmin (http://localhost:5050)
<img width="1852" height="785" alt="image" src="https://github.com/user-attachments/assets/3aa3042f-4e8c-47c4-abc5-16f53d32acd6" />
Muestra el panel gráfico de administración web donde se inició sesión de forma segura y se enlazó el servidor PostgreSQL apuntando al Host interno de la red de Docker (postgres-db) con las credenciales cargadas desde el archivo .env.

4. Workspace de Jupyter Lab (http://localhost:8888/?token=clavelaboratorio2026)
<img width="1857" height="920" alt="image" src="https://github.com/user-attachments/assets/73e64a4b-a871-4678-aad8-8da3c2896b2f" />
Evidencia del entorno de Jupyter Lab operativo y autenticado mediante el token de seguridad provisto, listo para la ejecución de scripts y notebooks de análisis de datos.

---
## Evidencias de Elaboración del Trabajo

1. Creación del Arbol
<img width="1467" height="590" alt="WhatsApp Image 2026-05-20 at 8 45 48 AM" src="https://github.com/user-attachments/assets/72877aae-579c-422e-b0ba-8a376d3c342e" />

2. Image y los Containers
<img width="1451" height="305" alt="WhatsApp Image 2026-05-20 at 8 45 31 AM" src="https://github.com/user-attachments/assets/f334720e-f7b2-4f78-af82-f888a42f0d52" />

3. Docker Network
<img width="937" height="232" alt="WhatsApp Image 2026-05-20 at 8 46 28 AM" src="https://github.com/user-attachments/assets/923426ab-b192-4e82-ad8d-cd2336dccf10" />

4. Running and Started
<img width="1467" height="210" alt="WhatsApp Image 2026-05-20 at 9 15 10 AM" src="https://github.com/user-attachments/assets/d2d70722-ce05-4449-8c55-5ce30c9b86fa" />

---
##





