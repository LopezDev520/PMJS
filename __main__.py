from .cli import parser
from .projectmgr import create, delete, edit
from .database.db import initDB
from .errors import ProjectError
import sys


def main():
  initDB()

  args = vars(parser.parse_args())

  args["path"] = args["path"] / args["projectName"]

  print(args)

  match args["command"].lower():
    ### TODO: Create errors for create function
    case "create": create(args.get("projectName"), args.get("path"))

    case "delete":
      try:
        delete(args.get("projectName"), args.get("preserve"))
      except ProjectError as PE:
        print(f"An error ocurred: {PE.args[0]}")

    case "edit":
      try:
        edit(args.get("projectName"))
      except ProjectError as PE:
        print(f"An error ocurred: {PE.args[0]}")

    case "open":
      if args.get("editor"):
        print(f"Opening project {args.get('projectName')} in {args.get('editor')}...")
      else:
        print("Especify an editor with the --editor or -e option")
        sys.exit(1)

if __name__ == "__main__":
  main()