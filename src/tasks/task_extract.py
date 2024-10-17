import csv
from prefect import task
import requests

@task(name="Extraer info de csv")
def task_extract_csv(filename):
  data = []
  with open(filename, "r") as csv_file:
    csv_reader = csv.DictReader(csv_file, delimiter=",")
    for row in csv_reader:
      tmp_data = (row["code"], row["nickname"], row["ancestry"])
      data.append(tmp_data)
  return data

@task(name="Extraer data de HP-API")
def task_extract_data(code):

  url = "https://hp-api.herokuapp.com/api/characters"
   
  response = requests.get(url)
  if response.status_code == 200:
    data = response.json()
    character = data[int(code)]
    names = character["name"]
    house = character["house"]
    patronus = character["patronus"]
    wand = character["wand"]["core"]
    return(names, house, patronus, wand)
  


 
    