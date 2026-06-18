# Sistema de Gestión de Trámites de Vacaciones
Trabajo Practico Integrador (TPI), Organización Empresarial (OE), Tecnicatura Universitaria en Programación a Distancia (TUPaD), Universidad Tecnológica Nacional (UTN), Argentina.

[![Python Version](https://img.shields.io/badge/python-3.10%2B-blue)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green)](./LICENSE)
[![Status](https://img.shields.io/badge/status-Development-yellow)](https://github.com/Lobin-Hood/TPI_OE-TUPaD)

**Sistema simulado de gestión de solicitudes de vacaciones** desarrollado en Python, con manejo de empleados, trámites de vacaciones y generación de códigos únicos de transacción. Utiliza **Pandas** para procesamiento de datos en CSV y proporciona una interfaz interactiva mediante línea de comandos.

---

## 📋 Tabla de Contenidos

- [Descripción](#descripción)
- [Características](#características)
- [Requisitos Previos](#requisitos-previos)
- [Instalación](#instalación)
- [Uso](#uso)
- [Estructura del Proyecto](#estructura-del-proyecto)
- [Flujo de Proceso (BPMN)](#flujo-de-proceso-bpmn)
- [Archivos de Datos](#archivos-de-datos)
- [Funcionalidades Principales](#funcionalidades-principales)
- [Errores Comunes y Soluciones](#errores-comunes-y-soluciones)
- [Contribución](#contribución)
- [Licencia](#licencia)

---

## 📌 Descripción

**TPI_OE-TUPaD** es un prototipo educativo que simula un sistema de gestión de trámites de vacaciones para una organización empresarial. El sistema permite:

- 📝 Registrar solicitudes de vacaciones de empleados
- 🔍 Consultar el estado de trámites existentes
- 📊 Mantener un registro persistente en archivos CSV
- 🆔 Generar códigos únicos de transacción (`VAC001`, `VAC002`, etc.)
- 📈 Seguimiento del flujo de aprobación de solicitudes

---

## ✨ Características

- **Gestión de Empleados**: Lectura y validación de datos de empleados desde CSV
- **Trámites de Vacaciones**: Creación, seguimiento y actualización de solicitudes
- **Códigos Únicos**: Generación automática de códigos de transacción en formato `VAC###`
- **Persistencia de Datos**: Almacenamiento en archivos CSV (contador, empleados, trámites)
- **Validación de Datos**: Verificación de tipos de datos y formatos de fechas
- **Estados de Trámites**: Flujo de estados (1 → 2 → 66)
- **Interfaz Interactiva**: Menú en línea de comandos para operaciones comunes

---

## 🔧 Requisitos Previos

- **Python** 3.10+
- Librerías: **pandas**, **datetime**

---

## 📦 Instalación

### 1. Clonar el Repositorio

```bash
git clone https://github.com/Lobin-Hood/TPI\_OE-TUPaD.git
cd TPI\_OE-TUPaD
```

---

## 👥 Integrantes del Equipo
- **Azpiroz Dafne** (Comisión 5)
- **Lobo, Pablo** (Comisión 24)
