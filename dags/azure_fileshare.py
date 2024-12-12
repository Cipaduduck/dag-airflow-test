from airflow import DAG
from airflow.utils.dates import days_ago
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator

# def read_file_from_azure_file_share():
#     # Initialize the AzureFileShareHook
#     with open('/home/airflow/test235566.txt', 'r') as file:
#         content = file.read()
#     print(content)
#     # Print or process the file content
#     print(file_content)
#     print(list_file)

# Define the DAG
with DAG(
    'read_file',
    default_args={'owner': 'airflow'},
    schedule_interval=None,  # Set your schedule or leave as None to trigger manually
    start_date=days_ago(1),
) as dag:
    
    # # Task to read the file
    # read_file_task = PythonOperator(
    #     task_id='read_file_from_azure_file_share',
    #     python_callable=read_file_from_azure_file_share,
    # )
    ls_file = BashOperator(
         task_id='list_file',
        bash_command='touch /opt/airflow/plugin/test.txt'
    )

    ls_file
