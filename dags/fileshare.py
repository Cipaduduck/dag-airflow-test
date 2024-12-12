from airflow import DAG
from airflow.providers.microsoft.azure.hooks.fileshare import AzureFileShareHook
from airflow.utils.dates import days_ago
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator

def read_file_from_azure_file_share():
    # Initialize the AzureFileShareHook
    azure_hook = AzureFileShareHook(azure_fileshare_conn_id='test_fileshare')
    
    # Specify the file share, directory, and file name
    file_share_name = 'test'
    directory_name = 'test'
    file_name = 'test.txt'
    
    # Download the file from Azure File Share
    file_content = azure_hook.get_file(file_path="/opt/airflow/dags/test235566.txt",share_name=file_share_name, directory_name=directory_name, file_name=file_name)
    list_file = azure_hook.list_files(share_name=file_share_name, directory_name=directory_name)
    with open('/opt/airflow/dags/test235566.txt', 'r') as file:
        content = file.read()
    print(content)
    # Print or process the file content
    print(file_content)
    print(list_file)

# Define the DAG
with DAG(
    'read_file_from_azure_file_share',
    default_args={'owner': 'airflow'},
    schedule_interval=None,  # Set your schedule or leave as None to trigger manually
    start_date=days_ago(1),
) as dag:
    
    # Task to read the file
    read_file_task = PythonOperator(
        task_id='read_file_from_azure_file_share',
        python_callable=read_file_from_azure_file_share,
    )
    ls_file = BashOperator(
         task_id='list_file',
        bash_command='ls /opt/airflow/dags'
    )

    read_file_task>>ls_file
