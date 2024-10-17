from prefect import flow
from tasks.task_utils import task_init_table, task_show_characters
from tasks.task_extract import task_extract_csv, task_extract_data
from tasks.task_load import task_load_character,task_load_csv_character

BASELINE_TASKS = False
DATA_PATH = "./resources/characters.csv"

@flow(name="ETL API***", log_prints=False)
def main_flow():
  if BASELINE_TASKS:
    task_init_table()

  initial_character_data = task_extract_csv(DATA_PATH)
   
  for character in initial_character_data:
    code = character[0]
    nickname = character[1]
    ancestry = character[2]

    api_character_data = task_extract_data(code)
    character_data = (code, *api_character_data,)

    task_load_character(character_data)
    task_load_csv_character(nickname, code, ancestry)
  
  task_show_characters()

if __name__ == "__main__":
  main_flow()