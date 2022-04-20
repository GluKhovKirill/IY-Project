import time
from datetime import datetime
from airflow.operators.python import PythonOperator
from airflow.models import Variable
from airflow import *
import json

from airflow.providers.postgres.operators.postgres import PostgresOperator

with DAG(
    dag_id='IU25BankDataBaseSetter',
    schedule_interval=None,
    start_date=datetime(2021, 1, 1),
    catchup=False,
    tags=['test'],
) as dag:
    def createSqlQuery():
        req = '''TRUNCATE TABLE city."bankAccount"; INSERT INTO city."bankAccount" (acc_from, acc_to, amount) VALUES'''
        req += ",".join([f""" (0, {i}, 100000)""" for i in range(1, 100)])

        return "".join(req)

    run_this_before = PostgresOperator(
        task_id="DataBaseSetter",
        sql=createSqlQuery(),
        postgres_conn_id="iu25",
    )