# Instrucciones para Generar Nuevos Proyectos

Este directorio es el **MASTER** para crear nuevos proyectos que sigan la metodología de IA asistida. Usa el generador automático en Python para máxima eficiencia.

## **Método 1: Generación Automática con Python (RECOMENDADO)**

### **Paso 1: Ejecutar el generador automático**
```bash
cd /ruta/donde/quieras
python3 generador_proyecto.py
```O
```

### **Paso 2: El generador te pedirá:**
- Nombre del proyecto
- Objetivo del proyecto
- Ruta donde crearlo

### **Paso 3: El sistema creará automáticamente:**
- ✅ Estructura completa de carpetas
- ✅ PROYECTO_[NOMBRE]_README.md personalizado
- ✅ Archivos README para cada carpeta
- ✅ REGLAS_ESTILO_IA.yaml y REGLAS_CURSOR_IA.yaml
- ✅ MEMORIA_PROYECTO_[NOMBRE].yaml
- ✅ .teamwork.yaml con configuración base
- ✅ Nomenclatura MAYÚSCULAS_CON_GUIONES aplicada

## **Método 2: Generación Manual con Cursor (Alternativo)**

*Nota: Solo usar si necesitas personalización extrema o el generador Python no está disponible.*

### **Paso 1: Estructura Base**
```
@cursor: Crea la estructura de carpetas base para un proyecto de [TIPO_PROYECTO] siguiendo la metodología de este directorio master
```

### **Paso 2: Personalizar README**
```
@cursor: Genera PROYECTO_[NOMBRE]_README.md para un proyecto de [TIPO_PROYECTO] con objetivo [OBJETIVO]
```

### **Paso 3: Adaptar Reglas**
```
@cursor: Personaliza REGLAS_ESTILO_IA.yaml para un proyecto de [TIPO_PROYECTO]
```

## **Ejemplo de Uso:**

**Proyecto**: "Sistema de Scouting de IA para Applus"
**Objetivo**: "Desarrollar un sistema de identificación de oportunidades de innovación usando IA"

**Comando:**
```bash
python3 generador_proyecto.py
```

**Entradas al generador:**
- Nombre: Sistema de Scouting de IA para Applus
- Objetivo: Desarrollar un sistema de identificación de oportunidades de innovación usando IA
- Ruta: [El sistema sugerirá automáticamente la carpeta "* - Proyectos"]

## **Ventajas del Generador Automático:**

✅ **Automatización completa** - Sin intervención manual
✅ **Consistencia garantizada** - Estructura idéntica en todos los proyectos
✅ **Validación automática** - Verifica entradas y maneja errores
✅ **Personalización inteligente** - Se adapta automáticamente al proyecto
✅ **Tiempo mínimo** - Proyecto completo en segundos
✅ **Mantenimiento centralizado** - Un solo lugar de actualización

## **Nota Importante:**
Este directorio master se actualiza constantemente. El generador Python siempre accede a la versión más reciente de la metodología automáticamente. Para proyectos nuevos, **usa siempre el generador automático** para garantizar consistencia y ahorrar tiempo.
