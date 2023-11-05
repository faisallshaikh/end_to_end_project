import os
from pathlib import Path

project_name = "ML_Project"

dir_file = os.getcwd()

list_of_components = [
    f"\\src\\__init__.py",
    f"\\src\\{project_name}\\__init__.py",
    f"\\src\\{project_name}\\components\\data_ingestion.py",
    f"\\src\\{project_name}\\components\\data_transform.py",
    f"\\src\\{project_name}\\components\\model_trainer.py",
    f"\\src\\{project_name}\\components\\model_monitor.py",
    "\\src\\exception.py",
    "\\src\\logger.py",
    "\\setup.py",
    "\\requirements.txt",
    "\\src\\utils.py",
    "\\src\\data_from_sql.py",
    "\\.env"

]

for file in list_of_components:

    filepath = dir_file + file
    whole_path = Path(filepath)
    dir_name , file_name = os.path.split(whole_path)

    os.makedirs(dir_name, exist_ok=True)

    if os.path.exists(filepath):
        pass

    if (not os.path.exists(filepath)):
        with open(filepath, 'w') as f:
            pass

    
            
