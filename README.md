# Proyecto: Mesa de partes digital
Este es el prototipo que hicimos para el curso de Fundamentos de Programación del Grupo 7.
Es un programa en python hecho a partir de lo que observamos como grupo en una mesa de partes, que permite registrar, validar, buscar y listar expedientes, guardándolos en un archivo de texto.

## Grupo 7:
Integrantes:
-Aguilar Ramos Mathew Arom
-Lazaro Yancce Luis Enrique
-Camones Estrada Favio Adriano
-Marquez Valverde Jerson Yair
-Rios Aponte Alvaro Ramiro Higinio

## Que puede hacer?
Con el programa se puede:
- registrar un expediente (DNI, nombres, dirección, trámite y asunto), con validación de cada dato
- buscarlo después por su código, que el programa genera solo (por ejemplo 2026-000001)
- listar todos los expedientes ordenados por código, por nombres o por DNI.

Los datos se guardan en 'expedientes.txt', así que no se pierden al cerrar el programa.

# Como esta organizado el código:
Todo el código esta dentro de la carpeta `src`:
- `main.py`: es el menú principal, desde donde se arranca todo.
- `validaciones.py`: revisa que el DNI, los nombres, los textos y el código estén bien escritos.
- `archivos.py`: guarda y carga los expedientes del archivo de texto.
- `expedientes.py`: registrar y listar expedientes.
- `busqueda.py`: es la búsqueda por código.

## Cómo probarlo
Necesitas tener Python 3. Abre una terminal en la carpeta del proyecto (la que contiene `src`) y ejecuta: "phyton src/main.py"

Es importante hacerlo desde esa carpeta, para que `expedientes.txt` se cree ahí. Ese archivo no se sube al repositorio.