#!/usr/bin/env python3
"""
Script de prueba para el generador de proyectos
Simula entrada de usuario para probar el generador automáticamente
"""

import subprocess
import sys
import os
from pathlib import Path

def test_generator():
    """Prueba el generador de proyectos con datos de ejemplo."""

    # Datos de prueba
    test_name = "Sistema de IA para Optimización Empresarial"
    test_objective = "Desarrollar un sistema de inteligencia artificial que optimice procesos empresariales mediante análisis predictivo y automatización inteligente"
    test_path = "./PROYECTO_PRUEBA"

    # Crear input simulado
    input_data = f"{test_name}\n{test_objective}\n{test_path}\ns\n"

    # Ejecutar el generador con input simulado
    process = subprocess.run(
        [sys.executable, "../generador_proyecto.py"],
        input=input_data,
        text=True,
        capture_output=True,
        cwd=Path(__file__).parent
    )

    print("STDOUT:")
    print(process.stdout)
    if process.stderr:
        print("STDERR:")
        print(process.stderr)

    print(f"Exit code: {process.returncode}")

    # Verificar si el proyecto se creó
    if os.path.exists(test_path):
        print(f"✅ Proyecto creado exitosamente en: {test_path}")
        return True
    else:
        print(f"❌ Error: No se encontró el directorio del proyecto en: {test_path}")
        return False

if __name__ == "__main__":
    test_generator()
