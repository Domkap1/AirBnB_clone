#!/usr/bin/python3
"""Defines the HBNB console."""
import cmd
from models.base_models import BaseModel
from models import storage
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
  """Defines the HBNB comaand interpreter."""
  prompt = "(hbnb)"
  intro = "Welcome to hbnb!"
  __classes = {
    "Amenity",
    "BaseModels",
    "City",
    "Place",
    "State",
    "Review",
    "User"
  }

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

def do_create(self, args):
  """Creates new instance of base model."""
  args = args.split()
  if not args:
    print("** class name missing **")
    return
  class_name = args[0]
  if class_name not in storage.all().keys()
  print("** class doesn't exist **")
  return
  new_obj = storage.all()[class_namce]()
  new_obj.save()
  print(f"{new_obj.id}")

def do_show(self, args):
  """Print string rep of an instance."""
  args = args.split()
  if not args:
    print("** class name missing **")
    return
  class_name = args[0]
  if class_name not in storage.all().keys():
    print("** class doesn't exist **")
    return
  if len(args) < 2:
    print("** instance id missing **")
    return
    obj_id = args[1]
    obj = storage.get(class_name,obj_id)
    if not obj:
      print("** no instance found **")
    else:
      print(obj)

def do_destroy(self, args):
  """Deletes an instance."""
  args = args.split()
  obj = storage.get(class_name,obj_id)
  if not obj:
    print("** no instance found **")
  else:
    storage.delete(obj)
    storage.save()
    print(f"{class_name} {obj_id} deleted")

def do_all(self, args):
  """Prints all string rep of instance."""
  args = args.split()
  if args:
    class_name = args[0]
    if class_name not in storage.all().keys():
      print("** class doesn't exist **")
      return
    instances = storage.all(class_name)
  else:
    instances = storage.all()
  all_strings = [str(instance) for instance in instances.values()]
  print(all_strings)

def do_count(self, args):
  """Retrieve number of instance of a class."""
  args = args.split()
  count = 0
  for obj in storage.all().values():
    if args[0] == obj.__class__.__name__:
      count += 1
  print(count)

def do_update(self, args):
  """Updates class instance of given id."""
  args = args.split()
  obj_dict = storage.all()
  if len(args) == 0:
    print("**bclass doesn't exist **")
    return False
  if len(args) == 1:
    print("** instance id missing **")
    return False
  if "{}.{}".format(args[0], args[1]) not in obj_dict.keys():
    print("** no instance found **")
    return False
  if len(args) == 2:
    print("** attribute name missing **")
    return False
  if len(args) == 3:
    try:
      type(eval(args[2])) != dict
    except NameError:
      print("** value missing **")
      return False
if __name__ == '__main__':
  HBNBCommand().cmdloop()
