#!/usr/bin/python3
"""Defines the HBNB console."""
import cmd
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review
from models.engine.file_storage import FileStorage as storage

class HBNBCommand(cmd.Cmd):
    """Defines the HBNB command interpreter."""
    prompt = "(hbnb) "
    intro = "Welcome to hbnb!"
    classes = ["Amenity", "BaseModel", "City", "Place", "State", "Review", "User"]

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
        if class_name not in self.classes:
            print("** class doesn't exist **")
            return
        new_obj = eval(class_name)()
        new_obj.save()
        print(new_obj.id)

    def do_show(self, args):
        """Print string rep of an instance."""
        args = args.split()
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in self.classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        obj_id = args[1]
        obj = storage.get(class_name, obj_id)
        if not obj:
            print("** no instance found **")
        else:
            print(obj)

    def do_destroy(self, args):
        """Deletes an instance."""
        args = args.split()
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in self.classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        obj_id = args[1]
        obj = storage.get(class_name, obj_id)
if not obj:
            print("** no instance found **")
        else:
            storage.delete(obj)
            storage.save()
            print(f"{class_name} {obj_id} deleted")

    def do_all(self, args):
        """Prints all string rep of instance."""
        args = args.split()
        if args and args[0] not in self.classes:
            print("** class doesn't exist **")
            return
        if args:
            instances = storage.all(args[0])
        else:
            instances = storage.all()
        all_strings = [str(instance) for instance in instances.values()]
        print(all_strings)

    def do_count(self, args):
        """Retrieve number of instance of a class."""
        args = args.split()
        if not args:
            print("** class name missing **")
            return
        if args[0] not in self.classes:
            print("** class doesn't exist **")
            return
        count = 0
        for obj in storage.all().values():
            if args[0] == obj.__class__.__name__:
                count += 1
        print(count)

    def do_update(self, args):
        """Updates class instance of given id."""
        args = args.split()
        if not args:
            print("** class name missing **")
            return
        if args[0] not in self.classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return
        class_name = args[0]
        obj_id = args[1]
        obj = storage.get(class_name, obj_id)
        if not obj:
            print("** no instance found **")
            return
        setattr(obj, args[2], args[3])
        storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()

