# Ollama en Docker

Este repositorio proporciona un Dockerfile y una guía para desplegar Ollama con FastAPI utilizando Docker. Ollama es un microservicio para la generación de texto utilizando modelos de lenguaje. Esta guía te ayudará a configurar y ejecutar tu propio servicio de generación de texto en un entorno Docker.

![Captura de pantalla del escritorio](Foed.png)

<a href="https://ko-fi.com/P5P013UUGZ">
    <img src="https://github.com/nuntius-dev/badips/raw/main/kofi.png" alt="comprar cafe" width="150" />
</a>

## Requisitos Previos

Asegúrate de tener instalado lo siguiente:

- [Docker](https://www.docker.com/get-started) (versión recomendada: 20.10 o superior)
- [Docker Compose](https://docs.docker.com/compose/install/) (opcional, pero recomendado para facilitar la gestión de contenedores)

## Estructura del Proyecto
/proyecto ├── Dockerfile ├── app.py └── requirements.txt
## Instalación

1. **Clona el repositorio:**

   ```bash
   git clone https://github.com/nuntius-dev/ollama.git
   cd ollama
   ```
2. **Construye la imagen de Docker:**
   ```bash
   docker build -t ollama-fastapi .
   ```
3. Ejecuta el contenedor en modo interactivo:
   ```bash
   docker run -p 80:80 ollama-fastapi
   ```
## Uso
Una vez que el contenedor se esté ejecutando, puedes acceder a la API de Ollama en http://localhost:80.
Para probar la IA, dirígete a http://tu-dominio.com/docs o http://localhost:80/docs

Rutas de la API
- GET /: Retorna un mensaje de bienvenida.

## Ejemplo de respuesta:
  ```bash
  {
      "message": "Bienvenido a la API de TinyLlama"
  }
  ```
- POST /generate: Genera texto basado en un prompt.

## Ejemplo de solicitud:
  ```bash
  {
      "prompt": "Escribe un cuento sobre un dragón."
  }
  ```
- POST /generate: Genera texto basado en un prompt.

## Ejemplo de respuesta:
  ```bash
  {
      "generated_text": "Había una vez un dragón que..."
  }
  ```
# Configuración
Puedes modificar el archivo app.py para personalizar el comportamiento de la API. Asegúrate de instalar las dependencias necesarias en el entorno Docker. El Dockerfile incluye las dependencias de Python requeridas.

Dependencias: Asegúrate de que las principales bibliotecas, como FastAPI, transformers y torch, están correctamente instaladas en tu Dockerfile.
# Advertencias
Asegúrate de que tu servidor tenga suficientes recursos (RAM y CPUs) para ejecutar el modelo de generación de texto, especialmente cuando uses modelos grandes.
Este proyecto debe ser ejecutado en un entorno seguro si planeas exponer la API a Internet.
Contribuciones
Las contribuciones son bienvenidas. Si tienes alguna mejora o corrección, no dudes en abrir un issue o una pull request.


Si quieres saber como instalarlo en docker sigue esta guia: [https://bit.ly/3CPLAyI](https://witmovil.com/guia-rapida-para-instalar-ollama-en-docker-easypanel-fastapi/)




