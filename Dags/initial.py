from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.models import Variable
from banking import bank
import json


def initialization():
    Variable.set('incoming_transactions', [])
    Variable.set('outgoing_transactions', [])
    Variable.set('bank_fee', json.dumps(0.1))
    Variable.set('bank_uid', Variable.get('bank_uid', default_var=-1))

    account_uids = [i for i in range(100)]
    Bank = bank.Bank()
    accounts = [Bank.load_account(i) for i in account_uids]

    [i.commit_transaction(-1, 10**6) for i in accounts]

    pass


with DAG(
    dag_id='test_bank',
    # schedule_interval='0 0 * * *',
    start_date=datetime(2021, 1, 1),
    catchup=False,
    dagrun_timeout=timedelta(minutes=60),
    tags=['example', 'example2'],
    # params={"example_key": "example_value"},
) as dag:
    init = PythonOperator(task_id='init_task', python_callable=initialization)
    init


if __name__ == "__main__":
    dag.cli()
