from email.policy import default
from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.subdag import SubDagOperator
from airflow.utils.task_group import TaskGroup
#from subdags.subdag_parallel_dag import subdag_parallel_dag
from datetime import datetime, timedelta

def subdag_parallel_dag(parent_dag_id, child_dag_id, default_args):
    with DAG(dag_id=f'{parent_dag_id}.{child_dag_id}', default_args=default_args) as dag:
        task_2 = BashOperator(
            task_id='task_2',
            bash_command='sleep 3'
        )

        task_3 = BashOperator(
            task_id='task_3',
            bash_command='sleep 3'
        )

        return dag


# Aqui creamos los default arguments
default_args={
    'owner': 'DavidBU',
    'depends_on_past': True,
    'email': ['dafbustosus@unal.edu.co'],
    'email_on_retry':False,
    'email_on_failure': False,
    'retries':5,
    'retry_delay': timedelta(minutes=1),
    'start_date': datetime(2022,8,4)
}

with DAG(
    dag_id='dag_paralelo', schedule_interval='@daily',default_args=default_args, catchup=False) as dag:
    tarea_1= BashOperator(
        task_id='tarea_1',
        bash_command='sleep 3'
    )

    with TaskGroup('procesando_tareas') as procesando_tareas:
        tarea_2=BashOperator(
            task_id='tarea_2',
            bash_command='sleep 3'
        )

        tarea_3= BashOperator(
            task_id='tarea_3',
            bash_command='sleep 3'
        )

    tarea_4= BashOperator(
        task_id='tarea_4',
        bash_command='sleep 3'
    )

    tarea_1 >> procesando_tareas >> tarea_4