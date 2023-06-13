from pathlib import Path
from datetime import date
from ..database.db import DB_PATH
from ..database.db import sql

import os
import sqlite3

def create(projectName: str, path: Path):
  if path.exists() and path.is_dir():
    print("exists!")
    os.chdir(path.absolute())

    filesInDir = os.listdir()
    if len(filesInDir) > 0:
      print("The folder will be empty")
      return

    sql(f"""
      INSERT INTO 
        projects("projectName", "path", "createdAt") 
        VALUES('{projectName}', '{path.absolute()}', '{date.today().__str__()}')
    """)

    os.chdir(path.absolute())
    os.system("npm init -y")

    print(f"Creation of project finalized! Use the 'pmjs open {projectName}' with the -e option to start working on your project!")

  else:
    os.mkdir(path.absolute())
    create(projectName, path)