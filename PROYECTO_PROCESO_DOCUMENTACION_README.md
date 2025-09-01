# Generador Master de Proyectos Asistidos por IA

**ESTE ES EL DIRECTORIO MASTER** que genera nuevos proyectos siguiendo la metodología de IA. No solo documenta el proceso, sino que es la fuente para crear proyectos completos.

## Propósito del Proyecto
Este proyecto **ES** la metodología y **GENERA** nuevos proyectos. Define el proceso completo desde reuniones iniciales hasta revisión final, todo asistido por IA, y proporciona las instrucciones para crear proyectos que sigan esta metodología.

## Estructura del Proyecto
- **docs/**: Documentación técnica y transcripciones del desarrollo de la metodología
- **plantillas/**: Plantillas específicas de este proyecto de definición
- **examples/**: Ejemplos de outputs generados durante el desarrollo
- **reglas/**: Reglas y directivas para IA en este proyecto
- **outputs/**: Entregables del proyecto de definición de metodología
- **memoria/**: Memoria persistente del desarrollo de la metodología

## Generación de Nuevos Proyectos
**Para crear un nuevo proyecto que siga esta metodología:**

1. **Crear directorio** del nuevo proyecto
2. **Usar Cursor** con el prompt de `INSTRUCCIONES_GENERAR_PROYECTO.md`
3. **Personalizar** según necesidades específicas del proyecto

## Instrucciones de Configuración
Las instrucciones para configurar la estructura de carpetas y archivos se encuentran en `INSTRUCCIONES_GENERAR_PROYECTO.md` en este mismo directorio.

## Proceso
Este proyecto sigue el proceso descrito en METODOLOGIA_IA_PROYECTOS.md, que incluye reuniones iniciales, investigación asistida, generación de propuestas, desarrollo y revisión, todo asistido por IA.

## Reglas Automáticas para IA
**IMPORTANTE**: Cursor debe seguir estas reglas automáticamente:

- **Memoria**: SIEMPRE actualizar `MEMORIA_PROYECTO_PROCESO_DOCUMENTACION.yaml` después de cambios significativos
- **Formato**: SIEMPRE usar Markdown para documentación
- **Estructura**: SIEMPRE seguir la organización de carpetas definida
- **Revisión**: SIEMPRE cuestionar suposiciones e identificar riesgos
- **Contexto**: SIEMPRE consultar `docs/` antes de generar contenido
- **Proceso**: Seguir la secuencia: Reunión → Investigación → Propuesta → Desarrollo → Revisión

## Archivos de Reglas
- `reglas/REGLAS_ESTILO_IA.yaml`: Directivas de estilo y prompts
- `reglas/REGLAS_CURSOR_IA.yaml`: Reglas específicas para comportamiento automático
- `.cursorrules`: Configuración automática para Cursor

## Nomenclatura
Este proyecto sigue la nomenclatura MAYÚSCULAS_CON_GUIONES para todos los archivos, facilitando la navegación y búsqueda.

## Uso como Generador Master
Este proyecto sirve como **GENERADOR AUTOMÁTICO** para:
- Crear nuevos proyectos que sigan la metodología
- Mantener consistencia en la implementación del proceso
- Actualizar la metodología basándose en experiencia práctica
- Documentar mejoras y refinamientos del método
- Proporcionar prompts listos para usar en Cursor

## Archivos Clave para Generación
- `INSTRUCCIONES_GENERAR_PROYECTO.md`: Instrucciones completas para crear proyectos
- `METODOLOGIA_IA_PROYECTOS.md`: Documentación completa del proceso
- `reglas/`: Reglas adaptables para nuevos proyectos
- `.cursorrules`: Configuración base para Cursor
