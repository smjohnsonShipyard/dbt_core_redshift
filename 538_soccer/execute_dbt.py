import subprocess
import os
import json

dbt_command = os.environ.get('DBT_COMMAND', 'dbt run')

subprocess.run(['sh', '-c', dbt_command], check=True)
