import os
import hashlib
import pandas as pd
from PIL import Image

# Ruta donde buscar imágenes
carpeta = "data/processed/"

# Extensiones de imagen que vamos a revisar
extensiones = (".jpg", ".jpeg", ".png", ".bmp", ".tiff", ".gif")

# Para guardar resultados
registros = []
hash_dict = {}

def calcular_hash(ruta):
    """Calcular hash SHA256 de un archivo"""
    hash_sha256 = hashlib.sha256()
    with open(ruta, "rb") as f:
        for bloque in iter(lambda: f.read(4096), b""):
            hash_sha256.update(bloque)
    return hash_sha256.hexdigest()

for root, _, files in os.walk(carpeta):
    for file in files:
        if file.lower().endswith(extensiones):
            ruta = os.path.join(root, file)
            try:
                # Validar que la imagen no esté corrupta
                with Image.open(ruta) as img:
                    img.verify()

                # Calcular hash
                hash_img = calcular_hash(ruta)

                if hash_img in hash_dict:
                    # Es un duplicado
                    registros.append({
                        "archivo": ruta,
                        "hash": hash_img,
                        "archivo_duplicado": hash_dict[hash_img],
                        "tipo_problema": "duplicado",
                        "estado": "Error"
                    })
                else:
                    # Guardar como referencia
                    hash_dict[hash_img] = ruta
                    registros.append({
                        "archivo": ruta,
                        "hash": hash_img,
                        "archivo_duplicado": "",
                        "tipo_problema": "",
                        "estado": "OK"
                    })

            except Exception:
                # Imagen corrupta
                registros.append({
                    "archivo": ruta,
                    "hash": None,
                    "archivo_duplicado": "",
                    "tipo_problema": "corrupto",
                    "estado": "Error"
                })

# Guardar reporte
df = pd.DataFrame(registros)
df.to_csv("reports/issuedImgProcessed.csv", index=False, encoding="utf-8")
print("Reporte generado: issuedImgProcessed.csv")
