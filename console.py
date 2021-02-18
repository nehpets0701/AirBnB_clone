#!/usr/bin/python3
"""main console class with cmd module"""
import cmd
import shlex
from models import storage
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User

classes = {"BaseModel": BaseModel, "State": State, "City": City,
           "Amenity": Amenity, "Place": Place, "Review": Review, "User": User}


class HBNBCommand(cmd.Cmd):
    """main console class with cmd module"""
    prompt = "(hbnb) "

    def do_quit(self, args):
        """quit function"""
        raise SystemExit

    def do_EOF(self, args):
        """EOF function"""
        raise SystemExit

    def emptyline(self):
        """exception for empty line"""
        pass

    def do_create(self, args):
        """creates a new instances of base model"""
        if args in classes:
            new = classes[args]()
            new.save()
            print(new.id)
        elif (len(args) == 0):
            print("** class name missing **")
        else:
            print("** class doesn't exist **")

    def do_show(self, args):
        """shows string representation of an instance"""
        strList = args.split()
        if (len(strList) == 0):
            print("** class name missing **")
        elif strList[0] not in classes:
            print("** class doesn't exist **")
        elif (len(strList) == 1):
            print("** instance id missing **")
        else:
            iid = "{}.{}".format(strList[0], strList[1])
            dicti = storage.all()
            if iid in dicti.keys():
                print(dicti[iid])
            else:
                print("** no instance found **")

    def do_destroy(self, args):
        """destroys an instance"""
        strList = args.split()
        if (len(strList) == 0):
            print("** class name missing **")
        elif (len(strList) == 1):
            print("** instance id missing **")
        elif strList[0] not in classes:
            print("** class doesn't exist **")
        else:
            iid = "{}.{}".format(strList[0], strList[1])
            dicti = storage.all()
            if iid in dicti.keys():
                del dicti[iid]
            else:
                print("** no instance found **")

    def do_all(self, args):
        """prints string representation for all instances"""
        strList = args.split()
        new = []
        if (len(strList) == 0):
            for x in storage.all():
                new.append(str(storage.all()[x]))
            print(new)
        elif strList[0] in classes:
            for x in storage.all():
                num = x.split(".")
                if num[0] == strList[0]:
                    new.append(str(storage.all()[x]))
            print(new)
        else:
            print("** class doesn't exist **")

    def do_update(self, args):
        """updates an instance"""
        strList = shlex.split(args)
        flag = 0
        if (len(strList) == 0):
            print("** class name missing **")
        elif len(strList) == 1:
            print("** instance id missing **")
        elif len(strList) == 2:
            print("** attribute name missing **")
        elif len(strList) == 3:
            print("** value missing **")
        elif strList[0] not in classes:
            print("** class doesn't exist **")
        else:
            iid = "{}.{}".format(strList[0], strList[1])
            for key, value in storage.all().items():
                if key == iid:
                    setattr(value, strList[2], str(strList[3]))
                    value.save()
                    flag = 1
            if flag == 0:
                print("** no instance found **")

if __name__ == "__main__":
    HBNBCommand().cmdloop()
