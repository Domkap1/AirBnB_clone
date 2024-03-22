#!/usr/bin/python3
"""Defines the HBNB console."""
import cmd
from models.base_models import BaseModel


class HBNBCommand(cmd.Cmd):
  """Defines the HBNB comaand interpreter."""
  prompt = "(hbnb)"
  intro = "Welcome to hbnb!"

def emptyline(self):
  """Pass empty line."""
  pass
  
def do_quit(self, arg):
  """Quits the command interpreter."""
  print("Exit the hbnb command interpreter")
  exit()

def do_EOF(self, arg):
  """Exit the command interpreter on EOF."""
  print()
  exit()

if __name__ == '__main__':
  HBNBCommand().cmdloop()
