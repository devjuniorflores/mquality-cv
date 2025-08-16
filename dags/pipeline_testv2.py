from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.empty import EmptyOperator
from datetime import datetime, timedelta

# Configuración por defecto para todas las tareas
default_args = {
    "owner": "data-team",
    "depends_on_past": False,
    "email": ["jndrs2111@gmail.com"],
    "email_on_failure": True,
    "email_on_retry": False,
    "retries": 2,
    "retry_delay": timedelta(minutes=5),
}

# Funciones de ejemplo (puedes reemplazarlas con tus procesos reales)
def extract():
    print("📥 Extrayendo datos...")

def transform():
    print("🛠️ Transformando datos...")

def load():
    print("📦 Cargando datos al destino final...")

# Definición del DAG
with DAG(
    dag_id="etl_template",
    description="Plantilla estándar para DAGs de ETL",
    default_args=default_args,
    start_date=datetime(2025, 8, 14),  # Siempre al menos 1 día antes
    schedule=None,  # Puedes cambiarlo a "0 2 * * *" para diario a las 2am
    catchup=False,
    tags=["etl", "template", "best-practices"],
) as dag:

    inicio = EmptyOperator(task_id="inicio")

    extract_task = PythonOperator(
        task_id="extract",
        python_callable=extract,
    )

    transform_task = PythonOperator(
        task_id="transform",
        python_callable=transform,
    )

    load_task = PythonOperator(
        task_id="load",
        python_callable=load,
    )

    fin = EmptyOperator(task_id="fin")

    # Flujo del DAG
    inicio >> extract_task >> transform_task >> load_task >> fin
