#!/usr/bin/env python3
# app.py

from flask import Flask, jsonify, send_file, render_template_string, send_from_directory
from flask_cors import CORS
import json
import os

app = Flask(__name__)
CORS(app)  # Permitir CORS para el frontend

# Datos del curso
CURSO_DATA = {
    "titulo": "Uso de Impresoras 3D",
    "descripcion": "Un curso introductorio sobre impresión 3D que te enseñará desde los conceptos básicos hasta la creación de objetos funcionales. Aprenderás sobre tipos de impresoras, materiales, software de diseño, y técnicas de impresión para llevar tus ideas del mundo digital al físico.",
    "duracion_horas": 12,
    "nivel": "Básico",
    "categoria": "Tecnología"
}

@app.route('/api/curso', methods=['GET'])
def get_curso():
    """Endpoint principal para obtener información del curso"""
    try:
        # Intentar leer desde archivo JSON si existe
        if os.path.exists('curso.json'):
            with open('curso.json', 'r', encoding='utf-8') as f:
                data = json.load(f)
            return jsonify(data)
        else:
            # Si no existe el archivo
            return jsonify(CURSO_DATA)
    except Exception as e:
        return jsonify({
            "error": "Error interno del servidor",
            "message": str(e)
        }), 500

@app.route('/curso.json', methods=['GET'])
def get_curso_json():
    """Servir el archivo curso.json directamente"""
    try:
        if os.path.exists('curso.json'):
            return send_file('curso.json', mimetype='application/json')
        else:
            # Crear el archivo si no existe
            with open('curso.json', 'w', encoding='utf-8') as f:
                json.dump(CURSO_DATA, f, ensure_ascii=False, indent=2)
            return send_file('curso.json', mimetype='application/json')
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/', methods=['GET'])
def index():
    """Página principal con información de la API"""
    return """
    <h1>API Aula STEAM - Curso Impresoras 3D</h1>
    <h2>Endpoints disponibles:</h2>
    <ul>
        <li><a href="/api/curso">/api/curso</a> - Información del curso (JSON)</li>
        <li><a href="/curso.json">/curso.json</a> - Archivo JSON directo</li>
        <li><a href="/curso">/curso</a> - Página del curso</li>
    </ul>
    """

@app.route('/curso', methods=['GET'])
def curso_page():
    """Servir la página del curso"""
    try:
        with open('index.html', 'r', encoding='utf-8') as f:
            html_content = f.read()
        return html_content
    except Exception as e:
        return f"Error cargando la página: {str(e)}", 500

@app.route('/health', methods=['GET'])
def health_check():
    """Endpoint para verificar que el servidor esté funcionando"""
    return jsonify({
        "status": "OK",
        "message": "Servidor API funcionando correctamente",
        "endpoints": ["/api/curso", "/curso.json", "/curso"]
    })

@app.route('/style.css')
def get_style():
    """Servir el archivo CSS"""
    return send_file('style.css', mimetype='text/css')

@app.errorhandler(404)
def not_found(error):
    return jsonify({
        "error": "Endpoint no encontrado",
        "available_endpoints": ["/api/curso", "/curso.json", "/curso"]
    }), 404

if __name__ == '__main__':
    # Crear archivo curso.json si no existe
    if not os.path.exists('curso.json'):
        with open('curso.json', 'w', encoding='utf-8') as f:
            json.dump(CURSO_DATA, f, ensure_ascii=False, indent=2)
        print("Archivo curso.json creado")
    
    print("Iniciando servidor Flask...")
    print("API disponible en: http://localhost:5000/api/curso")
    print("JSON directo en: http://localhost:5000/curso.json")
    
    app.run(debug=True, host='0.0.0.0', port=5000)
