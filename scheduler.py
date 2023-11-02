from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
from main import main

# Defina o nome do seu DAG
dag_name = 'scheduler_dag'

# Argumentos padrão do DAG
default_args = {
    'owner': 'Thiago',
    'depends_on_past': False,
    'start_date': datetime(2023, 1, 1),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# Crie uma instância do DAG
dag = DAG(
    dag_name,
    default_args=default_args,
    schedule_interval='@daily',
    catchup=False,
)

def run_script():
    main()

execute_script = PythonOperator(
    task_id='execute_script_task',
    python_callable=run_script,
    dag=dag,
)

execute_script

if __name__ == "__main__":
    dag.cli()
