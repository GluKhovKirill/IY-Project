import time
from datetime import datetime
from airflow.operators.python import PythonOperator
from airflow.models import Variable
from airflow import *
import json

from airflow.providers.postgres.operators.postgres import PostgresOperator

args = {
    'owner': 'airflow',
    'provide_context': True
}

with DAG(
    dag_id='IU25BankTransaction',
    schedule_interval=None,
    start_date=datetime(2021, 1, 1),
    catchup=False,
    tags=['dev'],
    default_args=args,
) as dag:
    def pull_cmd(**query):
        # query = Variable.get(key="IU25TransactionQuery", deserialize_json=True)
        print("kwargs", query)
        #request = f"""INSERT INTO city."bankAccount" (acc_from, acc_to, amount) VALUES
        #    ({query['from_acc']}, {query['to_acc']}, {query['amount']});"""
        request = ''
        return request

    run_this_after = PostgresOperator(
        task_id="DataBaseInsert",
        sql=pull_cmd(),
        postgres_conn_id="iu25",
    )
