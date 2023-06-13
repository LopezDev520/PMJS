from ..database.db import sql
from ..errors import ProjectError

from shutil import rmtree
import os

def delete(projectName, preserve=None):
  projects = sql(f"SELECT * FROM projects WHERE projectName='{projectName}'")

  if len(projects) > 0:
    projectToDelete = {
      'id': projects[0][0],
      'projectName': projects[0][1],
      'path': projects[0][2],
      'createdAt': projects[0][3]
    }

    sql(f"DELETE FROM projects WHERE id='{projectToDelete['id']}'")

    if not preserve:
      rmtree(projectToDelete["path"])

  else:
    raise ProjectError("Error: Project not found")
