from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

with DAG('batch_ledger', start_date=datetime(2023,1,1)) as dag:
    step1 = BashOperator(
        task_id='step1_process',
        bash_command='python process.py'
    )
    recovery = BashOperator(
        task_id='recovery_rollback',
        bash_command='python rollback.py',
        trigger_rule='one_failed'
    )
    normal = BashOperator(
        task_id='normal_commit',
        bash_command='python commit.py',
        trigger_rule='all_success'
    )
    
    step1 >> [recovery, normal]
