#!/usr/bin/python3
"""
Console
"""
import cmd
import shlex
import os
from models import storage
import mysql.connector
from models.base_model import BaseModel
from models.socialmedia_post import SocialMediaPost
from models.create_post import Post
from models import analyze_post
from models.database.database_db import db
from models.user import User


# Set MySQL host, user, password, and database environment variables
# os.environ['Solysis_MYSQL_HOST'] = 'localhost'
# os.environ['Solysis_MYSQL_USER'] = 'solysis_dev'
# os.environ['Solysis_MYSQL_PWD'] = 'solysis_dev_pwd'
# os.environ['Solysis_MYSQL_DB'] = 'solysis_dev_db'


class SocialMediaConsole(cmd.Cmd):
    """ 
    Command interpreter for social media analysis console. 
    """
    prompt = "(solysis) "

    def do_quit(self, arg):
        """ 
        Quit command to exit the program. 
        """
        return True

    def do_EOF(self, arg):
        """ 
        EOF command to exit the program. 
        """
        print()
        return True

    def emptyline(self):
        """ 
        Do nothing on an empty input line. 
        """
        pass

    def help_quit(self):
        """ 
        Help documentation for quit command. 
        """
        print("Quit command to exit the program")

    def help_EOF(self):
        """ 
        Help documentation for EOF command. 
        """
        print("EOF command to exit the program")

    def do_create(self, arg):
        """
        Create a new instance of BaseModel, save it, and print the id.
        """
        args = shlex.split(arg)
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]

        if class_name == "CreatePost":
            self.do_create_post(arg)
            return

        if class_name not in globals():
            print("** class doesn't exist **")
            return
        new_instance = globals()[class_name]()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, arg):
        """
        Print the string representation of an instance.
        """
        args = shlex.split(arg)
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in globals():
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return

        instance_id = args[1]
        key = "{}.{}".format(class_name, instance_id)
        objects = storage.all()
        if key not in objects:
            print("** no instance found **")
            return
        print(objects[key])

    def do_destroy(self, arg):
        """
        Delete an instance based on the class name and id.
        """
        args = shlex.split(arg)
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in globals():
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        instance_id = args[1]
        key = "{}.{}".format(class_name, instance_id)
        objects = storage.all()
        if key not in objects:
            print("** no instance found **")
            return
        del objects[key]
        storage.save()

    def do_all(self, arg):
        """
        Print all string representation of all instances.
        """
        args = shlex.split(arg)
        objects = storage.all()
        if args and args[0] not in globals():
            print("** class doesn't exist **")
            return
        class_name = args[0] if args else None
        print([str(obj) for key, obj in objects.items() if
               not class_name or key.startswith(class_name)])

    def do_update(self, arg):
        """
        Update an instance based on the class name and id.
        """
        args = shlex.split(arg)
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in globals():
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        instance_id = args[1]
        key = "{}.{}".format(class_name, instance_id)
        objects = storage.all()
        if key not in objects:
            print("** no instance found **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        attribute_name = args[2]
        if len(args) < 4:
            print("** value missing **")
            return
        attribute_value_str = args[3]
        attribute_value = attribute_value_str
        try:
            # Attempt to cast the value to int or float
            attribute_value = int(attribute_value_str)
        except ValueError:
            try:
                attribute_value = float(attribute_value_str)
            except ValueError:
                pass
        setattr(objects[key], attribute_name, attribute_value)
        storage.save()

    def do_create_post(self, arg):
        """
        Create a new social media post.
        Usage: create <user_id> <platform> <message> [--schedule <schedule_time>]
        """
        args = shlex.split(arg)
        if len(args) < 4 or args[1] == "--schedule":
            print("** invalid command **")
            return
        user_id = args[0]
        platform = args[1]
        message = args[2]
        schedule_time = ""

        # Check if the user exists
        user_exists = False
        for user in storage.all(User).values():
            if user.id == user_id:
                user_exists = True
                break
    
        if not user_exists:
            print("** invalid User id **")
            return
        if "--schedule" in args:
            schedule_index = args.index("--schedule")
            if schedule_index + 1 >= len(args):
                print("** invalid command **")
                return
            schedule_time = args[schedule_index + 1]
            # Remove '--schedule' and the schedule time from args list
            args.remove("--schedule")
            args.remove(schedule_time)

        new_post = Post()
        new_post.user_id = user_id
        new_post.platform = platform
        new_post.message = message
        new_post.schedule_time = schedule_time
        new_post.save()
        print(new_post.id)

    def do_analyze_post(self, arg):
        """
        Analyze posts for a given user.
        Usage: analyze_post <user_id>
        """
        args = shlex.split(arg)
        if not args:
            print("** user_id missing **")
            return
        
        post_id = args[0]
        # Retrieve the post from storage
        all_posts = storage.all(Post)

        # Filter the post with the provided ID
        post = None
        for stored_post in all_posts.values():
            if stored_post.id == post_id:
                post = stored_post
                break
        if not post:
            print("** Post not found **")
            return

        # Extract the user_id from the post
        user_id = post.user_id
        
        print("User ID:", user_id)

        # Perform analysis
        analysis_results = analyze_post.analyze_posts_for_user(user_id)

        # Display the results
        print(analysis_results)


if __name__ == '__main__':
    SocialMediaConsole().cmdloop()
