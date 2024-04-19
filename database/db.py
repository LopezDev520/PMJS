import sqlite3
from pathlib import Path
import os

user = os.environ.get("USER")
DB_PATH = Path(f"/home/{user}/.config/PMJS/projects.db")

## new change!

def initDB():
  conn = sqlite3.connect(DB_PATH)

  conn.execute("""
  CREATE TABLE IF NOT EXISTS "projects" (
	  "id"	INTEGER,
	  "projectName"	TEXT,
	  "path"	TEXT,
	  "createdAt"	TEXT,
	  PRIMARY KEY("id" AUTOINCREMENT)
  );
  """)

  conn.close()

def sql(query):
  conn = sqlite3.connect(DB_PATH)

  cur = conn.execute(query)

  data = cur.fetchall()

  conn.commit()

  return data