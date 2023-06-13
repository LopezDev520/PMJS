from ..database.db import sql
from ..errors import ProjectError
from pathlib import Path

def saveProject(project):
  sql(f"""
    UPDATE projects
    SET projectName = '{project['projectName']}',
        path = '{project['path']}'
    WHERE id={project['id']}
  """)

def listProject(project):
  print(f"Project Name: {project['projectName']}")
  print(f"Path: {project['path']}")

def edit(projectName):
  projects = sql(f"SELECT * FROM projects WHERE projectName='{projectName}'")

  ### TODO: Make a interactive console to edit projects
  if len(projects) > 0:
    projectToEdit = {
      'id': projects[0][0],
      'projectName': projects[0][1],
      'path': projects[0][2],
      'createdAt': projects[0][3]
    }

    editing = True

    print(f"Editing {projectToEdit['projectName']}. Type 'exit' to save changes or 'list' to list the actual data")
    print()
    print("Type the number to make changes")
    print("1. Change Name")
    print("2. Change Path")

    while editing:
      prompt = input(f"[{projectToEdit['projectName']}] -> ")

      if prompt == "":
        continue

      if prompt.lower() == "exit":
        editing = False
        saveProject(projectToEdit)

      if prompt.lower() == "ls":
        listProject(projectToEdit)

      try:
        option = int(prompt)

        if option < 1:
          print("Write a valid number")
          continue

        if option == 1:
          print("Editing name...")
          print("Write a new name")
          newName = input(f"{projectToEdit['projectName']} -> ")

          projectToEdit['projectName'] = newName

        if option == 2:
          print("Editing path...")
          print("Write the new path (absolute, start with /)")
          newPath = input(f"{projectToEdit['path']} -> ")

          newPath = Path(newPath)

          if newPath.exists():
            projectToEdit['path'] = newPath
          else:
            print("Write a valid path")
            continue

      except ValueError as e:
        print("Write a number to edit or 'exit' to close the program and save changes")

  else:
    raise ProjectError('Project not found')
