#!/usr/bin/env python3
"""
Generador Automático de Proyectos Asistidos por IA

Este script crea automáticamente la estructura completa de un nuevo proyecto
siguiendo la metodología definida en METODOLOGIA_IA_PROYECTOS.md.

Uso:
    python3 generador_proyecto.py

El script pedirá:
- Nombre del proyecto
- Objetivo del proyecto
- Ruta donde crear el proyecto

Luego creará toda la estructura de carpetas y archivos base.
"""

import os
import sys
from pathlib import Path
from datetime import datetime
import re


def sanitize_filename(name):
    """Convierte un nombre en un identificador válido para archivos."""
    # Solo reemplaza caracteres inválidos para nombres de archivos/carpetas
    # Mantén el nombre tal cual lo escribió el usuario
    sanitized = re.sub(r'[<>:"/\\|?*]', '', name)  # Solo caracteres inválidos
    sanitized = sanitized.strip()  # Quita espacios al inicio y final
    return sanitized


def get_user_input():
    """Obtiene la información del proyecto del usuario."""
    print("🚀 GENERADOR DE PROYECTOS ASISTIDOS POR IA")
    print("=" * 50)

    # Nombre del proyecto
    while True:
        project_name = input("\n📝 Nombre del proyecto: ").strip()
        if project_name:
            break
        print("❌ El nombre del proyecto no puede estar vacío.")

    # Objetivo del proyecto
    while True:
        project_objective = input("\n🎯 Objetivo del proyecto: ").strip()
        if project_objective:
            break
        print("❌ El objetivo del proyecto no puede estar vacío.")

    # Ruta donde crear el proyecto
    default_base_path = "/Users/ant/Library/CloudStorage/Dropbox/2 actions/_Cloud District/* - Proyectos Cloud"
    default_path = os.path.join(default_base_path, sanitize_filename(project_name))
    project_path = input(f"\n📁 Ruta del proyecto (por defecto: {default_path}): ").strip()
    if not project_path:
        project_path = default_path

    return {
        'name': project_name,
        'objective': project_objective,
        'path': Path(project_path),
        'safe_name': sanitize_filename(project_name),
        'date': datetime.now().strftime('%Y-%m-%d')
    }


def create_directory_structure(project_info):
    """Crea la estructura completa de carpetas del proyecto."""
    print("\n🏗️  Creando estructura de carpetas...")

    directories = [
        "",  # directorio raíz
        "docs",
        "docs/transcripciones",
        "docs/docs_tecnicos",
        "plantillas",
        "examples",
        "reglas",
        "outputs",
        "outputs/propuestas",
        "memoria"
    ]

    for directory in directories:
        path = project_info['path'] / directory
        path.mkdir(parents=True, exist_ok=True)
        print(f"  ✅ {directory or 'directorio raíz'}")


def generate_main_readme(project_info):
    """Genera el archivo PROYECTO_[NOMBRE]_README.md principal."""
    content = f"""# Generador Master de Proyectos Asistidos por IA - {project_info['name']}

**ESTE ES EL DIRECTORIO MASTER** que genera y gestiona el proyecto "{project_info['name']}" siguiendo la metodología de IA asistida.

## Propósito del Proyecto
{project_info['objective']}

## Estructura del Proyecto
- **docs/**: Documentación técnica y transcripciones del desarrollo del proyecto
  - transcripciones/TRANSCRIPCIONES_README.md
  - docs_tecnicos/TECNICO_README.md
- **plantillas/**: Plantillas específicas de este proyecto
- **examples/**: Ejemplos de outputs generados durante el desarrollo
- **reglas/**: Reglas y directivas para IA en este proyecto
- **outputs/**: Entregables del proyecto
  - propuestas/ - Versiones de propuestas (V1, V2, FINAL)
- **memoria/**: Memoria persistente del proyecto

## Proceso
Este proyecto sigue el proceso descrito en METODOLOGIA_IA_PROYECTOS.md, que incluye reuniones iniciales, investigación asistida, generación de propuestas, desarrollo y revisión, todo asistido por IA.

## Reglas Automáticas para IA
**IMPORTANTE**: Cursor debe seguir estas reglas automáticamente:

- **Memoria**: SIEMPRE actualizar `MEMORIA_PROYECTO_{project_info['safe_name']}.yaml` después de cambios significativos
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

## Fases del Proyecto
- [ ] **Reunión Inicial**: Recopilar requisitos y objetivos
- [ ] **Investigación**: Análisis de viabilidad y tecnologías
- [ ] **Propuesta**: Definir alcance, presupuesto y riesgos
- [ ] **Desarrollo**: Implementación del proyecto
- [ ] **Revisión**: Validación final y entrega

## Fecha de Inicio
{project_info['date']}

## Estado Actual
🔄 **En Desarrollo** - Proyecto recién creado

---
*Proyecto generado automáticamente siguiendo METODOLOGIA_IA_PROYECTOS.md*
"""

    return content


def generate_docs_readme():
    """Genera el archivo docs/DOCS_README.md."""
    content = """# Documentación del Proyecto

Este directorio contiene toda la documentación técnica y de proceso del proyecto.

## Estructura

### transcripciones/
Contiene las transcripciones de todas las reuniones, llamadas y sesiones importantes del proyecto.

- `reunion_inicial.md` - Primera reunión con el cliente
- `seguimiento_YYYY-MM-DD.md` - Reuniones de seguimiento
- `revision_final.md` - Reunión de cierre

### docs_tecnicos/
Documentación técnica específica del proyecto.

- `especificaciones.md` - Requisitos técnicos detallados
- `arquitectura.md` - Diseño de la solución
- `investigacion.md` - Análisis técnico realizado
- `recopilacion_fuentes_referencia.md` - Fuentes consultadas

## Convenciones

- Usar formato Markdown para todos los documentos
- Incluir fecha y participantes en transcripciones
- Mantener versión de documentos importantes
- Referenciar fuentes externas cuando sea relevante

## Proceso de Documentación

1. **Reuniones**: Transcribir inmediatamente después
2. **Técnico**: Documentar decisiones y razonamientos
3. **Investigación**: Guardar hallazgos y referencias
4. **Revisiones**: Actualizar documentos según cambios

---
*Actualizado automáticamente*
"""
    return content


def generate_transcripciones_readme():
    """Genera el archivo docs/transcripciones/TRANSCRIPCIONES_README.md."""
    content = """# Transcripciones de Reuniones

Este directorio contiene las transcripciones de todas las reuniones relacionadas con el proyecto.

## Formato de Archivos

Los archivos de transcripción siguen el formato:
```
reunion_[tipo]_[fecha].md
```

### Tipos de Reunión
- `inicial` - Primera reunión con el cliente
- `seguimiento` - Reuniones de progreso
- `revision` - Revisiones de entregables
- `cierre` - Reunión final

## Estructura de Transcripciones

Cada archivo debe incluir:

```markdown
# Reunión [Tipo] - [Fecha]

## Participantes
- Nombre 1 (Rol)
- Nombre 2 (Rol)

## Agenda
1. Tema 1
2. Tema 2

## Notas de la Reunión

### Tema 1
- Punto discutido
- Decisiones tomadas

### Tema 2
- Punto discutido
- Decisiones tomadas

## Acciones Pendientes
- [ ] Acción 1 - Responsable - Fecha límite
- [ ] Acción 2 - Responsable - Fecha límite

## Próxima Reunión
- Fecha: [Fecha]
- Agenda propuesta: [Temas]
```

## Proceso de Transcripción

1. **Durante la reunión**: Tomar notas en tiempo real
2. **Post-reunión**: Completar detalles y limpiar formato
3. **Distribución**: Compartir con participantes relevantes
4. **Archivo**: Mantener en este directorio organizado por fecha

---
*Plantilla para transcripciones del proyecto*
"""
    return content


def generate_tecnico_readme():
    """Genera el archivo docs/docs_tecnicos/TECNICO_README.md."""
    content = """# Documentación Técnica

Este directorio contiene toda la documentación técnica del proyecto, incluyendo especificaciones, arquitectura, investigación y referencias.

## Estructura de Documentos

### especificaciones.md
- Requisitos funcionales y no funcionales
- Casos de uso detallados
- Criterios de aceptación
- Restricciones técnicas

### arquitectura.md
- Diseño de la solución
- Diagramas de componentes
- Flujo de datos
- Decisiones arquitectónicas

### investigacion.md
- Análisis de tecnologías
- Evaluación de alternativas
- Benchmarking
- Recomendaciones técnicas

### recopilacion_fuentes_referencia.md
- Fuentes consultadas
- Artículos relevantes
- Documentación de referencia
- Mejores prácticas identificadas

## Convenciones Técnicas

### Nomenclatura
- Usar PascalCase para componentes
- camelCase para variables y funciones
- kebab-case para archivos y URLs
- UPPER_CASE para constantes

### Documentación de Código
```python
def funcion_ejemplo(parametro):
    \"\"\"Descripción de la función.

    Args:
        parametro: Descripción del parámetro

    Returns:
        Descripción del valor retornado
    \"\"\"
    pass
```

### Diagramas
Usar formato Mermaid para diagramas:
```mermaid
graph TD
    A[Inicio] --> B[Proceso]
    B --> C[Fin]
```

## Versionado Técnico

- Mantener versiones de documentos críticos
- Documentar cambios significativos
- Referenciar versiones en código

---
*Documentación técnica del proyecto*
"""
    return content


def generate_plantillas_readme():
    """Genera el archivo plantillas/PLANTILLAS_README.md."""
    content = """# Plantillas del Proyecto

Este directorio contiene plantillas reutilizables para diferentes tipos de documentos y entregables del proyecto.

## Plantillas Disponibles

### email.md
Plantilla para comunicaciones por email:
- Saludos y presentaciones
- Estructura de contenido
- Cierres profesionales

### propuesta.md
Estructura para propuestas de proyecto:
- Objetivos y alcance
- Metodología
- Cronograma y presupuesto
- Riesgos y mitigaciones

### informe.md
Formato para informes de progreso:
- Resumen ejecutivo
- Estado actual
- Próximos pasos
- Riesgos identificados

### reunion.md
Plantilla para preparación de reuniones:
- Objetivos de la reunión
- Agenda propuesta
- Materiales necesarios
- Participantes esperados

## Uso de Plantillas

1. **Copiar**: Copiar la plantilla al directorio apropiado
2. **Personalizar**: Adaptar contenido al contexto específico
3. **Versionar**: Mantener versiones según evolución
4. **Mejorar**: Actualizar plantillas basadas en experiencia

## Convenciones

- Usar formato Markdown consistente
- Incluir placeholders con [CORCHETES]
- Documentar secciones opcionales
- Mantener ejemplos claros

## Mejora Continua

Las plantillas deben actualizarse regularmente basándose en:
- Retroalimentación de usuarios
- Mejores prácticas identificadas
- Nuevos tipos de documentos requeridos
- Cambios en procesos del proyecto

---
*Plantillas reutilizables del proyecto*
"""
    return content


def generate_ejemplos_readme():
    """Genera el archivo examples/EJEMPLOS_README.md."""
    content = """# Ejemplos del Proyecto

Este directorio contiene ejemplos de outputs generados durante el desarrollo del proyecto.

## Tipos de Ejemplos

### email_ejemplo.md
Ejemplos de emails enviados durante el proyecto:
- Comunicación con cliente
- Coordinación interna
- Reportes de progreso

### propuesta_ejemplo.md
Ejemplos de propuestas generadas:
- Versiones diferentes
- Enfoques alternativos
- Respuestas a RFP

### informe_ejemplo.md
Ejemplos de informes producidos:
- Informes de progreso
- Informes técnicos
- Informes de cierre

## Estructura de Ejemplos

Cada ejemplo debe incluir:
- **Contexto**: Situación en la que se generó
- **Versión**: Número de versión o iteración
- **Resultado**: Impacto o feedback recibido
- **Lecciones**: Aprendizajes obtenidos

## Uso de Ejemplos

Los ejemplos sirven para:
- **Referencia**: Modelos para nuevos documentos
- **Aprendizaje**: Ver evolución del proyecto
- **Calidad**: Mantener estándares consistentes
- **Mejora**: Identificar patrones exitosos

## Archivo de Ejemplos

Crear un nuevo ejemplo:
1. Generar el documento en el contexto apropiado
2. Copiarlo a este directorio con nombre descriptivo
3. Documentar el contexto y resultado
4. Actualizar este README si es necesario

## Histórico

| Fecha | Tipo | Descripción | Resultado |
|-------|------|-------------|-----------|
| - | - | - | - |

---
*Ejemplos del proyecto*
"""
    return content


def generate_outputs_readme():
    """Genera el archivo outputs/OUTPUTS_README.md."""
    content = """# Outputs del Proyecto

Este directorio contiene todos los entregables y resultados generados durante el desarrollo del proyecto.

## Estructura

### propuestas/
Versiones de propuestas y ofertas:
- `propuesta_v1.md` - Primera versión
- `propuesta_v2.md` - Versión revisada
- `propuesta_final.md` - Versión final entregada

### informes/
Informes generados durante el proyecto:
- `informe_progreso_mensual.md`
- `informe_tecnico.md`
- `informe_cierre.md`

### presentaciones/
Materiales de presentación:
- `presentacion_cliente.pdf`
- `demo_prototipo.pdf`

## Versionado

Los documentos importantes siguen el esquema de versionado:
- **v1**: Primera versión completa
- **v2**: Versión con revisiones
- **final**: Versión definitiva entregada

## Convenciones de Nombres

- Usar prefijos descriptivos
- Incluir fechas cuando sea relevante
- Usar guiones bajos para separar palabras
- Mantener consistencia en formato

## Archivo y Organización

1. **Crear**: Generar documento en directorio apropiado
2. **Versionar**: Mantener versiones según evolución
3. **Documentar**: Registrar en este README
4. **Archivar**: Mover versiones obsoletas a subcarpetas

## Calidad de Outputs

Todos los outputs deben:
- ✅ Revisarse por pares
- ✅ Validarse contra requisitos
- ✅ Documentar suposiciones
- ✅ Incluir referencias a fuentes

---
*Entregables del proyecto*
"""
    return content


def generate_reglas_estilo(project_info):
    """Genera el archivo reglas/REGLAS_ESTILO_IA.yaml."""
    content = f"""rules:
  - name: Ser adversarial
    description: Siempre cuestiona suposiciones y identifica riesgos en revisiones.
    prompt_example: "@cursor: Scrutinize this – identify flaws, assumptions, risks."

  - name: Mantener consistencia
    description: Usa Markdown para toda la documentación y sigue la estructura de carpetas.
    prompt_example: "@cursor: Genera output en MD con secciones claras."

  - name: Identificar trade-offs
    description: En propuestas, destaca compromisos y alternativas.
    prompt_example: "@cursor: Examina factibilidad y escalabilidad."

  - name: Personalizar para {project_info['name']}
    description: Adaptar contenido al objetivo específico del proyecto.
    prompt_example: "@cursor: Asegúrate de que este contenido se alinee con el objetivo '{project_info['objective']}'."

  - name: Documentar decisiones
    description: Registrar razonamientos y alternativas consideradas.
    prompt_example: "@cursor: Documenta esta decisión en memoria_proyecto.yaml con alternativas consideradas."
"""
    return content


def generate_reglas_cursor(project_info):
    """Genera el archivo reglas/REGLAS_CURSOR_IA.yaml."""
    content = f"""reglas_cursor:
  description: Reglas específicas para que Cursor siga automáticamente en el proyecto "{project_info['name']}".

  memoria_automatica:
    - regla: "Actualizar MEMORIA_PROYECTO_{project_info['safe_name']}.yaml después de cada cambio significativo"
      descripcion: "Registrar insights, decisiones y razones en la memoria del proyecto"
      prompt: "@cursor: Actualiza memoria_proyecto.yaml con este insight: [descripción]"

    - regla: "Registrar cada interacción importante con la IA"
      descripcion: "Mantener historial de consultas y respuestas relevantes"
      prompt: "@cursor: Registra esta interacción en memoria_proyecto.yaml"

    - regla: "Documentar decisiones y alternativas consideradas"
      descripcion: "Explicar por qué se tomó una decisión y qué otras opciones se evaluaron"
      prompt: "@cursor: Documenta esta decisión en memoria_proyecto.yaml con alternativas consideradas"

  estructura_archivos:
    - regla: "Usar Markdown para toda la documentación"
      descripcion: "Mantener consistencia en el formato de archivos"
      prompt: "@cursor: Genera este contenido en formato Markdown"

    - regla: "Seguir la estructura de carpetas definida"
      descripcion: "Respetar la organización docs/, plantillas/, outputs/, etc."
      prompt: "@cursor: Guarda este archivo en la carpeta [nombre] según la estructura del proyecto"

    - regla: "Versionar outputs con sufijos (v1, v2, final)"
      descripcion: "Mantener historial de versiones de propuestas e informes"
      prompt: "@cursor: Crea la versión [v1/v2/final] de este documento"

  revision_adversarial:
    - regla: "Siempre cuestionar suposiciones en revisiones"
      descripcion: "Identificar y validar premisas ocultas"
      prompt: "@cursor: Examina críticamente este documento - identifica suposiciones no validadas"

    - regla: "Identificar riesgos automáticamente"
      descripcion: "Detectar amenazas potenciales y vulnerabilidades"
      prompt: "@cursor: Analiza este contenido para identificar riesgos y amenazas"

    - regla: "Sugerir alternativas y trade-offs"
      descripcion: "Proponer opciones alternativas y explicar compromisos"
      prompt: "@cursor: Sugiere alternativas a este enfoque y explica los trade-offs"

  contexto:
    - regla: "Consultar docs/ antes de generar contenido"
      descripcion: "Usar RAG para acceder a documentación existente"
      prompt: "@cursor: Basándote en la documentación en docs/, genera [tipo de contenido]"

    - regla: "Referenciar transcripciones en propuestas"
      descripcion: "Incluir citas y referencias a reuniones previas"
      prompt: "@cursor: Integra hallazgos de las transcripciones en docs/transcripciones/"

    - regla: "Integrar hallazgos de investigación"
      descripcion: "Conectar nueva información con investigación previa"
      prompt: "@cursor: Conecta este hallazgo con la investigación existente en docs/docs_tecnicos/"

  output:
    - regla: "Guardar en la carpeta correcta según el tipo"
      descripcion: "Organizar outputs según su naturaleza (propuestas, informes, presentaciones)"
      prompt: "@cursor: Guarda este [tipo de output] en outputs/[carpeta_apropiada]/"

    - regla: "Usar plantillas cuando estén disponibles"
      descripcion: "Aplicar formatos y estructuras predefinidas"
      prompt: "@cursor: Usa la plantilla de [plantillas/nombre_plantilla.md] para este contenido"

    - regla: "Mantener consistencia de formato"
      descripcion: "Aplicar el mismo estilo y estructura en documentos similares"
      prompt: "@cursor: Mantén consistencia con el formato de [documento_referencia]"

  flujo_trabajo:
    - regla: "Seguir el proceso de 5 pasos definido"
      descripcion: "Respetar la secuencia: reunión → investigación → propuesta → desarrollo → revisión"
      prompt: "@cursor: ¿En qué fase del proceso estamos? ¿Qué debería ser el siguiente paso?"

    - regla: "Integrar con Teamwork cuando sea relevante"
      descripcion: "Crear tareas y actualizar estado en .teamwork.yaml"
      prompt: "@cursor: Crea tareas en Teamwork basándote en [documento] y actualiza .teamwork.yaml"

  proyecto_especifico:
    - regla: "Mantener foco en el objetivo del proyecto"
      descripcion: "Asegurar que todas las actividades contribuyan al objetivo '{project_info['objective']}'"
      prompt: "@cursor: ¿Cómo contribuye esta tarea al objetivo principal del proyecto?"

    - regla: "Personalizar outputs para {project_info['name']}"
      descripcion: "Adaptar contenido y formato a las necesidades específicas del proyecto"
      prompt: "@cursor: Personaliza este contenido para el contexto específico de {project_info['name']}"
"""
    return content


def generate_memoria_proyecto(project_info):
    """Genera el archivo memoria/MEMORIA_PROYECTO_[NOMBRE].yaml."""
    content = f"""memoria:
  proyecto:
    nombre: "{project_info['name']}"
    descripcion: "{project_info['objective']}"
    fecha_inicio: "{project_info['date']}"
    estado: "recien_creado"
    fase_actual: "inicio"
    prioridad: "alta"

  estructura_carpetas:
    docs/transcripciones/: "Transcripciones de reuniones y sesiones del proyecto"
    docs/docs_tecnicos/: "Documentación técnica y especificaciones del proyecto"
    plantillas/: "Plantillas reutilizables específicas del proyecto"
    outputs/propuestas/: "Versiones de propuestas (V1, V2, FINAL)"
    reglas/: "Reglas y directivas para IA en este proyecto"
    memoria/: "Memoria persistente y diario del proyecto"
    examples/: "Ejemplos de outputs generados"

  entries:
    - date: "{project_info['date']}"
      tipo: "creacion_proyecto"
      titulo: "Creación automática del proyecto"
      insight: "Proyecto '{project_info['name']}' creado automáticamente siguiendo metodología IA asistida"
      acciones: ["Creación de estructura de carpetas", "Generación de archivos base", "Configuración de reglas"]
      estado: "completado"
      fuente: "Script generador_proyecto.py"

  decisiones_tomadas:
    - fecha: "{project_info['date']}"
      decision: "Proyecto generado automáticamente"
      razon: "Uso del generador master para asegurar consistencia metodológica"
      impacto: "Alto - establece base sólida del proyecto"

  proximos_pasos:
    - accion: "Configurar repositorio Git"
      prioridad: "alta"
      dependencias: []
      estimacion: "30 minutos"

    - accion: "Programar reunión inicial con stakeholders"
      prioridad: "alta"
      dependencias: []
      estimacion: "1-2 días"

    - accion: "Definir alcance detallado del proyecto"
      prioridad: "alta"
      dependencias: ["Reunión inicial"]
      estimacion: "2-3 días"

  metricas:
    archivos_creados: 0
    carpetas_estructuradas: 6
    reglas_definidas: 2
    plantillas_disponibles: 0

  riesgos_identificados:
    - riesgo: "Alcance no claramente definido"
      probabilidad: "alta"
      impacto: "alto"
      mitigacion: "Realizar reunión inicial detallada y documentar requisitos"

    - riesgo: "Falta de participación de stakeholders clave"
      probabilidad: "media"
      impacto: "alto"
      mitigacion: "Identificar y confirmar participación de todos los interesados"

  referencias_documentos:
    - documento: "PROYECTO_{project_info['safe_name']}_README.md"
      proposito: "Documentación principal del proyecto"
      estado: "generado"

    - documento: "reglas/REGLAS_CURSOR_IA.yaml"
      proposito: "Reglas automáticas para comportamiento de IA"
      estado: "generado"

    - documento: "reglas/REGLAS_ESTILO_IA.yaml"
      proposito: "Directivas de estilo y formato"
      estado: "generado"
"""
    return content


def generate_cursorrules(project_info):
    """Genera el archivo .cursorrules."""
    content = f"""# Reglas automáticas para Cursor en el proyecto "{project_info['name']}"

## Contexto del Proyecto
Este proyecto "{project_info['name']}" sigue el proceso asistido por IA descrito en METODOLOGIA_IA_PROYECTOS.md.

**Objetivo**: {project_info['objective']}

## Reglas Obligatorias
- SIEMPRE actualiza MEMORIA_PROYECTO_{project_info['safe_name']}.yaml después de cambios significativos
- SIEMPRE usa Markdown para documentación
- SIEMPRE sigue la estructura de carpetas definida
- SIEMPRE cuestiona suposiciones en revisiones
- SIEMPRE consulta docs/ antes de generar contenido
- SIEMPRE mantén foco en el objetivo: "{project_info['objective']}"

## Estructura de Carpetas
- docs/transcripciones/ - Transcripciones de reuniones
- docs/docs_tecnicos/ - Documentación técnica
- plantillas/ - Plantillas reutilizables
- examples/ - Ejemplos de outputs
- outputs/propuestas/ - Versiones de propuestas (V1, V2, FINAL)
- reglas/ - Reglas y directivas para IA
- memoria/ - Memoria persistente del proyecto

## Archivos de Reglas
- reglas/REGLAS_ESTILO_IA.yaml - Directivas de estilo y prompts
- reglas/REGLAS_CURSOR_IA.yaml - Reglas específicas para comportamiento automático

## Proceso a Seguir
1. Reunión inicial → 2. Investigación → 3. Propuesta → 4. Desarrollo → 5. Revisión

## Comportamiento Adversarial
Siempre identifica riesgos, suposiciones no validadas y sugiere alternativas.

## Proyecto Específico
- Nombre: {project_info['name']}
- Objetivo: {project_info['objective']}
- Fecha inicio: {project_info['date']}
"""
    return content


def generate_teamwork_config(project_info):
    """Genera el archivo .teamwork.yaml."""
    content = f"""# Configuración de Teamwork para el proyecto "{project_info['name']}"

# ID del proyecto en Teamwork (se configurará después de crear el proyecto)
project_id: null

# Configuración de tareas por defecto
default_task_settings:
  priority: "normal"
  estimated_hours: 4
  tags: ["{project_info['safe_name']}"]

# Estados de tareas a mapear
task_status_mapping:
  pendiente: "new"
  en_progreso: "in_progress"
  completada: "completed"
  bloqueada: "on_hold"

# Columnas del board Kanban
kanban_columns:
  - name: "Por Hacer"
    status: "new"
  - name: "En Progreso"
    status: "in_progress"
  - name: "En Revisión"
    status: "pending"
  - name: "Completado"
    status: "completed"

# Configuración de notificaciones
notifications:
  task_assigned: true
  task_completed: true
  project_updates: true

# Integración con fases del proyecto
project_phases:
  - name: "Reunión Inicial"
    description: "Recopilar requisitos y objetivos"
  - name: "Investigación"
    description: "Análisis técnico y viabilidad"
  - name: "Propuesta"
    description: "Definir alcance y presupuesto"
  - name: "Desarrollo"
    description: "Implementación del proyecto"
  - name: "Revisión"
    description: "Validación y entrega final"

# Metadatos del proyecto
metadata:
  nombre: "{project_info['name']}"
  objetivo: "{project_info['objective']}"
  fecha_creacion: "{project_info['date']}"
  metodologia: "IA_Asistida"
"""
    return content


def create_files(project_info):
    """Crea todos los archivos base del proyecto."""
    print("\n📄 Creando archivos base...")

    files_to_create = [
        # Archivo principal
        (f"PROYECTO_{project_info['safe_name']}_README.md", generate_main_readme(project_info)),

        # Documentación
        ("docs/DOCS_README.md", generate_docs_readme()),
        ("docs/transcripciones/TRANSCRIPCIONES_README.md", generate_transcripciones_readme()),
        ("docs/docs_tecnicos/TECNICO_README.md", generate_tecnico_readme()),

        # Plantillas y ejemplos
        ("plantillas/PLANTILLAS_README.md", generate_plantillas_readme()),
        ("examples/EJEMPLOS_README.md", generate_ejemplos_readme()),

        # Outputs
        ("outputs/OUTPUTS_README.md", generate_outputs_readme()),

        # Reglas
        ("reglas/REGLAS_ESTILO_IA.yaml", generate_reglas_estilo(project_info)),
        ("reglas/REGLAS_CURSOR_IA.yaml", generate_reglas_cursor(project_info)),

        # Memoria
        (f"memoria/MEMORIA_PROYECTO_{project_info['safe_name']}.yaml", generate_memoria_proyecto(project_info)),

        # Configuración
        (".cursorrules", generate_cursorrules(project_info)),
        (".teamwork.yaml", generate_teamwork_config(project_info)),
    ]

    for filename, content in files_to_create:
        filepath = project_info['path'] / filename
        filepath.parent.mkdir(parents=True, exist_ok=True)

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)

        print(f"  ✅ {filename}")


def create_gitignore(project_info):
    """Crea un archivo .gitignore básico."""
    content = """# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
*.egg-info/
.installed.cfg
*.egg
MANIFEST

# Virtual environments
venv/
env/
ENV/

# IDE
.vscode/
.idea/
*.swp
*.swo
*~

# OS
.DS_Store
Thumbs.db

# Project specific
outputs/final/
*.log
.env
"""

    filepath = project_info['path'] / '.gitignore'
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

    print("  ✅ .gitignore")


def main():
    """Función principal del generador de proyectos."""
    try:
        # Obtener información del proyecto
        project_info = get_user_input()

        # Confirmar creación
        print(f"\n📋 Resumen del proyecto:")
        print(f"   Nombre: {project_info['name']}")
        print(f"   Objetivo: {project_info['objective']}")
        print(f"   Ruta: {project_info['path']}")

        confirm = input("\n¿Proceder con la creación del proyecto? (s/n): ").strip().lower()
        if confirm not in ['s', 'si', 'yes', 'y']:
            print("❌ Creación cancelada.")
            return

        # Crear estructura de carpetas
        create_directory_structure(project_info)

        # Crear archivos base
        create_files(project_info)

        # Crear .gitignore
        create_gitignore(project_info)

        print("\n🎉 ¡Proyecto creado exitosamente!")
        print(f"📂 Ruta del proyecto: {project_info['path']}")
        print("\n📋 Próximos pasos recomendados:")
        print("1. Revisar y personalizar los archivos generados")
        print("2. Inicializar repositorio Git: git init")
        print("3. Crear primera reunión inicial")
        print("4. Configurar Teamwork si es necesario")
        print("5. Comenzar con la fase de investigación")

        # Moverse al directorio del proyecto y abrir herramientas
        try:
            # Cambiar al directorio del proyecto
            os.chdir(project_info['path'])
            print(f"📂 Cambiado al directorio: {project_info['path']}")

            if sys.platform == "darwin":  # macOS
                # Abrir Cursor en el directorio del proyecto
                print("🚀 Abriendo Cursor...")
                result = os.system("open -a 'Cursor' . 2>/dev/null")
                if result != 0:
                    print("⚠️  No se pudo abrir Cursor automáticamente.")
                    print("   Puedes abrirlo manualmente desde la carpeta del proyecto.")
                # También abrir el Finder para referencia
                os.system(f"open '{project_info['path']}'")
            elif sys.platform == "linux":
                os.system(f"xdg-open '{project_info['path']}'")
                # Intentar abrir VS Code si está disponible
                os.system("code . 2>/dev/null || echo 'Instala VS Code o Cursor para edición automática'")
            elif sys.platform == "win32":
                os.system(f"explorer '{project_info['path']}'")
                # Intentar abrir VS Code si está disponible
                os.system("code . 2>/dev/null || echo 'Instala VS Code o Cursor para edición automática'")
        except Exception as e:
            print(f"⚠️  No se pudo abrir automáticamente el editor: {e}")
            print("Puedes navegar manualmente a la carpeta del proyecto.")

    except KeyboardInterrupt:
        print("\n❌ Proceso interrumpido por el usuario.")
    except Exception as e:
        print(f"\n❌ Error durante la creación del proyecto: {e}")
        return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())
