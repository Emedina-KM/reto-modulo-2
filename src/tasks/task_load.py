from prefect import task
from mysql import connector
from config import config


@task(name="Carga de data en bd")
def task_load_character(character_data):
  try:
    with connector.connect(**config.MYSQL_CONFIG) as db:
      with db.cursor() as cursor:
        query_insert = """
          insert into characters(code, names, house, patronus, wand)
          values(%s, %s, %s, %s, %s)
        """
        cursor.execute(query_insert, character_data)
        db.commit()
        
  except Exception as error:
    print(f"Error: {error}")


@task(name="Agregar datos de csv a la bd")
def task_load_csv_character(nickname, code, ancestry):
  try:
    with connector.connect(**config.MYSQL_CONFIG) as db:
      with db.cursor() as cursor:
        query_insert_1 = "update characters set nickname = %s where code = %s"
        cursor.execute(query_insert_1, (nickname, code))
        db.commit()
        
        query_insert_2 = "update characters set ancestry = %s where code = %s"
        cursor.execute(query_insert_2, (ancestry, code))
        db.commit()
  except Exception as error:
    print(f"Error: {error}")
  