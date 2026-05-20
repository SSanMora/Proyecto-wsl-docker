# Entorno Controlado Multi-Servicio con WSL2 y Docker

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
