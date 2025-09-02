# Generador Automático de Proyectos Asistidos por IA

Este script Python automatiza completamente la creación de nuevos proyectos siguiendo la metodología de IA asistida definida en este directorio master.

## 🚀 Uso Rápido

```bash
python3 generador_proyecto.py
```

El script te pedirá:
- **Nombre del proyecto**: El nombre descriptivo del proyecto
- **Objetivo del proyecto**: Descripción clara del propósito principal
- **Ruta del proyecto**: Dónde crear el proyecto (tiene un valor por defecto inteligente)

## 📁 Estructura Generada

El script crea automáticamente toda la estructura de carpetas y archivos:

```
PROYECTO_[NOMBRE]/
├── PROYECTO_[NOMBRE]_README.md          # Documentación principal
├── docs/
│   ├── DOCS_README.md
│   ├── transcripciones/
│   │   └── TRANSCRIPCIONES_README.md
│   └── docs_tecnicos/
│       └── TECNICO_README.md
├── plantillas/
│   └── PLANTILLAS_README.md
├── examples/
│   └── EJEMPLOS_README.md
├── reglas/
│   ├── REGLAS_ESTILO_IA.yaml
│   └── REGLAS_CURSOR_IA.yaml
├── outputs/
│   ├── OUTPUTS_README.md
│   └── propuestas/
├── memoria/
│   └── MEMORIA_PROYECTO_[NOMBRE].yaml
├── .cursorrules                        # Configuración automática para Cursor
├── .teamwork.yaml                       # Configuración base para Teamwork
└── .gitignore                          # Archivo Git básico
```

## 🎯 Características

### ✅ Contenido Personalizado
- Todos los archivos se generan con contenido específico para tu proyecto
- Nombre y objetivo del proyecto se integran automáticamente en todos los documentos
- Fechas de creación y metadatos se incluyen automáticamente

### ✅ Reglas de IA Adaptadas
- `REGLAS_CURSOR_IA.yaml` incluye reglas específicas para el proyecto
- `REGLAS_ESTILO_IA.yaml` personalizadas según el contexto
- `.cursorrules` configura automáticamente el comportamiento de Cursor

### ✅ Memoria del Proyecto
- Archivo YAML de memoria completamente estructurado
- Historial de decisiones y riesgos identificados
- Próximos pasos sugeridos automáticamente

### ✅ Configuración Teamwork
- Archivo `.teamwork.yaml` con configuración base
- Estructura preparada para integración con Teamwork
- Estados y fases del proyecto predefinidos

## 🔧 Requisitos

- **Python 3.6+**
- **Permisos de escritura** en el directorio destino

## 📋 Próximos Pasos Después de la Creación

1. **Revisar archivos generados** y personalizar según necesidades específicas
2. **Inicializar Git**: `git init` en el directorio del proyecto
3. **Crear primera reunión inicial** en `docs/transcripciones/`
4. **Configurar Teamwork** si se va a usar (editar `.teamwork.yaml`)
5. **Comenzar investigación** siguiendo la metodología

## 🎨 Personalización

Todos los archivos generados están listos para usar pero pueden personalizarse:

- **README principal**: Ajustar secciones según necesidades específicas
- **Reglas de IA**: Modificar prompts y comportamientos según el proyecto
- **Estructura**: Agregar carpetas adicionales si son necesarias
- **Memoria**: Expandir con información específica del proyecto

## 🔄 Integración con Metodología

El generador sigue exactamente la metodología definida en:
- `METODOLOGIA_IA_PROYECTOS.md`
- `INSTRUCCIONES_GENERAR_PROYECTO.md`
- `PROYECTO_PROCESO_DOCUMENTACION_README.md`

## 🐛 Solución de Problemas

### Error de permisos
```bash
chmod +x generador_proyecto.py
# O usar python3 directamente
python3 generador_proyecto.py
```

### Error de ruta
- Asegurarse de tener permisos de escritura en el directorio destino
- Verificar que la ruta no contenga caracteres especiales problemáticos

### Error de Python
- Verificar que Python 3.6+ esté instalado: `python3 --version`
- Instalar dependencias si fuera necesario (este script no requiere dependencias externas)

## 📊 Estadísticas de Generación

En cada ejecución, el script genera:
- **13 archivos** de documentación y configuración
- **9 directorios** organizados jerárquicamente
- **Contenido 100% personalizado** basado en el input del usuario
- **Configuración completa** para herramientas de IA y gestión

## 🎉 Beneficios

✅ **Ahorro de tiempo**: Crea estructura completa en segundos
✅ **Consistencia**: Sigue metodología probada
✅ **Personalización**: Adapta todo al proyecto específico
✅ **Preparado para IA**: Configuración automática para Cursor
✅ **Gestión integrada**: Soporte nativo para Teamwork
✅ **Memoria persistente**: Sistema de seguimiento automático

---
*Generado siguiendo la metodología de IA asistida definida en este directorio master*
