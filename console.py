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
from models.base_model import BaseModel

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
        elif (len(strList) == 1):
            print("** instance id missing **")
        elif strList[0] in classes:
            iid = "{}.{}".format(strList[0], strList[1])
            dicti = storage.all().to_dict()
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
        elif strList[0] in classes:
            iid = "{}.{}".format(strList[0], strList[1])
            dicti = storage.all()
            if iid in dicti.keys():
                del dicti[iid]
            else:
                print("** no instance found **")

    def do_all(self, args):
        """prints string representation for all instances"""
        strList = args.split()
        if (len(strList) == 0):
            print(storage.all())
        elif (len(strList) == 1 and strList[0] in classes):
            print(storage.all())
            for x in storage.all():
                for y in x:
                    print(y)
        else:
            print("** class doesn't exist **")

    def do_update(self, args):
        """updates an instance"""
        strList = shlex.split(args)
        if (len(strList) == 0):
            print("** class name missing **")
        elif len(strList) == 1:
            print("** instance id missing **")
        elif len(strList) == 2:
            print("** attribute name missing **")
        elif len(strList) == 3:
            print("** value missing **")
        else:
            iid = "{}.{}".format(strList[0], strList[1])
            dicti = storage.all()
            if iid in dicti.keys():
                idict = dicti[iid]
                if strList[2] in idict.keys() and strList[2]:
                    idict[strList[2]] = strList[3]
                    storage.save()
                else:
                    idict[strList[2]] = strList[3]
                    storage.save()
            else:
                print("** no instance found **")
        else:
            print("** class doesn't exist **")

if __name__ == "__main__":
    HBNBCommand().cmdloop()
