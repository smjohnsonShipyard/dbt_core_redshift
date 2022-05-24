import subprocess
import os
import json

directory_of_file = os.path.dirname(os.path.realpath(__file__))
dbt_command = os.environ.get('DBT_COMMAND', 'dbt run')

os.chdir(directory_of_file)

subprocess.run(['sh', '-c', dbt_command], check=True)
