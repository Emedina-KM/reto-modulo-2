from prefect import task
from mysql import connector
from config import config
from tabulate import tabulate

# Elaboración del inicializador
@task(name="Inicializador de la tabla characters")
def task_init_table():
  try:
    with connector.connect(**config.MYSQL_CONFIG) as db:
      with db.cursor() as cursor:
        #considerar si poner un try o no
        try:
          cursor.execute("drop table if exists characters")
          db.commit()

          cursor.execute("""
            create table characters(
              id int primary key auto_increment,
              code varchar (10) unique,
              names varchar(255) unique,
              house varchar(255),
              patronus varchar(255),
              wand varchar(255),
              nickname varchar(255),
              ancestry varchar(255)
            )
          """)
          db.commit()

        except Exception as error:
          print(f"Error: {error}")

  except Exception as error:
    print(f"Error: {error}")

# En el @flow se dejo el log_prints=False, para que se pueda ver bien la tabla en los logs
@task(name="Mostar datos")
def task_show_characters():
  try:
    with connector.connect(**config.MYSQL_CONFIG) as db:
      with db.cursor() as cursor:
        cursor.execute("select * from characters")

        data = cursor.fetchall()
        print(tabulate(data, headers=cursor.column_names, tablefmt="github"))
  except Exception as error:
    print(f"Error: {error}")
