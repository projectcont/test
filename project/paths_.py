from pathlib import Path

def path():
    BASE_DIR = Path(__file__).resolve().parent
    #print('project_directory=',BASE_DIR)
    #print('            ', os.getcwd())
    #print('            ', os.path.abspath(os.curdir))
    #print('project_directory=',os.path.dirname(os.path.abspath(__file__)))
    #print('project_directory=',BASE_DIR)
    #print()
    #abspath = os.path.abspath("database.sqlite")

    return  BASE_DIR


