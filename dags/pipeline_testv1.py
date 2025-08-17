from airflow import DAG
from airflow.operators import PythonOperator
from airflow.operators import EmptyOperator  # reemplazo de DummyOperator
from datetime import datetime

# Definición de funciones
def descargar():
    print("📥 Descargando datos desde repo/bucket...")

def validar():
    print("✅ Validando que cada imagen tenga su label...")

def preprocesar():
    print("🛠️ Preprocesando (resize, normalización, limpieza)...")

def exportar():
    print("📦 Exportando dataset listo para el modelo...")

def registrar_dvc():
    print("🗂️ Registrando dataset en DVC...")

# Definición del DAG
with DAG(
    dag_id="mi_pipeline",
    description="Pipeline de datos automatizado con Airflow",
    start_date=datetime(2025, 8, 14),  # Un día antes para evitar conflictos
    schedule=None,  # ejecución manual (antes era schedule_interval)
    catchup=False,
    tags=["etl", "dataset", "vision"]
) as dag:

    inicio = EmptyOperator(task_id="inicio")

    t1 = PythonOperator(task_id="descargar", python_callable=descargar)
    t2 = PythonOperator(task_id="validar", python_callable=validar)
    t3 = PythonOperator(task_id="preprocesar", python_callable=preprocesar)
    t4 = PythonOperator(task_id="exportar", python_callable=exportar)
    t5 = PythonOperator(task_id="registrar_dvc", python_callable=registrar_dvc)

    fin = EmptyOperator(task_id="fin")

    # Definir orden: inicio → t1 → t2 → t3 → t4 → t5 → fin
    inicio >> t1 >> t2 >> t3 >> t4 >> t5 >> fin
