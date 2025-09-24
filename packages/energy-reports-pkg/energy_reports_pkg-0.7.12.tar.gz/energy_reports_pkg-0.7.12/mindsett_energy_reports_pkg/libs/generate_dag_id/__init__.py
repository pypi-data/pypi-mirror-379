import pathlib

def generate_dag_id(file):

    current_path = pathlib.Path(file)
    current_dir = current_path.parents[1]
    current_dir_str = str(current_dir)

    # directory = current_dir_str.split('_dags')[-1][1:].replace('/', '_')

    project = current_dir_str.split('_pkg')[0].split('/')[-1]

    dag_id = project

    # if directory == '':
    #     dag_id = project
    # else:
    #     dag_id = f"{project}_{directory}"

    return dag_id