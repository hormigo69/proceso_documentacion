# Instrucciones para Generar Nuevos Proyectos

Este directorio es el **MASTER** para crear nuevos proyectos que sigan la metodología de IA. Usa Cursor directamente con los prompts que encontrarás aquí.

## **Método 1: Generación Directa con Cursor**

### **Paso 1: Crear directorio del nuevo proyecto**
```bash
mkdir /ruta/donde/quieras/NOMBRE_PROYECTO
cd /ruta/donde/quieras/NOMBRE_PROYECTO
```

### **Paso 2: Usar este prompt en Cursor:**
```
Basándote en la estructura y metodología definida en [RUTA_A_ESTE_DIRECTORIO_MASTER], crea la estructura completa de carpetas y archivos para un nuevo proyecto llamado "[NOMBRE_PROYECTO]" con objetivo "[OBJETIVO_DEL_PROYECTO]".

Incluye:
- PROYECTO_[NOMBRE]_README.md personalizado
- Estructura de carpetas completa (docs/, plantillas/, examples/, reglas/, outputs/, memoria/)
- Archivos README para cada carpeta
- REGLAS_ESTILO_IA.yaml y REGLAS_CURSOR_IA.yaml adaptados
- MEMORIA_PROYECTO_[NOMBRE].yaml
- .teamwork.yaml con configuración base

Usa la nomenclatura MAYÚSCULAS_CON_GUIONES y personaliza todo según el proyecto específico.
```

## **Método 2: Generación Paso a Paso**

### **Paso 1: Estructura Base**
```
@cursor: Crea la estructura de carpetas base para un proyecto de [TIPO_PROYECTO] siguiendo la metodología de [RUTA_MASTER]
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

**Prompt completo:**
```
Basándote en la estructura y metodología definida en /Users/ant/Library/CloudStorage/Dropbox/2 actions/_Cloud District/Proceso documentación, crea la estructura completa de carpetas y archivos para un nuevo proyecto llamado "Sistema de Scouting de IA para Applus" con objetivo "Desarrollar un sistema de identificación de oportunidades de innovación usando IA".

Incluye toda la estructura con nomenclatura MAYÚSCULAS_CON_GUIONES y personaliza según el proyecto específico.
```

## **Ventajas de este Método:**

✅ **Sin scripts** - Todo con Cursor
✅ **Personalización automática** - Se adapta al proyecto específico
✅ **Consistencia garantizada** - Usa la metodología master
✅ **Flexibilidad total** - Puedes ajustar según necesidades
✅ **Mantenimiento fácil** - Un solo lugar de actualización

## **Nota Importante:**
Este directorio master se actualiza constantemente. Siempre usa la ruta completa para asegurar que Cursor acceda a la versión más reciente de la metodología.
