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

## 👥 Integrantes del Grupo
* **Estudiante 1:** Santiago Serrano Morales - serrano.santiago@correounivalle.edu.co
* **Estudiante 2:** Samuel Esteban Peña Jaramillo - samuel.pena@correounivalle.edu.co

## 🏛️ Arquitectura del Entorno
El sistema consta de 5 servicios aislados y comunicados a través de una red virtual tipo `bridge` gestionada mediante Docker Compose:
* **Nginx (Puerto 8080):** Servidor web frontal y Proxy Inverso.
* **Node.js (Puerto 3000 interno):** API nativa ejecutándose en modo seguro (Zero Dependencies).
* **PostgreSQL (Puerto 5432 interno):** Almacén de base de datos relacional con volumen persistente.
* **pgAdmin4 (Puerto 5050):** Panel gráfico web para la administración de la base de datos.
* **Jupyter Lab (Puerto 8888):** Entorno interactivo para análisis de datos.

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
