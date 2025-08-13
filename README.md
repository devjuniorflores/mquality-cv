# Sistema de Monitoreo de Calidad

El objetivo de este proyecto es desarrollar un sistema de monitoreo de calidad basado en visión por computadora, capaz de procesar, anotar, validar y preprocesar datos visuales (imágenes y videos) de manera automatizada.
El sistema integrará manejo de datos, anotación en formatos estándar (YOLO, COCO), validación y versionado con DVC, preprocesamiento y preparación para frameworks de deep learning, y orquestación de pipelines con Airflow.
Este flujo permitirá tener datasets limpios, balanceados y listos para entrenamiento de modelos de detección y clasificación, asegurando reproducibilidad y escalabilidad.


## 📂 Estructura inicial del proyecto
```plaintext
├── data/
│   ├── raw/              # Datos originales (no versionados en Git)
│   └── processed/        # Datos procesados
├── notebooks/            # Jupyter notebooks
├── src/                  # Código fuente
├── .gitignore            # Ignorar data y archivos temporales
├── README.md             # Documentación principal
```
## Procesamiento y Transformación de Frames

En esta etapa del proyecto, el objetivo fue **preprocesar los frames extraídos** para prepararlos para futuras tareas de análisis y modelado.  

### 🔹 Actividades realizadas
1. **Lectura de imágenes con OpenCV**  
   - Uso de `cv2.imread()` para cargar imágenes desde `data/processed`.
   - Verificación de rutas y control de errores para asegurar la carga correcta.

2. **Redimensionamiento (Resize)**  
   - Uso de `cv2.resize()` para normalizar la resolución de los frames a un tamaño estándar (300x300 px).  
   - Esto facilita el procesamiento en modelos de visión por computadora y reduce el costo computacional.

3. **Recorte (Crop)**  
   - Selección de una región específica de interés (`img[y1:y2, x1:x2]`).  
   - El recorte permite centrar el análisis solo en el área relevante de cada frame, eliminando ruido visual.

4. **Exportación de imágenes procesadas**  
   - Guardado con `cv2.imwrite()` de los nuevos archivos (`resized_opencv.png` y `crop_opencv.png`) para uso en las siguientes fases del pipeline.

### Objetivo
Estandarizar y limpiar los frames para que los datos visuales estén listos para análisis, modelado o integración en pipelines de visión por computadora.

## Anotación y Etiquetado de Datos 

En esta fase, nos enfocamos en la creación y validación de datasets anotados para tareas de detección de objetos, utilizando herramientas y formatos estándar del ecosistema de visión por computadora.

### 🔹 Actividades realizadas

- Instalación y configuración de CVAT para anotación colaborativa.  
- Importación y etiquetado de un conjunto de imágenes con bounding boxes y asignación de clases.  
- Exportación de las anotaciones en formatos **YOLO** y **COCO** para máxima compatibilidad con frameworks de deep learning.  
- Validación manual y automatizada de los archivos de anotación YOLO (`.txt`), asegurando que las coordenadas estén correctamente normalizadas entre 0 y 1.  
- Exploración de la estructura del archivo JSON de COCO, identificando y comprendiendo sus componentes clave: `images`, `annotations` y `categories`.

### 🔹 Resultados y aprendizajes clave

- Comprensión profunda de los formatos de anotación y su impacto en el entrenamiento de modelos.  
- Implementación de un script en Python para validar la calidad y consistencia de las anotaciones YOLO, reduciendo errores y mejorando la confiabilidad del dataset. (validacion_txtYolo.ipynb) 
- Familiarización con el flujo completo de anotación, exportación y validación, sentando las bases para la integración con pipelines de entrenamiento.

### Objetivo
Consolidar un flujo completo y confiable de anotación y validación de datos visuales, utilizando formatos estándar (YOLO y COCO), que permita generar datasets de alta calidad listos para entrenamiento de modelos de visión por computadora. Esto asegura que las anotaciones sean precisas, consistentes y compatibles con múltiples frameworks, facilitando el desarrollo eficiente y escalable de soluciones de detección y clasificación.

## Validación de Dataset y Configuración de Remoto S3 con DVC

### 🔍 Actividades realizadas
- Verificación de que las etiquetas coincidan con las imágenes y registro de las que no están etiquetadas en un `.csv`.
- Detección de imágenes **duplicadas** (mismo hash) y **corruptas** (archivos incompletos o ilegibles).
- Comprensión de la estructura interna del cache de DVC (`.dvc/cache`), con subcarpetas basadas en los primeros 2 caracteres del hash.
- Ejecución de `dvc push` para subir el dataset validado al bucket S3.

### 📚 Conocimientos consolidados
- Uso de **hashes SHA-256** para identificar y deduplicar archivos.
- Relación entre cache local de DVC y almacenamiento remoto.

### Objetivo
Validar la integridad y consistencia del dataset, eliminando duplicados y detectando archivos corruptos, para luego configurar y subir el conjunto de datos a un almacenamiento remoto en Amazon S3 mediante DVC.

## Preprocesamiento

### 🔹 Actividades realizadas
1. **Resize uniforme** de las imágenes a dimensiones estándar (ej. `640x640`).
2. **Normalización** de valores de píxeles a escala `[0,1]` (px/255).
3. **Data augmentation** con rotaciones, flips, y blur para aumentar diversidad.
4. **Balanceo de clases** mediante técnicas de oversampling (creación de datos sintéticos).
5. **Estructuración final** del dataset en `data/processed/` manteniendo subcarpetas por clase.
6. **Creación de validador** para verificar integridad y conteo de imágenes por clase.
7. **Discusión sobre versionado con DVC**:
   - **Versionar:** `raw/` y `processed/`
   - **No versionar:** `temp/` (datos intermedios regenerables)

---

### 📌 Conocimientos reforzados
- Identificación y corrección de **desbalance de clases**.
- Importancia de la **normalización de datos** y escalas correctas (`[0,1]` o `[-1,1]`).
- Uso de **data augmentation** para robustecer el modelo.
- Buenas prácticas en **gobernanza de datos** con DVC.
- Diferencia entre datos **intermedios** y datos **versionables**.

  **Objetivo del día:**  
Implementar el pipeline de preprocesamiento y dejar el dataset listo para entrenamiento.
