# Sistema de Gestión de Trámites de Vacaciones
Trabajo Practico Integrador (TPI), Organización Empresarial (OE), Tecnicatura Universitaria en Programación a Distancia (TUPaD), Universidad Tecnológica Nacional (UTN), Argentina.

[![Python Version](https://img.shields.io/badge/python-3.10%2B-blue)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green)](./LICENSE)
[![Status](https://img.shields.io/badge/status-Development-yellow)](https://github.com/Lobin-Hood/TPI_OE-TUPaD)

**Sistema simulado de gestión de solicitudes de vacaciones** desarrollado en Python, con manejo de empleados, trámites de vacaciones y generación de códigos únicos de transacción. Utiliza **Pandas** para procesamiento de datos en CSV y proporciona una interfaz interactiva mediante línea de comandos.

---

## 📌 Diagrama de Flujo (BPMN 2.0)

<img src = "https://drive.google.com/uc?export=view&id=1kmVloGdB2oSu3mk9UkKk5KTVM1fSgpV3" width = "100%">

---

## ✨ Diccionario de Datos

<table>
  <tr><td colspan = "3">Entidad: <b>Empleados</b></b></td></tr>
  <tr><td width = "20%"><b>Campo</b></td><td width = "50%"><b>Tipo</b></td><td width = "30%"><b>Descripción</b></td></tr>
  <tr><td><b>DNI</b></td><td>Cadena de texto (aunque esté compuesto sólo por números, no van a realizarse operaciones aritméticas sobre él)</td><td>Identificador único del/a empleado/a.</td></tr>
  <tr><td><b>dias_disponibles</b></td><td>Número entero</td><td>Cantidad de días de vacaciones disponibles.</td></tr>
</table>

<table>
  <tr><td colspan = "3">Entidad: <b>Trámites</b></b></td></tr>
  <tr><td width = "20%"><b>Campo</b></td><td width = "50%"><b>Tipo</b></td><td width = "30%"><b>Descripción</b></td></tr>
  <tr><td><b>id_tramite</b></td><td>Cadena de texto</td><td>Identificador único del trámite.</td></tr>
  <tr><td><b>id_empleado</b></td><td>Cadena de texto (aunque esté compuesto sólo por números, no van a realizarse operaciones aritméticas sobre él)</td><td>Identificador único del/a empleado/a.</td></tr>
  <tr><td><b>fecha_inicio</b></td><td>Fecha (formato DD/MM/AAAA)</td><td>Fecha solicitada de inicio de vacaciones (inclusive).</td></tr>
  <tr><td><b>fecha_fin</b></td><td>Fecha (formato DD/MM/AAAA)</td><td>Fecha solicitada de fin de vacaciones (inclusive).</td></tr>
  <tr><td><b>estado</b></td><td>Número entero</td><td>Máquina de estados para el proceso de “solicitud de vacaciones”.</td></tr>
</table>

---

## 🔧 Requisitos Previos

- **Python** 3.10+
- Librerías: **pandas**, **datetime**

---

## 📦 Instalación

### 1. Clonar el repositorio

```bash
git clone https://github.com/Lobin-Hood/TPI\_OE-TUPaD.git
cd TPI\_OE-TUPaD
```

### 2. Ubicar los siguientes archivos en los directorios indicados:
<table>
  <tr><td><b>Archivo</b></td><td><b>Ubicación</b></td><td><b>Función</b></td></tr>
  <tr><td><b><a href = "https://drive.google.com/file/d/17Kk2KtaBxW2NaWaoD5yDJF4XzZFmi0qd">empleados.csv</a></b></td><td>/datos/</td><td>Tabla de empleados (validación de identidad y consulta de días disponibles)</td></tr>
  <tr><td><b><a href = "https://drive.google.com/file/d/1V8OWFpMW6H695aE3wYDcl2EFlxsfA6TQ">tramites.csv</a></b></td><td>/estados/</td><td>Tabla de trámites (registro de solicitudes y máquina de estados)</td></tr>
  <tr><td><b><a href = "https://drive.google.com/file/d/1r-EdhvryiGTijJ-a_YKI4DVf30s7O3Xk">contador.csv</a></b></td><td>/estados/</td><td>Registra número de trámites realizados (para generar códigos consecutivos).</td></tr>
</table>

### 3. Ejecutar el archivo principal:
```bash
cd scripts
python bot.py
```

---

## 👥 Integrantes del Equipo
- **Azpiroz, Dafne** (Comisión 5)
- **Lobo, Pablo** (Comisión 24)
