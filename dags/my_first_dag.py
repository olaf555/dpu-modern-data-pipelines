from airflow import DAG
from airflow.utils import timezone
from airflow.operators.empty import EmptyOperator

with DAG(
    "my_first_dag",
    start_date=timezone.datetime(2025, 2, 1),
    schedule=None,
    tags=["dpu", "my_first_dag", "hello"],  # Fixed incorrect quotes
):  # Best practice to assign DAG to a variable
    t1 = EmptyOperator(task_id="t1")
    t2 = EmptyOperator(task_id="t2")

    t1 >> t2  # Example of task dependency (optional)
