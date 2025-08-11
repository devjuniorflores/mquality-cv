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
