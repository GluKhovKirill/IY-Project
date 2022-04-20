import time
from datetime import datetime
from airflow.operators.python import PythonOperator
from airflow.models import Variable
from airflow import *
import json
import random

from airflow.providers.postgres.operators.postgres import PostgresOperator
from airflow.operators.trigger_dagrun import TriggerDagRunOperator
default_args = {"not": "used"}
default_args = json.dumps(default_args)
with DAG(
        dag_id='IU25BankExampleInsert',
        schedule_interval=None,
        start_date=datetime(2021, 1, 1),
        catchup=False,
        tags=['example'],
) as dag:
    def push_cmd(**kwargs):
        Variable.set(key="IU25TransactionQuery", value=default_args)

    run_this = PythonOperator(
        task_id="InsertQuery",
        python_callable=push_cmd)

    trigger = TriggerDagRunOperator(
        task_id="InsertTrigger",
        trigger_dag_id='IU25BankTransaction',
        conf={"from_acc":123,"to_acc":456,"amount":random.randint(10, 25)},

    )
    '''
            from_acc=123,  # example from acc id
            to_acc=456,  # example to acc id
            amount=random.randint(10, 25)  # example amount
     '''

    run_this>>trigger
