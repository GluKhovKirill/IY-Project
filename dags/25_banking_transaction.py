import time
from datetime import datetime
from airflow.operators.python import PythonOperator, get_current_context
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
    def pull_cmd(**query, ):
        #context = get_current_context()
        #context['dag_run'].conf('acc_from')
        #print(dag)
        # query = Variable.get(key="IU25TransactionQuery", deserialize_json=True)
        print("kwargs", query)
        request = """INSERT INTO city."bankAccount" (acc_from, acc_to, amount) VALUES
            ({{ ti.xcom_pull(\'DataBaseInsertHelper\')['from_acc'] }}, {{ti.xcom_pull(\'DataBaseInsertHelper\')['to_acc']}}, {{ti.xcom_pull(\'DataBaseInsertHelper\')['amount']}});"""
        #query['ti'].xcom_pull('DataBaseInsertHelper')
        #request = 'select 1'
        return request

    def helper(**context):
        print(context['dag_run'].conf)

        return context['dag_run'].conf

    def helpertest(**context):
        print(context['ti'].xcom_pull('DataBaseInsertHelper'))

        return context['dag_run'].conf

    run_this_after = PostgresOperator(
        task_id="DataBaseInsert",
        sql=pull_cmd(),
        postgres_conn_id="iu25",
    )

    operator2 = PythonOperator(
        provide_context=True,
        task_id="DataBaseInsertHelper",
        python_callable=helper
    )

    operator3 = PythonOperator(
        provide_context=True,
        task_id="test",
        python_callable=helpertest
    )
    operator2 >>operator3>> run_this_after
