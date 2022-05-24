import subprocess
import os
import json

dbt_command = os.environ.get('DBT_COMMAND', 'dbt run')
directory_of_file = os.path.dirname(os.path.realpath(__file__))


os.chdir(directory_of_file)
subprocess.run(['sh', '-c', dbt_command], check=True)
