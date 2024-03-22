#!/usr/bin/python3
"""
Console
"""
import cmd
import shlex
import os
from flask import Flask
import mysql.connector
from models.socialmedia_post import SocialMediaPost
from models.analytics_data import AnalyticsData
from models.user_profile import UserProfile
from models.engine.database import db
from models.user import User



# Set MySQL host, user, password, and database environment variables
os.environ['Solysis_MYSQL_HOST'] = 'localhost'
os.environ['Solysis_MYSQL_USER'] = 'solysis_dev'
os.environ['Solysis_MYSQL_PWD'] = 'solysis_dev_pwd'
os.environ['Solysis_MYSQL_DB'] = 'solysis_dev_db'


app = Flask(__name__)


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

    def do_create_post(self, arg):
        """ 
        Create a new social media post, save it, and print the id. 
        """
        args = shlex.split(arg)
        if len(args) < 2:
            print("** missing arguments **")
            return
        user_id = args[0]
        content = args[1]

        connection = None
        try:
            connection = mysql.connector.connect(
                host=os.getenv('Solysis_MYSQL_HOST'),
                user=os.getenv('Solysis_MYSQL_USER'),
                password=os.getenv('Solysis_MYSQL_PWD'),
                database=os.getenv('Solysis_MYSQL_DB')
            )
            cursor = connection.cursor()
            # Prepare SQL query to insert a new post
            sql_query = "INSERT INTO social_media_posts (user_id, content) VALUES (%s, %s)"
            cursor.execute(sql_query, (user_id, content))
            connection.commit()

            print("Post created successfully")
        except Exception as e:
            print("Error:", e)
        finally:
            if connection:
                cursor.close()
                connection.close()

    def do_show_post(self, arg):
        """ 
        Print the details of a social media post. 
        """
        args = shlex.split(arg)
        if not args:
            print("** post id missing **")
            return
        post_id = args[0]

        try:
            connection = mysql.connector.connect(
                host=os.getenv('Solysis_MYSQL_HOST'),
                user=os.getenv('Solysis_MYSQL_USER'),
                password=os.getenv('Solysis_MYSQL_PWD'),
                database=os.getenv('Solysis_MYSQL_DB')
            )
            cursor = connection.cursor(dictionary=True)

            # Prepare SQL query to select post details
            sql_query = "SELECT * FROM social_media_posts WHERE id = %s"
            cursor.execute(sql_query, (post_id,))
            post = cursor.fetchone()

            if post:
                print(post)
            else:
                print("** no post found **")
        except Exception as e:
            print("Error:", e)
        finally:
            if connection:
                cursor.close()
                connection.close()
        """post = storage.get(SocialMediaPost, post_id)
        if not post:
            print("** no post found **")
            return
        print(post)"""

    def do_analyze_post(self, arg):
        """ 
        Analyze the engagement metrics of a social media post. 
        """
        args = shlex.split(arg)
        if not args:
            print("** post id missing **")
            return
        post_id = args[0]
        try:
            connection = mysql.connector.connect(
                host=os.getenv('Solysis_MYSQL_HOST'),
                user=os.getenv('Solysis_MYSQL_USER'),
                password=os.getenv('Solysis_MYSQL_PWD'),
                database=os.getenv('Solysis_MYSQL_DB')
            )
            cursor = connection.cursor()

            # Placeholder for your analytics logic
            print("Engagement metrics: [Placeholder]")

        except Exception as e:
            print("Error:", e)
        finally:
            if connection:
                cursor.close()
                connection.close()
        """analytics_data = AnalyticsData.analyze_post_engagement(post_id)
        print("Engagement metrics:", analytics_data)"""

    def do_update_profile(self, arg):
        """ 
        Update the profile information of a user. 
        """
        args = shlex.split(arg)
        if len(args) < 2:
            print("** missing arguments **")
            return
        user_id = args[0]
        profile_data = args[1:]

        try:
            connection = mysql.connector.connect(
                host=os.getenv('Solysis_MYSQL_HOST'),
                user=os.getenv('Solysis_MYSQL_USER'),
                password=os.getenv('Solysis_MYSQL_PWD'),
                database=os.getenv('Solysis_MYSQL_DB')
            )
            cursor = connection.cursor()

            # Prepare SQL query to update user profile
            sql_query = "UPDATE user_profiles SET profile_data = %s WHERE user_id = %s"
            cursor.execute(sql_query, (profile_data, user_id))
            connection.commit()

            print("User profile updated successfully")
        except Exception as e:
            print("Error:", e)
        finally:
            if connection:
                cursor.close()
                connection.close()
        """UserProfile.update_profile(user_id, profile_data)
        print("User profile updated successfully")"""

    def do_create(self, arg):
        """
        Create a new instance of BaseModel, save it, and print the id.
        """
        args = shlex.split(arg)
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in globals():
            print("** class doesn't exist **")
            return

        try:
            connection = mysql.connector.connect(
                host=os.getenv('Solysis_MYSQL_HOST'),
                user=os.getenv('Solysis_MYSQL_USER'),
                password=os.getenv('Solysis_MYSQL_PWD'),
                database=os.getenv('Solysis_MYSQL_DB')
            )
            cursor = connection.cursor()

            # Placeholder SQL query for creating new instance
            sql_query = "INSERT INTO {} () VALUES ()".format(class_name)
            cursor.execute(sql_query)
            connection.commit()

            print("{} instance created successfully".format(class_name))
        except Exception as e:
            print("Error:", e)
        finally:
            if connection:
                cursor.close()
                connection.close()
        """new_instance = globals()[class_name]()
        new_instance.save()
        print(new_instance.id)"""

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

        try:
            connection = mysql.connector.connect(
                host=os.getenv('Solysis_MYSQL_HOST'),
                user=os.getenv('Solysis_MYSQL_USER'),
                password=os.getenv('Solysis_MYSQL_PWD'),
                database=os.getenv('Solysis_MYSQL_DB')
            )
            cursor = connection.cursor(dictionary=True)

            # Placeholder SQL query for fetching instance details
            sql_query = "SELECT * FROM {} WHERE id = {}".format(class_name, instance_id)
            cursor.execute(sql_query)
            instance = cursor.fetchone()

            if instance:
                print(instance)
            else:
                print("** no instance found **")
        except Exception as e:
            print("Error:", e)
        finally:
            if connection:
                cursor.close()
                connection.close()
        """key = "{}.{}".format(class_name, instance_id)
        objects = storage.all()
        if key not in objects:
            print("** no instance found **")
            return
        print(objects[key])"""

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
        try:
            connection = mysql.connector.connect(
                host=os.getenv('Solysis_MYSQL_HOST'),
                user=os.getenv('Solysis_MYSQL_USER'),
                password=os.getenv('Solysis_MYSQL_PWD'),
                database=os.getenv('Solysis_MYSQL_DB')
            )
            cursor = connection.cursor()

            # Placeholder SQL query for deleting instance
            sql_query = "DELETE FROM {} WHERE id = {}".format(class_name, instance_id)
            cursor.execute(sql_query)
            connection.commit()

            print("Instance deleted successfully")
        except Exception as e:
            print("Error:", e)
        finally:
            if connection:
                cursor.close()
                connection.close()
        """key = "{}.{}".format(class_name, instance_id)
        objects = storage.all()
        if key not in objects:
            print("** no instance found **")
            return
        del objects[key]
        storage.save()"""

    def do_all(self, arg):
        """
        Print all string representation of all instances.
        """
        args = shlex.split(arg)
        # objects = storage.all()
        if args and args[0] not in globals():
            print("** class doesn't exist **")
            return
        class_name = args[0] if args else None
    # Modify this part according to your data model and SQL schema
        try:
            connection = mysql.connector.connect(
                host=os.getenv('Solysis_MYSQL_HOST'),
                user=os.getenv('Solysis_MYSQL_USER'),
                password=os.getenv('Solysis_MYSQL_PWD'),
                database=os.getenv('Solysis_MYSQL_DB')
            )
            cursor = connection.cursor(dictionary=True)

            # Placeholder SQL query for fetching all instances of a class
            sql_query = "SELECT * FROM {}".format(class_name)
            cursor.execute(sql_query)
            instances = cursor.fetchall()

            for instance in instances:
                print(instance)
        except Exception as e:
            print("Error:", e)
        finally:
            if connection:
                cursor.close()
                connection.close()
        """print([str(obj) for key, obj in objects.items() if
               not class_name or key.startswith(class_name)])"""

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

    # Modify this part according to your data model and SQL schema
        try:
            connection = mysql.connector.connect(
                host=os.getenv('Solysis_MYSQL_HOST'),
                user=os.getenv('Solysis_MYSQL_USER'),
                password=os.getenv('Solysis_MYSQL_PWD'),
                database=os.getenv('Solysis_MYSQL_DB')
            )
            cursor = connection.cursor()

            # Placeholder SQL query for updating instance attribute
            sql_query = "UPDATE {} SET {} = '{}' WHERE id = {}".format(class_name, attribute_name, attribute_value, instance_id)
            cursor.execute(sql_query)
            connection.commit()
    
            print("Instance updated successfully")
        except Exception as e:
            print("Error:", e)
        finally:
            if connection:
                cursor.close()
                connection.close()
        """key = "{}.{}".format(class_name, instance_id)
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
        storage.save()"""

    # Additional methods for user management

    def do_sign_up(self, arg):
        """
        Sign up a new user.
        """
        args = shlex.split(arg)
        if len(args) < 2:
            print("** missing arguments **")
            return
        email = args[0]
        password = args[1]
        # Modify this part according to your data model and SQL schema
        try:
            connection = mysql.connector.connect(
                host=os.getenv('Solysis_MYSQL_HOST'),
                user=os.getenv('Solysis_MYSQL_USER'),
                password=os.getenv('Solysis_MYSQL_PWD'),
                database=os.getenv('Solysis_MYSQL_DB')
            )
            cursor = connection.cursor()

            # Check if the user already exists
            cursor.execute("SELECT * FROM users WHERE email = %s", (email,))
            existing_user = cursor.fetchone()

            if existing_user:
                print("** user already exists **")
                return

            # Placeholder SQL query for inserting new user
            sql_query = "INSERT INTO users (email, password) VALUES ('{}', '{}')".format(email, password)
            cursor.execute(sql_query)
            connection.commit()

            print("User signed up successfully")
        except Exception as e:
            print("Error:", e)
        finally:
            if connection:
                cursor.close()
                connection.close()
        """existing_user = storage.get_by(User, email=email)
        if existing_user:
            print("** user already exists **")
            return
        new_user = User(email=email, password=password)
        new_user.save()
        print("User signed up successfully")"""

    def do_log_in(self, arg):
        """
        Log in with existing user credentials.
        """
        args = shlex.split(arg)
        if len(args) < 2:
            print("** missing arguments **")
            return
        email = args[0]
        password = args[1]
        # Modify this part according to your data model and SQL schema
        try:
            connection = mysql.connector.connect(
                host=os.getenv('Solysis_MYSQL_HOST'),
                user=os.getenv('Solysis_MYSQL_USER'),
                password=os.getenv('Solysis_MYSQL_PWD'),
                database=os.getenv('Solysis_MYSQL_DB')
            )
            cursor = connection.cursor(dictionary=True)

            # Placeholder SQL query for fetching user by email and password
            sql_query = "SELECT * FROM users WHERE email = '{}' AND password = '{}'".format(email, password)
            cursor.execute(sql_query)
            user = cursor.fetchone()

            if user:
                print("User logged in successfully")
            else:
                print("** invalid email or password **")
        except Exception as e:
            print("Error:", e)
        finally:
            if connection:
                cursor.close()
                connection.close()
        """user = storage.get_by(User, email=email)
        if not user or user.password != password:
            print("** invalid email or password **")
            return
        # Set session variable or token for user's session
        print("User logged in successfully")"""

    def do_delete_account(self, arg):
        """
        Delete user account.
        """
        args = shlex.split(arg)
        if not args:
            print("** user id missing **")
            return
        user_id = args[0]
        try:
            connection = mysql.connector.connect(
                host=os.getenv('Solysis_MYSQL_HOST'),
                user=os.getenv('Solysis_MYSQL_USER'),
                password=os.getenv('Solysis_MYSQL_PWD'),
                database=os.getenv('Solysis_MYSQL_DB')
            )
            cursor = connection.cursor()

            # Placeholder SQL query for deleting user by id
            sql_query = "DELETE FROM users WHERE id = {}".format(user_id)
            cursor.execute(sql_query)
            connection.commit()

            print("User account deleted successfully")
        except Exception as e:
            print("Error:", e)
        finally:
            if connection:
                cursor.close()
                connection.close()
        """user = storage.get(User, user_id)
        if not user:
            print("** no user found **")
            return
        user.delete()
        print("User account deleted successfully")"""

if __name__ == '__main__':
    SocialMediaConsole().cmdloop()
