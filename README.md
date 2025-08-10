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
