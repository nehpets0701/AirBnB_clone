#!/usr/bin/python3
import cmd


"""main console class with cmd module"""
class HBNBCommand(cmd.Cmd):
    """main console class with cmd module"""
    prompt = "(hbnb) "

    def do_quit(self, args):
        """quit function"""
        raise SystemExit

    def emptyline(self):
        """exception for empty line"""
        pass

    def do_create(self, args):
        """skeleton for create"""
        pass

    def do_show(self, args):
        """skeleton for show"""
        pass

    def do_destroy(self, args):
        """skeleton for destroy"""
        pass

    def do_all(self, args):
        """skeleton for all"""
        pass

    def do_update(self, args):
        """skeleton for update"""
        pass



if __name__ == "__main__":
    HBNBCommand().cmdloop()
