#
# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

"""Example DAG demonstrating the usage of the BashOperator."""

from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.models import Variable
from banking import bank
from industry import IndustryHandler
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

