import argparse
import os
from pathlib import Path

parser = argparse.ArgumentParser(
  prog="PMJS",
  description="A simple project manager for your Javascript Web Projects!",
  argument_default=argparse.SUPPRESS,
)

parser.add_argument(
  "command",
  choices=["create", "delete", "edit", "open"],
  help="""
    The command to be executed:
    
    create: Create a project giving a name;
    delete: Delete a project giving the name, use --preserve to preserve the files;
    edit: Give the project name to edit it in an interactive console;
    open: Give the project name and use the --editor to specify a editor to open the project;
    """
)

parser.add_argument(
  "projectName",
  help="The project that will be affected"
)

parser.add_argument(
  "-e", "--editor",
  dest="editor",
  choices=["vscode", "sublimetext"],
  help="Editor to use for opening a project"
)

parser.add_argument(
  "-p", "--path",
  type=Path,
  default=Path(os.getcwd()),
  help="Overrides the path, if not specified, the actual path is used"
)

parser.add_argument(
  '--preserve',
  action="store_true",
  help="Preserve project files on delete, with this disabled, the project files will be deleted"
)