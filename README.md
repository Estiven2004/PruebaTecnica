# Aula STEAM - Curso Impresoras 3D

Este proyecto es una API y frontend sencilla para mostrar información sobre un curso introductorio de impresión 3D. Utiliza Flask para el backend y archivos HTML/CSS para la presentación.

## Características

- API en Flask que entrega información de un curso (título, descripción, duración, nivel, categoría)
- Endpoint para obtener el archivo `curso.json`
- Página web del curso (frontend simple)
- Permite CORS para integración con frontend externo
- Endpoint de health check para monitoreo

## Endpoints

- **GET /**  
  Página principal con información de los endpoints disponibles.

- **GET /api/curso**  
  Devuelve la información del curso en formato JSON.

- **GET /curso.json**  
  Descarga directa del archivo JSON del curso.

- **GET /curso**  
  Página web con la información del curso (requiere archivo `index.html`).

- **GET /style.css**  
  Archivo CSS para estilos (requiere archivo `style.css`).

- **GET /health**  
  Verifica el estado del servidor.

## Instalación y uso

1. **Clona el repositorio:**
   ```bash
   git clone https://github.com/Estiven2004/PruebaTecnica.git
   cd PruebaTecnica
   ```

2. **Instala las dependencias:**
   ```bash
   pip install flask flask-cors
   ```

3. **Ejecuta la aplicación:**
   ```bash
   python app.py
   ```

4. **Accede a la API desde tu navegador o herramientas como Postman:**
   - http://localhost:5000/api/curso
   - http://localhost:5000/curso.json
   - http://localhost:5000/curso

## Estructura de archivos

- `app.py` — Código principal de la API en Flask
- `curso.json` — Datos del curso (se crea automáticamente si no existe)
- `index.html` — Página web del curso (debes crearla o personalizarla)
- `style.css` — Estilos para la página web

## Personalización

Puedes modificar el archivo `curso.json` o la variable `CURSO_DATA` en `app.py` para cambiar la información del curso.

## Licencia

Este proyecto está bajo la licencia MIT.
